from src.utils.redis_client import RedisClient
from src.utils.log import logger
from . import dns_server as dns
import threading
import time
import os


def domain_registrator(dns_server: dns.DNSServer, data: dict) -> None:
    """
    Registers DNS records with "A" type
    """
    domain = os.environ.get("DOMAIN", "kube.bridge")
    dns_server.records = {
        'A': {
            f'{k}.{domain}.': v['cluster_ips'] for k, v in data.items()
        }
    }


def dns_srv() -> None:
    redis = RedisClient()
    while not redis.ping_redis():
        logger.warning("Redis not available. Retrying in 5 seconds...")
        time.sleep(5)
    dns_server = dns.DNSServer(port=53)
    subscriber_thread = threading.Thread(
        target=lambda: redis.subscriber(
            lambda x: domain_registrator(
                dns_server, x)))
    subscriber_thread.start()
    dns_server.serve()
