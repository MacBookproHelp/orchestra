Scalable controller implementation for heterogenous wireless network management

CONTROLLER IMPLEMENTATION 
------------------------------------------------------------------------------------------------------------------------------------------
REQUIREMENTS:
Pycharm
Docker  -> pip install docker
python3 
Cassandra -> pip install cassandra
pyangbind -> sudo -h pip install pyang
ZMQ -> pip install zmq
yang model
yang python files

------------------------------------------------------------------------------------------------------------------------------------------
USAGE:

CONTROLLER_A:
Starts the database and we can start connecting to other devices starting with Controller_B,
Wireless_SDN, Wired_SDN, Switch, AP and VMACs.

CONTROLLER_B:
Joins the cluster and able to communicate with other devices as well.

------------------------------------------------------------------------------------------------------------------------------------------
Linux machine

------------------------------------------------------------------------------------------------------------------------------------------

Yang py folder contains all necessary python files for sending the packets. 

Tet.sh -> Database script for Controller A

Tet2.sh -> Database script for Controller B

