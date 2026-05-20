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

commands = [
    'default interface GigabitEthernet0/2',
    'default interface GigabitEthernet0/3',
    'no interface Loopback0'
    ]
all_routers = [R1, R2, R3]

#The config is different and i dont know how to make a for loop to use different config for each router, so i will just connect to each router and send the config separately. 
#I will try to make a for loop in the future to make it more efficient.

for router in all_routers:
    # Establish SSH connection to the device
    net_connect = ConnectHandler(**router)
    net_connect.enable()
    print("Decommissioning interfaces: " + router['host'])
    net_connect.send_config_set(commands)

    # Close the connection
    net_connect.disconnect()
    