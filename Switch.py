#Switch_to_orc
from queue import Queue
import socket
import threading
import client_to_orc
import json
import pyangbind.lib.pybindJSON as pybindJSON
import switch_to_orc
import socket
from socket import *
#Send Broadcast
import re
import os

def get_ip_data(ether_adapter):
    ip_data = os.popen("ifconfig " + ether_adapter)
    for line in ip_data:
        match2 = re.search(r'inet\s+(\d+.\d+.\d+.\d+)', line)
        if match2:
            ip_ = match2.group(1)

            return ip_

def get_bd_address(ether_adapter):
    ip_data = os.popen("ifconfig " + ether_adapter)
    for line in ip_data:
        match2 = re.search(r'broadcast\s+(\d+.\d+.\d+.\d+)', line)
        if match2:
            bcast = match2.group(1)
            return bcast
def bd_send(Host,port):
    sock=socket(AF_INET,SOCK_DGRAM)
    msg='hello'
    sock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
    sock.sendto(msg.encode(),(Host,port))

def con_server(server_host,server_port):
    server_address=(server_host,server_port)
    sock=socket(AF_INET,SOCK_DGRAM)
    sw=switch_to_orc.switch_to_orc()
    ob=sw.switchmac.flows.flow.add("8965")
    ob.ip_src="192.168.1.2"
    ob.ip_dst='192.168.1.45'
    ob.throughput="2.45"
    packet=(pybindJSON.dumps(sw))
    sock.sendto(packet.encode("Utf-8"),server_address)
    data, server=sock.recv(4096)
    print('Client:' +data)

if __name__=="__main__":
    ethernet_card = "wlp1s0"
    bd_of_the_machine = get_bd_address(ethernet_card)
    ip_of_the_machine = get_ip_data(ethernet_card)
    t4 = threading.Thread(target=bd_send, name="Broadcast_send", args=(bd_of_the_machine, 6798))
    t4.start()
    q=Queue()
    t2=threading.Thread(target=con_server,name="Switch",args=("192.168.1.27",4292,))
    t2.start()