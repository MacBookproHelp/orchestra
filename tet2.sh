#!/bin/sh
if sudo docker ps -a | grep -q 'cassandra'; then
	sudo docker start node2
else
	sudo docker run --name node2 -it -d -e CASSANDRA_BROADCAST_ADDRESS="$(sudo ifdata -pa wlp1s0)" -p 7000:7000 -e CASSANDRA_SEEDS="$(sudo cat '/home/teja/PycharmProjects/new/ip_of_controller')" cassandra:2 
fi
