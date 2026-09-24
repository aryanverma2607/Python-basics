'''
iMPORTANT PROPERTIES
ip.version
ip.is_private
ip.is_global
ip.is_loopback
ip.is_multicast
ip.is_unspecified'''

import ipaddress

netwok=ipaddress.ip_address("192.168.1.10")
print(netwok)
netwok = ipaddress.ip_address("192.168.1.10")
print(netwok)
print(list(ipaddress.hosts()))

print(type(netwok))

a=netwok.version
print(a)

x=netwok.is_private
print(x)

i=ipaddress.ip_network("192.168.1.0/24")
print(i)
print(list(ipaddress.hosts()))
print(list(ipaddress.hosts()))
'''

ipaddress
│
├── ip_address()
│
├── ip_network()
│
├── ip_interface()
│
├── IP properties
│   ├── version
│   ├── is_private
│   ├── is_global
│   ├── is_loopback
│   └── ...
│
└── Network properties
    ├── network_address
    ├── broadcast_address
    ├── netmask
    ├── prefixlen
    ├── num_addresses
    └── hosts()'''