# Final Controller B
# Ports used 5678, 5243
import logging
import socket
from socket import *
import zmq
import threading
import cassandra
from cassandra.cluster import Cluster
import subprocess
from subprocess import Popen
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import os
import orc_to_wired
import switch_to_orc
import Ap_to_orc
import client_to_orc
import re
from threading import Thread
import orc_to_wireless
import json
from queue import Queue
from socket import *


# Get bd address from host machine
# Change the re.search according to your machine
def get_bd_address(ether_adapter):
    ip_data = os.popen("ifconfig " + ether_adapter)
    for line in ip_data:
        match2 = re.search(r'broadcast\s+(\d+.\d+.\d+.\d+)', line)
        if match2:
            bcast = match2.group(1)
            return bcast


# Get ip address from host machine
# Change the re.search according to the machine
def get_ip_data(ether_adapter):
    ip_data = os.popen("ifconfig " + ether_adapter)
    for line in ip_data:
        match2 = re.search(r'inet\s+(\d+.\d+.\d+.\d+)', line)
        if match2:
            ip_ = match2.group(1)

            return ip_


# Send Broadcast
def bd_send(Host, port):
    sock = socket(AF_INET, SOCK_DGRAM)
    msg = 'hello'
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    sock.sendto(msg.encode(), (Host, port))


# Receive Broadcast
def bd_recv(Host, port, q19):
    sock = socket(AF_INET, SOCK_DGRAM)
    address = Host, port
    sock.bind(address)
    msg, client = sock.recvfrom(4089)
    a = msg.decode()
    b = client[0]
    q19.put(b)


# Receive Broadcast
def bd_recv(Host, port, q16):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = Host, port
    sock.bind(address)
    msg, client = sock.recvfrom(4089)
    a = msg.decode()
    b = client[0]
    q16.put(b)


def bd_recv_wireless(Host, port, q):
    sock = socket(AF_INET, SOCK_DGRAM)
    address = Host, port
    sock.bind(address)
    msg, client = sock.recvfrom(1024)
    a = msg.decode()
    b = client[0]
    q = q.put(b)


