from ncclient import manager
from jinja2 import Template

def main():
    HOST = '192.168.20.30'
    PORT = 830
    devUser = 'netconf'
    devPass = 'cisco'
    
    # Establish a NETCONF connection to the device
    netconf_connection = manager.connect(host=HOST,
                                         port=PORT,
                                         username=devUser,
                                         password=devPass,
                                         device_params={'name': 'csr'},
                                         hostkey_verify=False)
    
    # Define the XML configuration template for the loopback interface
    routerConfig = '''
    <config xmlns='urn:ietf:params:xml:ns:netconf:base:1.0'>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>{{ HOSTNAME }}</hostname>
        <interface>
          <Loopback>
            <name>{{ LOOPBACK_INTERFACE }}</name>
            <description>{{ LOOPBACK_DESCRIPTION }}</description>
            <ip>
              <address>
                <primary>
                  <address>{{ LOOPBACK_IP }}</address>
                  <mask>255.255.255.255</mask>
                </primary>
              </address>
            </ip>
          </Loopback>
        </interface>
      </native>
    </config>
    '''
    # Use Jinja2 to render the template with the variables
    interface_template = Template(routerConfig)
    interface_render = interface_template.render(HOSTNAME='C8K',
                                               LOOPBACK_INTERFACE='100',
                                               LOOPBACK_DESCRIPTION='Loopback Interface by netconf',
                                               LOOPBACK_IP='10.0.0.100')

    # Push the configuration to the device
    commit = False
    
    print("Pushing Config!")
    netconf_connection.edit_config(config=interface_render, target='running',)

if __name__ == "__main__":
    main()