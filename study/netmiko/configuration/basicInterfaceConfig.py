from netmiko import ConnectHandler
from getpass import getpass


# Define Login Credentials
username = 'cisco'
password = getpass('Enter password: ')

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

R1_commands = [
    'interface Loopback0',
    'ip address 192.168.255.1 255.255.255.255',
    'interface GigabitEthernet0/2',
    'ip address 10.1.2.1 255.255.255.0',
    'interface GigabitEthernet0/3',
    'ip address 10.1.3.1 255.255.255.0',
    'router ospf 1',
    'network 0.0.0.0 255.255.255.255 area 0'
    ]
R2_commands = [
    'interface Loopback0',
    'ip address 192.168.255.2 255.255.255.255',
    'interface GigabitEthernet0/2',
    'ip address 10.1.2.2 255.255.255.0',
    'interface GigabitEthernet0/3',
    'ip address 10.2.3.2 255.255.255.0',
    'router ospf 1',
    'network 0.0.0.0 255.255.255.255 area 0'
    ]
R3_commands = [
    'interface Loopback0',
    'ip address 192.168.255.3 255.255.255.255',
    'interface GigabitEthernet0/2',
    'ip address 10.1.3.3 255.255.255.0',
    'interface GigabitEthernet0/3',
    'ip address 10.2.3.3 255.255.255.0',
    'router ospf 1',
    'network 0.0.0.0 255.255.255.255 area 0'
    ]

all_routers = [R1, R2, R3]

#The config is different and i dont know how to make a for loop to use different config for each router, so i will just connect to each router and send the config separately. 
#I will try to make a for loop in the future to make it more efficient.

# Connect to R1
net_connect = ConnectHandler(**R1)
net_connect.enable()
print("configuring interfaces: " + R1['host'])
net_connect.send_config_set(R1_commands)
net_connect.disconnect()

# Connect to R2
net_connect = ConnectHandler(**R2)
net_connect.enable()
print("configuring interfaces: " + R2['host'])
net_connect.send_config_set(R2_commands)
net_connect.disconnect()

# Connect to R3
net_connect = ConnectHandler(**R3)
net_connect.enable()
print("configuring interfaces: " + R3['host'])
net_connect.send_config_set(R3_commands)
net_connect.disconnect()