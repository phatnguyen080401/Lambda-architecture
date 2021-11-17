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

kafka-produce:
	cd ./lambda-architecture && \
	pipenv run python producer.py

streaming-layer:
	cd ./lambda-architecture && \
	pipenv run python streaming.py

batch-layer:
	cd ./lambda-architecture && \
	pipenv run python batch.py

speed-layer:
	cd ./lambda-architecture && \
	pipenv run python speed.py