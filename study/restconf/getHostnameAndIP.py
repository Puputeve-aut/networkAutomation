import requests
import urllib3

class restconf():
    '''
    Used for our Restconf stuff
    '''
    def __init__(self):
        self.baseURL = 'https://c8k.homelab.com/restconf/data/'
        self.yangContainer = 'Cisco-IOS-XE-native:native/'
        self.devUser = 'restconf'
        self.devPass = 'cisco'

    def restConnection(self, method, yangLeaf="", payload=""):
        '''
        Create connection to Router with RESTCONF
        '''
        
        headers= {
            'content-Type' : 'application/yang-data+json',
            'Accept' : 'application/yang-data+json',
        }
        # disable HTTPS check 
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        try:
            return requests.request(method, self.baseURL + self.yangContainer + yangLeaf,
                                    auth=(self.devUser, self.devPass),
                                    verify=False,
                                    data=payload, 
                                    headers=headers)       
                
        except requests.exceptions.ConnectionError:
            print("Connection Error!")
            
        except requests.exceptions.Timeout:
            print("Timeout")
            
        except:
            print("Not Working!")           
    
    def getHostname(self):
        '''
        Get router hostname
        '''
        
        leafname = 'hostname'
        return self.restConnection('GET', leafname)

    def getLoopbackIP(self):
        '''
        Get Loopback0 IP
        '''
        
        leafname = 'interface/Loopback=100/ip/address/primary/address'
        return self.restConnection('GET', leafname)
    
connectRouter = restconf()
    
def main():
    
    try:
        deviceHostname = connectRouter.getHostname().json()
        print(deviceHostname['Cisco-IOS-XE-native:hostname'])

        deviceLoopbackIP = connectRouter.getLoopbackIP().json()
        print(deviceLoopbackIP['Cisco-IOS-XE-native:address'])
        
    except AttributeError:
        print("Coennection Failed")
        


if __name__ == '__main__':
    main()