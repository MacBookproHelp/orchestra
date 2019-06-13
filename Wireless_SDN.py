#writing script for publisher wireless
import pyangbind
import zmq
import socket
from socket import *
import time
import threading
import json
import wirel_to_orc
import jsonpickle
from threading import Thread
import os
import re
import wirel_to_orc
import pyangbind.lib.pybindJSON as pybindJSON

sw= wirel_to_orc.wirel_to_orc()

ob= sw.ControllerMac.clients.add("01:23:45:67:89:ab")
ob.ip="192.168.1.1"
ob.throughput="3.1"
ob.Signal="3.14"

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

#Send Broadcast
def bd_send(Host,port):
    sock=socket(AF_INET,SOCK_DGRAM)
    msg='hello'
    sock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
    sock.sendto(msg.encode(),(Host,port))

#This is for publishing to the controller
def publish():
    sw=wirel_to_orc.wirel_to_orc()
    ob= sw.ControllerMac.clients.add("01:23:45:67:89:ab")
    ob.ip="192.168.1.27"
    ob.throughput="1.1"
    ob.Signal="1.4"
    a=sw.get()

    packet = (pybindJSON.dumps(sw))
    context=zmq.Context()
    socket=context.socket(zmq.PUB)
    socket.bind("tcp://*:6782")
    for data in range(2):
        socket.send_string('wireless: %s' % packet,encoding="Utf-8")
        time.sleep(1)
    socket.close()
def rep(host,port):
    context=zmq.Context()
    socket=context.socket(zmq.REP)
    socket.bind('tcp://' '%s:%d' %(host,port))
    message=socket.recv_json(1024)
    print(message)

if __name__=="__main__":
    ethernet_card = "wlp1s0"
    bd_of_the_machine = get_bd_address(ethernet_card)
    ip_of_the_machine = get_ip_data(ethernet_card)

    t1 = threading.Thread(target=bd_send, name="Broadcast_send", args=(bd_of_the_machine, 5694))
    t1.start()
    threads=threading.Thread(target=publish)
    threads.start()
    t2=threading.Thread(target=rep,args=(ip_of_the_machine,9843))
    t2.start()