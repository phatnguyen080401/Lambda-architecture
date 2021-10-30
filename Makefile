start-cluster:
	docker-compose -f ./setup/docker-compose.yml up

shutdown-cluster:
	docker-compose -f ./setup/docker-compose.yml down	

reset-volume-cluster:
	rm -r ./setup/docker/volumes/cassandra_seed/*
	rm -r ./setup/docker/volumes/cassandra_node/*
	rm -r ./setup/docker/volumes/kafka-1/*
	rm -r ./setup/docker/volumes/zookeeper/*

setup-env:
	cd ./lambda-architecture && \
	pipenv install -r requirements.txt

run:
	cd ./lambda-architecture && \
	pipenv run python3 main.py