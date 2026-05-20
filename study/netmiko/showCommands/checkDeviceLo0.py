from netmiko import ConnectHandler
from getpass import getpass
import re

def getIP(fullOutput):
    # Use regular expression to find all IP addresses in the output
    rePattern = re.compile(r"^Loopback0\s+(\d{1,3}(?:\.\d{1,3}){3})", re.MULTILINE)
    return re.findall(rePattern, fullOutput)

def main():
    username = "cisco"
    password = getpass("Enter password: ")

    # Define device connection parameters
    R1 = {
        "device_type": "cisco_ios",
        "ip": "192.168.20.71",
        "host": "R1",
        "username": username,
        "password": password,
    }

    R2 = {
        "device_type": "cisco_ios",
        "ip": "192.168.20.72",
        "host": "R2",
        "username": username,
        "password": password,
    }

    R3 = {
        "device_type": "cisco_ios",
        "ip": "192.168.20.73",
        "host": "R3",
        "username": username,
        "password": password,
    }

    # Create a list of devices to connect to
    all_routers = [R1, R2, R3]
    
    # Loop through each device, connect, and retrieve the IP address of Loopback0
    for router in all_routers:
        networkConnect = ConnectHandler(**router)
        output = networkConnect.send_command("show ip int brief")
        deviceIP = getIP(output)
        
        print(f"{router['host']} Management Addresses: {deviceIP[0]}")
    
if __name__ == "__main__":
    main()