def bd_recv_VMAC(Host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = Host, port
    sock.bind(address)
    msg, client = sock.recvfrom(1024)
    a = msg.decode()
    b = client[0]
    return b


def bd_recv_AP(Host, port, q14):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = Host, port
    sock.bind(address)
    msg, client = sock.recvfrom(1024)
    a = msg.decode()
    b = client[0]
    q14.put(b)


def bd_recv_Switch(Host, port, q7):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = Host, port
    sock.bind(address)
    msg, client = sock.recvfrom(1024)
    a = msg.decode()
    b = client[0]
    q7.put(b)


def bd_recv_wired(Host, port, q3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = Host, port
    sock.bind(address)
    msg, client = sock.recvfrom(1024)
    a = msg.decode()
    b = client[0]
    q3 = q3.put(b)


def subscriber_wireless(host, port, q2):
    context = zmq.Context()
    sub = context.socket(zmq.SUB)  # Note.
    sub.setsockopt_string(zmq.SUBSCRIBE, 'wireless:')  # Note.
    # host='192.168.1.46'
    # port=5677
    sub.connect("tcp://" "%s:%d" % ((host), port))
    for i in range(1):
        b = ('Received: %s' % sub.recv_string())
        q2 = q2.put(b)
        # print(type(('Received: %s' % sub.recv_string())))


def insert_wireless(recv_string):
    cluster = Cluster(contact_points=['172.17.0.2'])
    session = cluster.connect()
    id = 1
    session.execute("""INSERT INTO testspace.wireless_sdn(PacketID, PacketValue)
    VALUES(%s,%s)""", (id, recv_string))
    print("inserted wireless sdn data")


def insert_wired(recv_string1):
    cluster = Cluster(contact_points=['172.17.0.2'])
    session = cluster.connect()
    id = 1
    session.execute("""INSERT INTO testspace.wired_sdn(PacketID, PacketValue)
    VALUES(%s,%s)""", (id, recv_string1))
    print("inserted wired sdn data")


def insert_VMAC(recv_string):
    cluster = Cluster(contact_points=['172.17.0.2'])
    session = cluster.connect()
    id = 1
    session.execute("""INSERT INTO testspace.VMAC(PacketID, PacketValue)
    VALUES(%s,%s)""", (id, recv_string))
    print("inserted VMAC data")


def insert_AP(recv_string):
    cluster = Cluster(contact_points=['172.17.0.2'])
    session = cluster.connect()
    id = 1
    session.execute("""INSERT INTO testspace.AP(PacketID, PacketValue)
    VALUES(%s,%s)""", (id, recv_string))


def insert_Switch(recv_string):
    cluster = Cluster(contact_points=['172.17.0.2'])
    session = cluster.connect()
    id = 1
    session.execute("""INSERT INTO testspace.Switch(PacketID, PacketValue)
    VALUES(%s,%s)""", (id, recv_string))


def send_req_wireless(host, port):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://" "%s:%d" % ((host), port))
    print("sending req to wireless sdn")
    sw = orc_to_wireless.orc_to_wireless()
    a = sw.get()
    # this default should return a serializable version of obj or raise TypeError
    packet = (json.dumps(a, default=lambda x: x.__dict_))
    print(packet)
    # print(type(packet))
    socket.send_json(packet)
    msg = socket.recv(1024)
    print("received reply: %s" % msg)


# join cluster
def join_cluster():
    subprocess.call(["/home/teja/PycharmProjects/new/tet2.sh"])


# Send Req
def send_Req(Host, port):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://" "%s:%d" % ((Host), port))
    print("sending req to the controller A")
    socket.send_string("Can i join the cluster?")
    msg = socket.recv(1024)
    print("Received reply: %s" % msg)


def subscriber_wired(Host1, port, q4):
    context = zmq.Context()
    sub = context.socket(zmq.SUB)  # Note.
    sub.setsockopt_string(zmq.SUBSCRIBE, 'wired:')  # Note.
    # host='192.168.1.46'
    # port=5677
    sub.connect("tcp://" "%s:%d" % ((Host1), port))
    for i in range(1):
        ar = ('Received: %s' % sub.recv_string())
        q4 = q4.put(ar)
        # print(type(('Received: %s' % sub.recv_string())))


def send_req_wired(host, port):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://" "%s:%d" % ((host), port))
    print("sending req to wired_sdn")
    sw = orc_to_wired.orc_to_wired()
    a = sw.get()
    # this default should return a serializable version of obj or raise TypeError
    packet = (json.dumps(a, default=lambda x: x.__dict_))
    print(packet)
    # print(type(packet))
    socket.send_json(packet)
    msg = socket.recv(1024)
    print("received reply: %s" % msg)


def insert_wired(recv_string1):
    cluster = Cluster(contact_points=['172.17.0.2'])
    session = cluster.connect()
    id = 1
    session.execute("""INSERT INTO testspace.wired_sdn(PacketID, PacketValue)
    VALUES(%s,%s)""", (id, recv_string1))
    print("inserted wired sdn data")


def listen_Switch(Host, port, q6):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((Host, port))
    while 1:
        msgg, client = sock.recvfrom(1024)
        msg = msgg.decode("utf-8")
        print('connected with switch : ' + client[0] + ':' + str(client[1]))
        q6.put(msg)
        t = threading.Thread(target=insert_Switch, args=(msg,))
        t.start()
        print('inserted data to switch')
    sock.close()


def listen_Ap(Host, port, q6):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((Host, port))
    while 1:
        msgg, client = sock.recvfrom(1024)
        msg = msgg.decode("utf-8")
        print('connected with switch : ' + client[0] + ':' + str(client[1]))
        q6.put(msg)
        t = threading.Thread(target=insert_AP, args=(msg,))
        t.start()
        print('inserted data to AP')
    sock.close()


def talkToClient(ip):
    logging.info("sending 'clients we received your data' to %s", ip)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto("ok".encode('utf-8'), ip)


def listen_clients(Host, port, q15):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((Host, port))
    while True:
        msgg, client = sock.recvfrom(1024)
        msg = msgg.decode("utf-8")
        q15.put(msg)
        print('connected with : ' + client[0] + ':' + str(client[1]))

        t = threading.Thread(target=talkToClient, args=(client,))
        t.start()


if __name__ == "__main__":
    ethernet_card = "wlp1s0"
    bd_of_the_machine = get_bd_address(ethernet_card)
    ip_of_the_machine = get_ip_data(ethernet_card)
    t1 = threading.Thread(target=bd_send, name="Broadcast_send", args=(bd_of_the_machine, 5432))
    t1.start()

    q19 = Queue()
    t2 = threading.Thread(target=bd_recv, name='recv_bd', args=(bd_of_the_machine, 5678, q19))
    t2.start()
    h = q19.get()
    file = open('/home/teja/PycharmProjects/new/ip_of_controller', "w")
    file.write(h)
    file.close()
    t3 = threading.Thread(target=send_Req, name='req', args=(h, 5367))
    t4 = threading.Thread(target=join_cluster, name="join_cluster")
    t3.start()
    t4.start()

    # wireless
    q = Queue()
    t45 = threading.Thread(target=bd_recv_wireless, args=(bd_of_the_machine, 5694, q))
    t45.start()
    Host = (q.get())
    q2 = Queue()
    t5 = threading.Thread(target=subscriber_wireless, name="Receive_publisher_msgs", args=(Host, 6782, q2))
    t5.start()
    recv_string = (q2.get())
    t7 = threading.Thread(target=insert_wireless, name="insert", args=(recv_string,))
    t7.start()

    t11 = threading.Thread(target=send_req_wireless, name="send_req", args=(Host, 9843))
    t11.start()

    # wired
    q3 = Queue()
    t8 = threading.Thread(target=bd_recv_wired, args=(bd_of_the_machine, 3727, q3))
    t8.start()
    Host1 = (q3.get())
    q4 = Queue()
    t9 = threading.Thread(target=subscriber_wired, name="Receive_publisher_msgs", args=(Host1, 6564, q4))
    t9.start()
    recv_string1 = (q4.get())
    t10 = threading.Thread(target=insert_wired, name="insert_wired", args=(recv_string1,))
    t10.start()

    t12 = threading.Thread(target=send_req_wired, name="send_req", args=(Host, 9723))
    t12.start()

    # Switch
    q7 = Queue()
    t13 = threading.Thread(target=bd_recv_Switch, args=(bd_of_the_machine, 6798, q7))
    t13.start()
    Host2 = (q7.get())

    q6 = Queue()
    t14 = threading.Thread(target=listen_Switch, args=(ip_of_the_machine, 4292, q6))
    t14.start()
    recv_string2 = (q6.get())
    t15 = threading.Thread(target=insert_Switch, name="insert_Switch", args=(recv_string2,))
    t15.start()

    # AP
    q14 = Queue()
    t13 = threading.Thread(target=bd_recv_AP, args=(bd_of_the_machine, 8573, q14))
    t13.start()
    Host2 = (q14.get())

    q15 = Queue()
    t14 = threading.Thread(target=listen_Ap, args=(ip_of_the_machine, 4331, q15))
    t14.start()
    recv_string6 = (q15.get())
    t15 = threading.Thread(target=insert_AP, name="insert_Ap", args=(recv_string6,))
    t15.start()

    q10 = Queue()
    t17 = threading.Thread(target=listen_clients, args=(ip_of_the_machine, 4221, q10))
    t17.start()
    recv_string3 = (q10.get())
    t18 = threading.Thread(target=insert_VMAC, args=(recv_string3,))
    t18.start()








