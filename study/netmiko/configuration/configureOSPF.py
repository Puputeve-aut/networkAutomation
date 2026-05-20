from netmiko import ConnectHandler
from getpass import getpass

# Get device credentials
devUser = "cisco"
devPass = getpass(prompt="Enter device password: ")

# Define device connection parameters
#Secret password is the same as login password in this case, but it can be different.
R1 = {
    "device_type": "cisco_ios",
    "host": "192.168.20.71",
    "username": devUser,
    "password": devPass,
    "secret": devPass
}

R2 = {
    "device_type": "cisco_ios",
    "host": "192.168.20.72",
    "username": devUser,
    "password": devPass,
    "secret": devPass
}

R3 = {
    "device_type": "cisco_ios",
    "host": "192.168.20.73",
    "username": devUser,
    "password": devPass,
    "secret": devPass
}

# Create a list of devices to connect to
all_routers = [R1, R2, R3]

configOSPF = ['router ospf 10',
              'network 10.0.0.0 0.255.255.255 area 0',
              'network 172.16.0.0 0.0.255.255 area 0',
              'network 192.168.20.0 0.0.0.255 area 0'
              ]

# Loop through each router and configure OSPF
for router in all_routers:
    # Establish SSH connection to the device
    net_connect = ConnectHandler(**router)
    
    net_connect.enable()
    print("Configuring OSPF on device: " + router['host'])
    # Send the OSPF configuration commands to the device
    net_connect.send_config_set(configOSPF)
     
    # Close the connection
    net_connect.disconnect()