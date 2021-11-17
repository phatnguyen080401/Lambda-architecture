# Lambda-architecture

## Setup
For the ease of deployment Docker Compose script is used. It still needs some manual steps, however.

* Docker
  * Edit `docker-compose.yml` file and replace paths in `volumes` to match your environment
  * To start all the services run this command from the main project folder: docker-compose up
* Cassandra  
  * In another terminal, connect to Cassandra instance with command like: `docker exec -it cassandra-seed bash`
  * Once inside, initialise Cassandra's keyspace: `cqlsh -f init/init.sql`
  * You can also run `cqlsh` and start issuing CQL statements directly against Cassandra

## Usage

1. Clone repository

```
  git clone 
```

2. Run Docker containers

```
  make start-docker
```

3. Setup virtual env for project

```
  make setup-env
```

4. Run project (Must run in order)

```
  1. make kafka-produce
  2. make streaming-layer
  3. make speed-layer
  4. make batch-layer
```
5. Analyze

```
  Go to notebook for analyzing
```