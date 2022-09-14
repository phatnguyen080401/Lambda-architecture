import sys
sys.path.append(".")

from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer
from twitter.twitter import TwitterStreamer

from config.config import config
from logger.logger import Logger

KAFKA_ENDPOINT = "{0}:{1}".format(config['KAFKA']['KAFKA_ENDPOINT'], config['KAFKA']['KAFKA_ENDPOINT_PORT'])
KAFKA_TOPIC    = config['KAFKA']['KAFKA_TOPIC']

logger = Logger("Kafka-Producer")

try:
  admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_ENDPOINT)

  topic = []
  topic.append(NewTopic(name=KAFKA_TOPIC, num_partitions=3, replication_factor=1))
  admin_client.create_topics(new_topics=topic, validate_only=False)

  logger.info(f"Create topic: {KAFKA_TOPIC}")
except Exception as e:
  logger.error(e)

class Producer:

  producer = KafkaProducer(bootstrap_servers=KAFKA_ENDPOINT, acks='all')

  @staticmethod
  def produce():
    TwitterStreamer(producer=Producer.producer, topic=KAFKA_TOPIC).stream_tweets()

if __name__ == '__main__':
  Producer.produce()