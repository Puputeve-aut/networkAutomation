from netmiko import ConnectHandler
from getpass import getpass
import os
# Get device credentials
username = "cisco"
password = getpass(prompt="Enter device password: ")

# Define device connection parameters
#Secret password is the same as login password in this case, but it can be different.
R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.20.71',
    'host': 'R1',
    'username': username,
    'password': password,
    'secret': password
}

R2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.20.72',
    'host': 'R2',
    'username': username,
    'password': password,
    'secret': password
}

R3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.20.73',
    'host': 'R3',
    'username': username,
    'password': password,
    'secret': password
}

# Create a list of devices to connect to
all_routers = [R1, R2, R3]

for router in all_routers:
    net_connect = ConnectHandler(**router)
    net_connect.enable()
    print("*****" * 20)
    print(f"Configuring {router['host']}")

    print(net_connect.send_config_from_file(r'study/netmiko/configuration/intDescription/netconfUser.txt'))
    
    net_connect.disconnect()