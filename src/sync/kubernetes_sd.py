from kubernetes import client, config
from src.utils.log import logger
from . import core
import sys
import os

allow_service_types = os.environ.get(
    "ALLOW_SERVICE_TYPES", [
        "ClusterIP", "NodePort", "LoadBalancer"])

try:
    if os.environ.get("DEPLOYMENT_ENV") == "local":
        config.load_kube_config(config_file="~/.kube/kind/local")
    else:
        config.incluster_config.load_incluster_config()
except BaseException as e:
    logger.error(e)
    sys.exit(1)


def kubernetes_service_discovery() -> dict:
    """
    Retrieves services from Kubernetes API
    """
    services = {}
    v1 = client.CoreV1Api()
    try:
        ret = v1.list_service_for_all_namespaces(watch=False)
    except BaseException as e:
        logger.error("Failed to list Kubernetes namespaces.", e)
    else:
        for i in ret.items:
            svc_name: str = i.metadata.name
            scv_namespace = list()
            scv_namespace.append(i.metadata.namespace)
            svc_annotations = i.metadata.annotations or dict()
            svc_type: str = i.spec.type
            svc_cluster_ips: list = i.spec.cluster_i_ps
            if core.allow_sync(
                    service_namespace=i.metadata.namespace,
                    service_annotations=svc_annotations) and svc_type in allow_service_types and (
                    "None" not in svc_cluster_ips):
                if svc_name not in services:
                    services[svc_name] = {
                        "type": svc_type,
                        "cluster_ips": svc_cluster_ips,
                        "namespaces": scv_namespace
                    }
                else:
                    services[svc_name]["cluster_ips"].extend(svc_cluster_ips)
                    services[svc_name]["namespaces"].extend(scv_namespace)
        logger.debug("Kubernetes services fetched successfully")
        return services
