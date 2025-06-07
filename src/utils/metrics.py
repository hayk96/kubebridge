from prometheus_client import Gauge, Counter, disable_created_metrics

disable_created_metrics()

kubebridge_sync_services = Gauge("kubebridge_sync_services",
                                 "Total services discovered and synchronized by the KubeBridge Sync component",
                                 labelnames=["app_name", "namespace", "service_type", "service_name", "service_ip"])

kubebridge_sync_services_count = Gauge("kubebridge_sync_services_count",
                                       "Number of services synchronized by the KubeBridge Sync component",
                                       labelnames=["app_name"])

kubebridge_dns_requests = Counter("kubebridge_dns_requests",
                                  "Total count of DNS requests processed for domain records",
                                  labelnames=["app_name", "record_type", "record_name", "record_ip"])

kubebridge_dns_lookup_time_seconds = Gauge("kubebridge_dns_lookup_time_seconds",
                                           "Time taken to resolve DNS queries in seconds",
                                           labelnames=["app_name", "record_type", "record_name", "record_ip"])
