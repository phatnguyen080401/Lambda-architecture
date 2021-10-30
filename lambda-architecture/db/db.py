from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthenticator
from config import config
from logger import Logger

CLUSTER_NAME     = config['CASSANDRA']['CLUSTER_NAME']
CLUSTER_KEYSPACE = config['CASSANDRA']['CLUSTER_KEYSPACE']
CLUSTER_USERNAME = config['CASSANDRA']['CLUSTER_USERNAME']
CLUSTER_PASSWORD = config['CASSANDRA']['CLUSTER_PASSWORD']
CLUSTER_HOST     = config['CASSANDRA']['CLUSTER_HOST']
CLUSTER_PORT     = config['CASSANDRA']['CLUSTER_PORT']

auth_provider = PlainTextAuthenticator(username=CLUSTER_USERNAME, password=CLUSTER_PASSWORD)
contact_points = [CLUSTER_HOST]

logger = Logger('DB')

class DB:

  __instance = None

  @staticmethod
  def getDB():
    if DB.__instance == None:
      DB()
    return DB.__instance

  def __init__(self):
    if DB.__instance:
      raise Exception("This class is a singleton!")
    else:
      DB.__instance = self

    self._keyspace = None

    try:
      self._cluster = Cluster(contact_points, port=CLUSTER_HOST, auth_provider=auth_provider)
      logger.info(f"Setup cluster {CLUSTER_NAME}")
    except Exception as e:
      logger.error(e)

  def __connect__(self):
    try:
      self._session = self._cluster.connect()
      logger.info(f"Open session to '{CLUSTER_NAME}'")
    except Exception as e:
      logger.error(e)

  def __disconnect__(self):
    try:
      self._session.shutdown()
      logger.info(f"Close session to {CLUSTER_NAME}")
    except Exception as e:
      logger.error(e)

  def shutdown(self):
    self.__disconnect__()

    try:
      self._cluster.shutdown()
      logger.info(f"Shutdown connect to cluster {CLUSTER_NAME}")
    except Exception as e:
      logger.error(e)

  def create_keyspace(self, keyspace=CLUSTER_KEYSPACE):
    cql = "CREATE KEYSPACE IF NOT EXISTS % WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 }" % (keyspace)

    try:
      self.__connect__()
      self.execute(cql)
      logger.info(f"Create keyspace {keyspace}")

      self.set_keyspace(keyspace)
    except Exception as e:
      logger.error(e)

  def set_keyspace(self, keyspace):
    self._session.set_keyspace(keyspace)
    self._keyspace = keyspace

    logger.info(f"Using keyspace '{keyspace}'")

  def fetch(self, cql):
    rows = None

    try:
      rows = self._session.execute(cql)
      logger.info(f"Execute: '{cql}'")
    except Exception as e:
      logger.error(e)

    return rows

  def execute(self, cql, para=None):
    try:
      if para:
        self._session.execute(cql, para)
      else:
        self._session.execute(cql)

      logger.info(f"Execute: '{cql}'")
    except Exception as e:
      logger.error(e)