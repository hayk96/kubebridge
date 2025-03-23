# KubeBridge
Discover, Bridge, and Resolve Services in Kubernetes

# Components
* **Sync** - Syncs and maps Kubernetes services with DNS records real-time.
* **DNS** - Resolves service names to Kubernetes service IP addresses.
* **Redis** - A Pub/Sub messaging system for K8s service discovery used by Sync and DNS apps.

# Features
KubeBridge's DNS feature in Kubernetes provides service discovery by resolving service names to Kubernetes service IP addresses within a cluster. Key features:

* **Service Discovery:** Automatically registers Kubernetes services and makes them resolvable via DNS.

* **DNS Resolution:** Services can be queried using *.kube.bridge domain (e.g., my-service.kube.bridge) without specifying namespace.

* **Custom DNS Configuration:** Supports overriding Kubernetes DNS settings for advanced use cases.

# Installation
KubeBridge can be installed using Helm. The following steps will guide you through the installation process.
```shell
helm install kubebridge helm/charts
```

# Configuration
## Sync service
#### Service discovery by namespace
```yaml
sync:
  allowNamespaces: ["*"]
  denyNamespaces: ['kube-system', 'kube-public']
```

#### Service discovery by service type
```yaml
  allowServiceTypes:
    - NodePort
    - ClusterIP
    - LoadBalancer
```

#### Service discovery by service annotations
If this is set to `true` in service annotations, then the Kubernetes service is explicitly configured to be synced to KubeBridge. (The value `false` will disable the service sync.)
```yaml
annotations:
  kubebridge.io/service-sync: "true"
```

## DNS service
#### Search domain
Service names can be resolved using the *.kube.bridge domain.
```yaml
dns:
  domain: kube.bridge
```
#### Custom DNS configuration
Custom DNS configuration can be set to map service names to IP addresses.
```yaml 
dns:
  extraDNSConfig: |
    {
      "A": {
        "kubebridge.io.": [
          "127.0.0.1"
        ]
      },
      "CNAME": {
        "kube-bridge.io": "kubebridge.io."
      }
    }
```