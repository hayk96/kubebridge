from ast import literal_eval
from .log import logger
import redis
import time
import os

redis_host = os.environ.get("REDIS_HOST") or "127.0.0.1"
redis_port = os.environ.get("REDIS_PORT") or 6379
redis_db = os.environ.get("REDIS_DB") or 0
redis_client = redis.Redis(
    host=redis_host,
    port=redis_port,
    db=redis_db,
    decode_responses=True)
redis_pubsub_channel = "kubebridge:kubernetes_services"
m = {}
read_messages_counter = -1


def ping_redis(
        msg="Redis is up. Ping has been succeeded to",
        ext_msg=None) -> bool:
    """This function pings to Redis server"""
    global redis_client
    try:
        if redis_client.ping():
            logger.info(
                f"{msg} {redis_host}:{redis_port}", extra=ext_msg)
            return True
    except BaseException as err:
        logger.error(err)
        return False


def publisher(data: str):
    """
    Publishes data to Redis
    """
    global redis_client, redis_pubsub_channel
    try:
        redis_client.publish(redis_pubsub_channel, data)
    except BaseException as e:
        logger.error(f"Failed to publish data to Redis. {e}",
                     extra={"channel": redis_pubsub_channel})
    else:
        logger.debug(f"Data published to Redis successfully: {data}",
                     extra={"channel": redis_pubsub_channel})


def subscriber(func):
    """
    Subscribe data from Redis
    """
    global m
    global read_messages_counter
    global redis_client
    pubsub = redis_client.pubsub()
    pubsub.subscribe(redis_pubsub_channel)
    while True:
        try:
            message = pubsub.get_message(
                ignore_subscribe_messages=True, timeout=int(
                    os.environ.get("K8S_SERVICE_SYNC_INTERVAL")) + 1)
            read_messages_counter += 1
            # Wait as the messages can be readable after subscription
            if read_messages_counter == 0:
                time.sleep(
                    int(os.environ.get("K8S_SERVICE_SYNC_INTERVAL")) + 1)
                continue
            if message:
                m = literal_eval(message.get("data"))
            else:
                raise Exception("No messages in Redis. Waiting...")
        except BaseException as e:
            logger.error(
                f"Failed to subscribe data from Redis. {e}. Reconnecting...", extra={
                    "channel": redis_pubsub_channel})
            time.sleep(5)
            continue
        else:
            func(m)
            logger.debug("Received data from Redis successfully",
                         extra={"channel": redis_pubsub_channel, "data": m})
