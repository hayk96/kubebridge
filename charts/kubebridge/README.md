# KubeBridge Helm Chart Parameters Reference

This document provides a reference for the configurable values in the `values.yaml` file of the KubeBridge Helm chart.

## Parameters
### Global parameters

| Name                      | Type   | Value               | Description                                                                        |
|---------------------------|--------|---------------------|------------------------------------------------------------------------------------|
| `global.logLevel`         | string | `info`              | The log level for all KubeBridge components.                                       |
| `global.nameOverride`     | string | `""`                | Partially override common.names.fullname template (will maintain the release name) |
| `global.fullnameOverride` | string | `""`                | Fully override common.names.fullname template.                                     |
| `global.image.repository` | string | `hayk96/kubebridge` | The Docker image repository.                                                       |
| `global.image.tag`        | string | `v0.1.0`     | The Docker image tag.                                                              |

### Sync parameters

| Name                                              | Type   | Value                                       | Description                                                     |
|---------------------------------------------------|--------|---------------------------------------------|-----------------------------------------------------------------|
| `sync.replicaCount`                               | int    | `1`                                         | Number of replicas for the Sync component.                      |
| `sync.imagePullPolicy`                            | string | `IfNotPresent`                              | Image pull policy for the Sync component.                       |
| `sync.imagePullSecrets`                           | list   | `[]`                                        | Secrets for pulling Docker images.                              |
| `sync.k8sServiceSyncIntervalSeconds`              | int    | `3`                                         | Interval in seconds for syncing (fetching) Kubernetes services. |
| `sync.allowNamespaces`                            | list   | `["*"]`                                     | List of namespaces allowed for syncing.                         |
| `sync.denyNamespaces`                             | list   | `["kube-system", "kube-public"]`            | List of namespaces denied for syncing.                          |
| `sync.allowServiceTypes`                          | list   | `["NodePort", "ClusterIP", "LoadBalancer"]` | Allowed Kubernetes service types for syncing.                   |
| `sync.rbac.create`                                | bool   | `true`                                      | Whether to create RBAC resources for Sync component.            |
| `sync.serviceAccount.create`                      | bool   | `true`                                      | Whether to create a service account.                            |
| `sync.serviceAccount.annotations`                 | object | `{}`                                        | Annotations for the service account.                            |
| `sync.serviceAccount.name`                        | string | `""`                                        | Name of the service account.                                    |
| `sync.podAnnotations`                             | object | `{}`                                        | Annotations for the Sync pods.                                  |
| `sync.podSecurityContext`                         | object | `{}`                                        | Security context for the Sync pods.                             |
| `sync.securityContext`                            | object | `{}`                                        | Security context for the Sync containers.                       |
| `sync.resources`                                  | object | `{}`                                        | Resource requests and limits for the Sync pods.                 |
| `sync.livenessProbe`                              | object | See `values.yaml`                           | Liveness probe configuration for the Sync pods.                 |
| `sync.readinessProbe`                             | object | See `values.yaml`                           | Readiness probe configuration for the Sync pods.                |
| `sync.autoscaling.enabled`                        | bool   | `false`                                     | Whether to enable autoscaling for the Sync component.           |
| `sync.autoscaling.minReplicas`                    | int    | `1`                                         | Minimum number of replicas for autoscaling.                     |
| `sync.autoscaling.maxReplicas`                    | int    | `20`                                        | Maximum number of replicas for autoscaling.                     |
| `sync.autoscaling.targetCPUUtilizationPercentage` | int    | `80`                                        | Target CPU utilization percentage for autoscaling.              |
| `sync.nodeSelector`                               | object | `{}`                                        | Node selector for scheduling Sync pods.                         |
| `sync.tolerations`                                | list   | `[]`                                        | Tolerations for scheduling Sync pods.                           |
| `sync.affinity`                                   | object | `{}`                                        | Affinity rules for scheduling Sync pods.                        |

### DNS parameters

| Name                                             | Type   | Value             | Description                                          |
|--------------------------------------------------|--------|-------------------|------------------------------------------------------|
| `dns.domain`                                     | string | `kube.bridge`     | Domain name for the DNS component.                   |
| `dns.replicaCount`                               | int    | `1`               | Number of replicas for the DNS component.            |
| `dns.imagePullPolicy`                            | string | `IfNotPresent`    | Image pull policy for the DNS component.             |
| `dns.imagePullSecrets`                           | list   | `[]`              | Secrets for pulling images.                          |
| `dns.extraDNSConfig`                             | string | See `values.yaml` | Additional DNS configuration.                        |
| `dns.service.type`                               | string | `ClusterIP`       | Kubernetes service type for the dns component.       |
| `dns.serviceAccount.create`                      | bool   | `true`            | Whether to create a service account.                 |
| `dns.serviceAccount.annotations`                 | object | `{}`              | Annotations for the service account.                 |
| `dns.serviceAccount.name`                        | string | `""`              | Name of the service account.                         |
| `dns.podAnnotations`                             | object | `{}`              | Annotations for the DNS pods.                        |
| `dns.podSecurityContext`                         | object | `{}`              | Security context for the DNS pods.                   |
| `dns.securityContext`                            | object | `{}`              | Security context for the DNS containers.             |
| `dns.resources`                                  | object | `{}`              | Resource requests and limits for the DNS pods.       |
| `dns.livenessProbe`                              | object | See `values.yaml` | Liveness probe configuration for the DNS pods.       |
| `dns.readinessProbe`                             | object | See `values.yaml` | Readiness probe configuration for the DNS pods.      |
| `dns.autoscaling.enabled`                        | bool   | `false`           | Whether to enable autoscaling for the DNS component. |
| `dns.autoscaling.minReplicas`                    | int    | `1`               | Minimum number of replicas for autoscaling.          |
| `dns.autoscaling.maxReplicas`                    | int    | `20`              | Maximum number of replicas for autoscaling.          |
| `dns.autoscaling.targetCPUUtilizationPercentage` | int    | `80`              | Target CPU utilization percentage for autoscaling.   |
| `dns.nodeSelector`                               | object | `{}`              | Node selector for scheduling DNS pods.               |
| `dns.tolerations`                                | list   | `[]`              | KubeBridge sync tolerations for pod assignment.      |
| `dns.affinity`                                   | object | `{}`              | KubeBridge sync affinity for pod assignment.         |

### Redis parameters

| Name                               | Type       | Value                            | Description                                                      |
|------------------------------------|------------|----------------------------------|------------------------------------------------------------------|
| `redis.enabled`                    | bool       | `true`                           | Whether to enable the Redis component.                           |
| `redis.master.podLabels`           | object     | `{app: redis}`                   | Labels for the Redis master pods.                                |
| `redis.master.persistence.enabled` | bool       | `false`                          | Whether to enable persistence for the Redis master.              |
| `redis.replica.replicaCount`       | int        | `0`                              | Number of replicas for the Redis replica.                        |
| `redis.auth.enabled`               | bool       | `true`                           | Whether to enable authentication for Redis.                      |
| `redis.auth.generatePassword`      | bool       | `true`                           | Whether to generate a password for Redis authentication.         |
| `redis.auth.existingSecret`        | string     | `redis-secret`                   | Name of the existing Kubernetes secret for Redis authentication. |