#!/usr/bin/env python
import scapy.all as scapy
def scan(ip):
    arp_request = scapy.ARP()
    scapy.ls(arp_request)   # or arp_request.show()
    arp_request.pdst = ip
#   scapy.ls(arp_request)
#   print(arp_request.summary())   # prints ARP who is pdst says psrc

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#   scapy.ls(broadcast)
#   print(broadcast.summary())

    arp_request_broadcast = broadcast/arp_request
#   print(arp_request_broadcast.summary())
#   arp_request_broadcast.show()

    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered.summary())
    print(unanswered.summary())
scan('192.168.1.1/24')