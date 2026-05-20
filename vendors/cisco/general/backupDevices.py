import getpass
from automation import find_project_root, load_inventory, backup_device
#---------------------------------------------------------------------------------------------------------------------

def main():
    # 1. Automatically find the project root folder directory
    try:
        root_dir = find_project_root("networkAutomation")
    except FileNotFoundError as e:
        print(e)
        return

    # 2. Load YAML inventory mapping
    device_map = load_inventory(root_dir)
    if device_map is None:
        return
    
    print("=" * 50)
    print("CISCO CONFIGURATION BACKUP TOOL")
    print("=" * 50)
    
    # 3. Collect Device Credentials
    print("[*] Please enter the SSH credentials for yor devices:")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")
    secret = getpass.getpass("Enable Secret (Press Enter if not required): ").strip()

    # 4. Ask user for backup scope
    print("\nBackup Scope:")
    print("1. Backup a single specific device")
    print("2. Backup ALL devices in inventory")
    choice = input("Select an option (1 or 2): ").strip()

    # 5. Handle choices
    if choice == "1":
        target_hostname = input("\nEnter device hostname (e.g., R1, C8K-Switch): ").strip()
        if target_hostname in device_map:
            target_ip = device_map[target_hostname]
            backup_device(target_hostname, target_ip, root_dir, username, password, secret)
        else:
            print(f"[!] Error: Hostname '{target_hostname}' doesn't exist in inventory.yaml")
            print(f"Available options: {', '.join(device_map.keys())}")

    elif choice == "2":
        print(f"\n[+] Starting bulk backup for {len(device_map)} devices...")
        for hostname, ip_address in device_map.items():
            backup_device(hostname, ip_address, root_dir, username, password, secret)
        print("\n[✓] Bulk backup process completed.")

    else:
        print("[!] Invalid option selected. Exiting script.")

if __name__ == "__main__":
    main()