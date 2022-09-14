start-docker:
	docker-compose -f ./setup/docker-compose.yml up -d

shutdown-docker:
	docker-compose -f ./setup/docker-compose.yml down	

reset-volume-docker:
	sudo rm -rf ./setup/docker/volumes/cassandra-seed/*
	sudo rm -rf ./setup/docker/volumes/cassandra-node/*
	sudo rm -rf ./setup/docker/volumes/kafka/*
	sudo rm -rf ./setup/docker/volumes/zookeeper/*

setup-env:
	bash scripts/setup-env.sh

start-all:
	bash scripts/start-all.sh