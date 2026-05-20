# My first Netmiko program
# Import the Netmiko Library
# The Netmiko library provides SSH connectivity to network devices for automation.
from netmiko import ConnectHandler
from getpass import getpass

# Get device credentials
devUser = "cisco"
devPass = getpass(prompt="Enter device password: ")

# Define device connection parameters
#Secret password is the same as login password in this case, but it can be different.
R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.20.71',
    'host': 'R1',
    'username': devUser,
    'password': devPass,
    'secret': devPass
}

R2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.20.72',
    'host': 'R2',
    'username': devUser,
    'password': devPass,
    'secret': devPass
}

R3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.20.73',
    'host': 'R3',
    'username': devUser,
    'password': devPass,
    'secret': devPass
}

# Create a list of devices to connect to
all_routers = [R1, R2, R3]

for router in all_routers:
    # Establish SSH connection to the device
    net_connect = ConnectHandler(**router)
    net_connect.enable()
    print("Saving configuration on device: " + router['host'])  
    net_connect.send_command("write memory")
     
    # Close the connection
    net_connect.disconnect()