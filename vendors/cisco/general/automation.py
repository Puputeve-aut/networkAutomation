import re
import getpass
import time
from netmiko import ConnectHandler

# --- AUTHENTICATION ---
USERNAME = input("Enter Network SSH Username: ")
PASSWORD = getpass.getpass("Enter Network SSH Password: ")

def normalize_mac(mac_str):
    """Converts a raw string into a Cisco formatted MAC address (aabb.ccdd.eeff)"""
    clean_mac = re.sub(r'[^a-fA-F0-9]', '', mac_str).lower()
    return f"{clean_mac[0:4]}.{clean_mac[4:8]}.{clean_mac[8:12]}" if len(clean_mac) == 12 else None

def trace_via_router_jump(router_ip, user_input):
    print(f"\n[*] Logging into Edge Router ({router_ip})...")
    
    # Establish base connection to the router
    router_conn = ConnectHandler(
        device_type='cisco_ios', 
        host=router_ip, 
        username=USERNAME, 
        password=PASSWORD, 
        secret=PASSWORD
    )
    
    # 1. IDENTIFY INPUT TYPE & LOOKUP IN ARP TABLE
    # Check if the input looks like an IP address
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
    
    # Parse the ARP table line dynamically
    for line in lines:
        chunks = line.split()
        if len(chunks) >= 6:
            current_line_ip = chunks[1]
            current_line_mac = normalize_mac(chunks[3])
            current_line_interface = chunks[5]
            
            if is_ip and current_line_ip == target_ip:
                target_mac = current_line_mac
                router_interface = current_line_interface
                break
            elif not is_ip and current_line_mac == target_mac:
                target_ip = current_line_ip
                router_interface = current_line_interface
                break
                
    if not target_mac or not router_interface:
        print(f"[-] Could not find a matching active ARP entry for '{user_input}' on the router.")
        router_conn.disconnect()
        return

    print(f"[+] Match Found! IP: {target_ip} | MAC: {target_mac} | Router Interface: {router_interface}")
    
    # 2. FIND THE FIRST SWITCH IP VIA CDP
    base_interface = router_interface.split('.')[0]
    cdp_out = router_conn.send_command(f"show cdp neighbors {base_interface} detail")
    neighbor_ip_match = re.search(r'(?:IP address|IPv4 Address):\s+([0-9\.]+)', cdp_out)
    
    if not neighbor_ip_match:
        print(f"[-] No downstream switch discovered via CDP on interface {base_interface}.")
        router_conn.disconnect()
        return
        
    next_switch_ip = neighbor_ip_match.group(1)
    print(f"[-->] Core router connects directly to Switch at: {next_switch_ip}")
    
    # 3. JUMP FROM ROUTER TO SWITCH VIA NATIVE SSH
    print(f"[*] Command: Executing 'ssh -l {USERNAME} {next_switch_ip}' from R1 shell...")
    
    ssh_command = f"ssh -l {USERNAME} {next_switch_ip}"
    router_conn.write_channel(ssh_command + "\n")
    time.sleep(2)
    
    output = router_conn.read_channel()
    
    # Handle the SSH password prompt of the switch
    if "password:" in output.lower():
        router_conn.write_channel(PASSWORD + "\n")
        time.sleep(2)
        output = router_conn.read_channel()
    
    # Verify we successfully reached the switch prompt
    if ">" in output or "#" in output:
        print(f"[+] Successfully tunneled into Switch ({next_switch_ip}) via R1!")
    else:
        print(f"[-] Failed to tunnel into switch. Shell output: \n{output}")
        router_conn.disconnect()
        return

    # 4. TRACE MAC ON THE SWITCH (Inside the tunnel)
    router_conn.read_channel()  # Clear buffer
    
    mac_command = f"show mac address-table address {target_mac}"
    router_conn.write_channel(mac_command + "\n")
    time.sleep(2)
    mac_table_out = router_conn.read_channel()
    
    port_match = re.search(r'(Gi\d/\d/\d+|Fa\d/\d/\d+|Te\d/\d/\d+|Gi\d/\d|Fa\d/\d|Po\d+)', mac_table_out)
    
    if port_match:
        final_port = port_match.group(1)
        print("\n" + "="*60)
        print(f" SUCCESS (PROXY TRACE VIA ROUTER)")
        print(f" Target Device IP : {target_ip}")
        print(f" Target MAC       : {target_mac}")
        print(f" Switch Address   : {next_switch_ip}")
        print(f" Physical Port    : {final_port}")
        print("="*60)
    else:
        print(f"[-] MAC address not found in the switch's CAM table. Output:\n{mac_table_out}")
    
    # Clean exit out of the switch back to the router, then close connection
    router_conn.write_channel("exit\n")
    router_conn.disconnect()

# --- RUNNER ---
if __name__ == "__main__":
    print("=" * 60)
    print(" HYBRID IP/MAC ROUTER-JUMP PROXY TRACER")
    print("=" * 60)
    
    ROUTER_GATEWAY = input("Enter Reachable Router IP (e.g., 192.168.20.1): ").strip()
    
    # User can type "192.168.30.51" OR "5000.0007.0000" (any standard format)
    USER_SEARCH = input("Enter Target IP or MAC Address to locate: ").strip()
    
    trace_via_router_jump(ROUTER_GATEWAY, USER_SEARCH)