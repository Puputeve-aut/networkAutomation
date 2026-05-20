from netmiko import ConnectHandler
from getpass import getpass

# Get device credentials
devUser = "cisco"
devPass = getpass(prompt="Enter device password: ")

# Define device connection parameters
R1 = {
    "device_type": "cisco_ios",
    "host": "192.168.20.71",
    "username": devUser,
    "password": devPass,
}

R2 = {
    "device_type": "cisco_ios",
    "host": "192.168.20.72",
    "username": devUser,
    "password": devPass,
}

R3 = {
    "device_type": "cisco_ios",
    "host": "192.168.20.73",
    "username": devUser,
    "password": devPass,
}

# Create a list of devices to connect to
all_routers = [R1, R2, R3]

commands = ["show ip ospf neighbor", "show ip route ospf | b Gate", "show clock"]

# Loop through each device and perform operations
for router in all_routers:
    # Establish SSH connection to the device
    net_connect = ConnectHandler(**router)

    # Send a command and print the output
    for command in commands:
        print("*****" * 20)
        output = net_connect.send_command(command, strip_command=False)
        print(net_connect.find_prompt(), output)
    
    # Close the connection
    net_connect.disconnect()