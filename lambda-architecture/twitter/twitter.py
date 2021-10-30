from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

from config import config
from logger import Logger

CONSUMER_KEY        = config['TWITTER']['CONSUMER_KEY']
CONSUMER_SECRET     = config['TWITTER']['CONSUMER_SECRET']
ACCESS_TOKEN        = config['TWITTER']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['TWITTER']['ACCESS_TOKEN_SECRET']

logger = Logger('Twitter-API')

class TwitterAuth:
  def authenticate(self):
    try:
      auth = OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
      auth.set_access_token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)

      logger.info("Authenticate Twitter App")
    except Exception as e:
      logger.error(e)

    return auth

class TwitterStreamer:
  def __init__(self, producer, topic):
      self._twitterAuth = TwitterAuth()
      self._producer = producer
      self._topic = topic

  def stream_tweets(self):
    keyword = ["Bitcoin",  "Ehereum", "Keycaps"]
    
    while True:
      try:
        listener = ListenerTS(self._producer, self._topic) 
        auth = self._twitterAuth.authenticate()
        stream = Stream(auth, listener)
        stream.filter(track=keyword, languages= ["en"])

        logger.info("Streaming Tweets")
      except Exception as e:
        logger.error(e)

class ListenerTS(StreamListener):
  def __init__(self, producer, topic):
    self._producer = producer
    self._topic = topic

  def on_data(self, raw_data):
    try:
      # data_json = json.loads(raw_data)
      # tweet = data_json['text'].encode('utf-8')
      self._producer.send(self._topic, str.encode(raw_data))

      logger.info(f"Tweet: {raw_data}")
    except Exception as e:
      logger.error(e)

    return True
