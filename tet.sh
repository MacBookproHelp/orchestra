

if sudo docker ps -a | grep -q 'cassandra';then
#	#sudo docker inspect --format="{{.Id}}" node1	
	sudo docker start node1
#elif sudo docker ps -a | grep -q 'node2';then
#	sudo docker start node2
#elif sudo docker ps -a | grep -q 'node3';then
#	sudo docker start node3
#elif sudo docker ps -a | grep -q 'node4';then
#	sudo docker start node4
else
#	#sudo ifdata -pa wlp3s0
	sudo docker run --name node1 -d -e CASSANDRA_BROADCAST_ADDRESS="$(sudo ifdata -pa wlp3s0)"  -p 7000:7000 cassandra:2
fi

#if sudo docker ps -a | grep -q 'node2';then
	#sudo docker inspect --format="{{.Id}}" node1	
#	sudo docker start node1
#elif sudo docker ps -a | grep -q 'node3';then
#	sudo docker start node2
#elif sudo docker ps -a | grep -q 'node4';then
#	sudo docker start node3
#else
#	sudo docker run --name node2 -d -e CASSANDRA_BROADCAST_ADDRESS=192.168.1.27 -p 7000:7000 -#e CASSANDRA_SEEDS=192.168.1.27 cassandra:2
#fi
