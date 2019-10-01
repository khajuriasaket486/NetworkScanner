#!/usr/bin/env python
import scapy.all as scapy
import sys
print('Python %s on %s' % (sys.version, sys.platform))
def scan(ip):
    arp_request = scapy.ARP()
    scapy.ls(arp_request)
    arp_request.pdst=ip
    scapy.ls(arp_request)
    print(arp_request.summary())


scan('192.168.1.0/24')