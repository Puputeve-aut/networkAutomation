from netmiko import ConnectHandler
from getpass import getpass

# Get device credentials
username = "cisco"
password = getpass(prompt="Enter device password: ")

# Define device connection parameters
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

# Loop through each device and perform operations
for router in all_routers:
    # Establish SSH connection to the device
    net_connect = ConnectHandler(**router)
    
    print("*****" * 20)
    # Send a command and print the output
    output = net_connect.send_command("show  int description | e admin", strip_command=False)
    print(net_connect.find_prompt(), output)
    
    
    # Close the connection
    net_connect.disconnect()