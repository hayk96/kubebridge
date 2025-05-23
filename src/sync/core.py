from .kubernetes_sd import kubernetes_service_discovery
from src.utils.redis_client import RedisClient
from src.utils.log import logger
import time
import os


def service_sync():
    redis = RedisClient()
    while not redis.ping_redis():
        logger.warning("Redis not available. Retrying in 5 seconds...")
        time.sleep(5)

    while True:
        kubernetes_services = kubernetes_service_discovery()
        redis.publisher(str(kubernetes_services))
        time.sleep(int(os.environ.get("K8S_SERVICE_SYNC_INTERVAL", 3)))


def allow_sync(service_namespace: str, service_annotations: dict) -> bool:
    """
    Checks if the service is allowed to be synced
    """
    allowed_namespaces = os.environ.get("ALLOW_NAMESPACES", ["*"])
    denied_namespaces = os.environ.get("DENY_NAMESPACES", [])
    service_sync_annotation = "kubebridge.io/service-sync"

    allow_ns: bool = (service_namespace in allowed_namespaces or "*" in allowed_namespaces) and \
        service_namespace not in denied_namespaces
    force_allow_service: bool = service_annotations.get(
        service_sync_annotation) == "true"
    disallow_service: bool = service_annotations.get(
        service_sync_annotation) == "false"

    if force_allow_service:
        return True
    elif disallow_service:
        return False
    elif allow_ns:
        return True
    elif not allow_ns:
        return False
