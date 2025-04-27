from ast import literal_eval
from .log import logger
import redis
import time
import os


class RedisClient:
    """
    Redis client for publishing and subscribing messages
    """
    msg: dict = {}
    read_msg_counter: int = -1

    def __init__(self):
        self.redis_host = os.environ.get("REDIS_HOST", "127.0.0.1")
        self.redis_port = os.environ.get("REDIS_PORT", 6379)
        self.redis_db = os.environ.get("REDIS_DB", 0)
        self.redis_username = os.environ.get("REDIS_USERNAME")
        self.redis_password = os.environ.get("REDIS_PASSWORD")
        self.redis_pubsub_channel = "KubeBridge:KubernetesServices"

        self.client = redis.Redis(
            host=self.redis_host,
            port=int(self.redis_port),
            db=int(self.redis_db),
            username=self.redis_username,
            password=self.redis_password,
            decode_responses=True)

    def ping_redis(self,
                   msg="Successfully connected to Redis server",
                   ext_msg: dict = None) -> bool:
        """
        Pings to Redis server to check if it is up
        """
        try:
            if self.client.ping():
                logger.debug(
                    f"{msg} {self.redis_host}:{self.redis_port}", extra=ext_msg)
                return True
        except BaseException as err:
            logger.error(err)
            return False

    def publisher(self, data: str):
        """
        Publish data to Redis channel
        """
        try:
            self.client.publish(self.redis_pubsub_channel, data)
        except BaseException as e:
            logger.error(f"Failed to publish data to Redis. {e}",
                         extra={"redis_channel": self.redis_pubsub_channel})
        else:
            logger.debug(f"Data published to Redis successfully", extra={
                         "redis_channel": self.redis_pubsub_channel, "data": data})

    def subscriber(self, func):
        """
        Subscribe data from Redis channel
        """
        pubsub = self.client.pubsub()
        pubsub.subscribe(self.redis_pubsub_channel)
        while True:
            try:
                message = pubsub.get_message(
                    ignore_subscribe_messages=True, timeout=int(
                        os.environ.get("K8S_SERVICE_SYNC_INTERVAL")) + 1)
                RedisClient.read_msg_counter += 1
                # Wait as the messages can be readable after subscription
                if RedisClient.read_msg_counter == 0:
                    time.sleep(
                        int(os.environ.get("K8S_SERVICE_SYNC_INTERVAL")) + 1)
                    continue
                if message:
                    RedisClient.msg = literal_eval(message.get("data"))
                else:
                    raise Exception("No messages found in Redis.")
            except BaseException as e:
                logger.error(
                    f"Redis subscription failed. {e} Retrying...", extra={
                        "redis_channel": self.redis_pubsub_channel})
                time.sleep(5)
                continue
            else:
                func(RedisClient.msg)
                logger.debug(
                    "Data received from Redis successfully",
                    extra={
                        "redis_channel": self.redis_pubsub_channel,
                        "data": RedisClient.msg})
