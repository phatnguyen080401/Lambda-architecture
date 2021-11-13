start-docker:
	docker-compose -f ./setup/docker-compose.yml up

shutdown-docker:
	docker-compose -f ./setup/docker-compose.yml down	

reset-volume-docker:
	rm -r ./setup/docker/volumes/cassandra_seed/*
	rm -r ./setup/docker/volumes/cassandra_node/*
	rm -r ./setup/docker/volumes/kafka-1/*
	rm -r ./setup/docker/volumes/zookeeper/*

setup-env:
	cd ./lambda-architecture && \
	pipenv install -r requirements.txt

run:
	cd ./lambda-architecture && \
	pipenv run python main.py

kafka-produce:
	cd ./lambda-architecture && \
	pipenv run python -B /kafkaProducer/producer.py