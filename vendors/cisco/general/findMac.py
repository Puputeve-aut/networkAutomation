import re
import sys
import time
from netmiko import ConnectHandler

def get_clean_input(prompt_text):
    """Bypasses standard input glitches by reading directly from stdin stream."""
    sys.stdout.write(prompt_text)
    sys.stdout.flush()
    return sys.stdin.readline().strip()

def normalize_mac(mac_str):
    """Converts various MAC formats to Cisco continuous hex format (aabb.ccdd.eeff)"""
    clean_mac = re.sub(r'[^a-fA-F0-9]', '', mac_str).lower()
    return f"{clean_mac[0:4]}.{clean_mac[4:8]}.{clean_mac[8:12]}" if len(clean_mac) == 12 else None

def jump_to_switch_from_router(router_conn, switch_ip, username, password):
    """Opens a clean SSH tunnel from the Router shell to the target Switch IP."""
    print(f"[*] Router executing: 'ssh -l {username} {switch_ip}'...")
    ssh_command = f"ssh -l {username} {switch_ip}"
    router_conn.write_channel(ssh_command + "\n")
    time.sleep(2)
    
    output = router_conn.read_channel()
    if "password:" in output.lower():
        router_conn.write_channel(password + "\n")
        time.sleep(2)
        output = router_conn.read_channel()
        
    if ">" in output or "#" in output:
        router_conn.write_channel("terminal length 0\n")
        time.sleep(0.5)
        router_conn.write_channel("terminal width 0\n")
        time.sleep(0.5)
        router_conn.read_channel()  
        return True
    return False

def trace_via_router_jump(router_ip, user_input, username, password):
    print(f"\n[*] Connecting to Anchor Router ({router_ip})...")
    
    router_conn = ConnectHandler(
        device_type='cisco_ios', 
        host=router_ip, 
        username=username, 
        password=password, 
        secret=password
    )
    
    router_conn.send_command("terminal length 0")
    router_conn.send_command("terminal width 0")
    
    # ARP TABLE LOOKUP PHASE
    is_ip = re.match(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}', user_input)
    target_mac = None
    target_ip = None
    router_interface = None
    
    if is_ip:
        target_ip = user_input
        print(f"[*] Querying ARP table on router for IP: {target_ip}...")
        arp_out = router_conn.send_command(f"show arp | include {target_ip}")
    else:
        target_mac = normalize_mac(user_input)
        if not target_mac:
            print("[-] Error: The MAC address format typed is invalid.")
            router_conn.disconnect()
            return
        print(f"[*] Querying ARP table on router for MAC: {target_mac}...")
        arp_out = router_conn.send_command(f"show arp | include {target_mac}")
    
    lines = arp_out.strip().splitlines()
    for line in lines:
        chunks = line.split()
        if len(chunks) >= 6:
            if is_ip and chunks[1] == target_ip:
                target_mac = normalize_mac(chunks[3])
                router_interface = chunks[5]
                break
            elif not is_ip and normalize_mac(chunks[3]) == target_mac:
                target_ip = chunks[1]
                router_interface = chunks[5]
                break
                
    if not target_mac or not router_interface:
        print(f"[-] Could not find a matching active ARP entry for '{user_input}' on the router.")
        router_conn.disconnect()
        return

    print(f"[+] Match Found! IP: {target_ip} | MAC: {target_mac} | Router Interface: {router_interface}")
    
    base_interface = router_interface.split('.')[0]
    cdp_out = router_conn.send_command(f"show cdp neighbors {base_interface} detail")
    neighbor_ip_match = re.search(r'(?:IP address|IPv4 Address):\s+([0-9\.]+)', cdp_out)
    
    if not neighbor_ip_match:
        print(f"[-] No downstream switch discovered via CDP on interface {base_interface}.")
        router_conn.disconnect()
        return
        
    current_switch_ip = neighbor_ip_match.group(1)
    
    # TRACE LOOP
    final_port = None
    switches_checked = []

    while True:
        print(f"\n[*] Auditing Switch: {current_switch_ip}")
        switches_checked.append(current_switch_ip)
        
        if not jump_to_switch_from_router(router_conn, current_switch_ip, username, password):
            print(f"[-] Failed to jump from Router to Switch {current_switch_ip}.")
            break
            
        router_conn.read_channel()  
        
        router_conn.write_channel(f"show mac address-table address {target_mac}\n")
        time.sleep(1.5)
        mac_table_out = router_conn.read_channel()
        
        port_match = re.search(r'(Gi\d/\d/\d+|Fa\d/\d/\d+|Te\d/\d/\d+|Gi\d/\d|Fa\d/\d|Po\d+)', mac_table_out)
        if not port_match:
            print(f"[-] MAC address lost. Not found in CAM table of {current_switch_ip}.")
            router_conn.write_channel("exit\n")
            time.sleep(0.5)
            break
            
        current_port = port_match.group(1)
        print(f"[+] Found MAC on interface: {current_port}")
        
        router_conn.write_channel(f"show cdp neighbors {current_port} detail\n")
        time.sleep(1.5)
        cdp_out = router_conn.read_channel()
        
        next_hop_match = re.search(r'(?:IP address|IPv4 Address):\s+([0-9\.]+)', cdp_out)
        
        router_conn.write_channel("exit\n")
        time.sleep(1)
        router_conn.read_channel()  
        
        if next_hop_match:
            next_switch_ip = next_hop_match.group(1)
            
            if next_switch_ip in switches_checked or next_switch_ip == router_ip:
                final_port = current_port
                break
                
            print(f"[-->] Trunk link detected on {current_port}. Target is past Switch: {next_switch_ip}")
            current_switch_ip = next_switch_ip
            continue
        else:
            print(f"[!] No downstream switches on {current_port}. Edge port found!")
            final_port = current_port
            break

    if final_port:
        print("\n" + "="*60)
        print(f" SUCCESS: EDGE PORT IDENTIFIED (ROUTER-PROXY)")
        print(f" Target Device IP  : {target_ip}")
        print(f" Target MAC        : {target_mac}")
        print(f" Access Switch IP  : {current_switch_ip}")
        print(f" Physical Edge Port: {final_port}")
        print(f" Switch Hop Path   : {' -> '.join(switches_checked)}")
        print("="*60)
        
    router_conn.disconnect()


# --- STREAM-BASED PROMPT GATHERING ---
if __name__ == "__main__":
    print("=" * 60)
    print(" L2 TRUNK-MARCHING PORT LOCATOR")
    print("=" * 60)
    
    # Utilizing sys.stdin.readline() wrapper to guarantee no terminal environment breaks
    ROUTER_GATEWAY = get_clean_input("Step 1: Enter Reachable Router IP: ")
    USER_SEARCH    = get_clean_input("Step 2: Enter Target IP or MAC to locate: ")
    INPUT_USER     = get_clean_input("Step 3: Enter Network SSH Username: ")
    INPUT_PASS     = get_clean_input("Step 4: Enter Network SSH Password: ")
    
    print(f"\n[+] Processing... Starting dynamic trace for target: {USER_SEARCH}")
    trace_via_router_jump(ROUTER_GATEWAY, USER_SEARCH, INPUT_USER, INPUT_PASS)