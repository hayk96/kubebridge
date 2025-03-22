from src.utils.redis_client import RedisClient
from . import dns_server as dns
import threading
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


def dns_srv():
    redis = RedisClient()
    if redis.ping_redis():
        dns_server = dns.DNSServer(port=53)
        subscriber_thread = threading.Thread(
            target=lambda: redis.subscriber(
                lambda x: domain_registrator(
                    dns_server, x)))
        subscriber_thread.start()
        dns_server.serve()
