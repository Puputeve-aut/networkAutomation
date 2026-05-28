///BGP Commands///

router bgp xxx                                                          /Create BGP
neighbor xx.xx.xx.xx remote-as yyy                                      /Add peers to BGP
neighbor xx.xx.xx.xx ebgp-multihop                                      /Set peer TTL = 255 for eBGP
neighbor xx.xx.xx.xx update source loopbackY                            /Make the loopback interface for peer source address


https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/22166-bgp-trouble-main
show ip bgp neighbor | include (neighbor is)|(state =)                  /Check ALL BGP ports and states
show ip bgp neighbor xx.xx.xx.xx | i (Interface associated.*)           /Check if the neighbor is connected or not
