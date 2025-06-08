## [v0.2.1] - 2025-06-08
### Bug Fixes
- [`d726f81`](https://github.com/hayk96/kubebridge/commit/d726f81a599206265a9a147dcacf3f4fa21dd9ef) - **prometheus-metrics**: Fix metric type of DNS request latency *(PR [#4](https://github.com/hayk96/kubebridge/pull/4) by [@hayk96](https://github.com/hayk96))*
  - :arrow_lower_right: *fixes issue [#3](https://github.com/hayk96/kubebridge/issues/3) opened by [@hayk96](https://github.com/hayk96)*


## [v0.2.0] - 2025-06-07
### New Features
- [`9f46b2c`](https://github.com/hayk96/kubebridge/commit/9f46b2cad85307dd79e90e11d20b3f761db63eaa) - Add support exporting Prometheus metrics *(PR [#1](https://github.com/hayk96/kubebridge/pull/1) by [@hayk96](https://github.com/hayk96))*

### Chores
- [`076f596`](https://github.com/hayk96/kubebridge/commit/076f59607b35d7abd5b2ccb1ae85b437994008b0) - **helm-charts**: Bump app and chart version *(commit by [@hayk96](https://github.com/hayk96))*


## [v0.1.0] - 2025-05-04
### New Features
- [`60275e0b`](https://github.com/hayk96/kubebridge/commit/60275e0bad1f9c47b368c97382e51438c3ce809c) - Add retry for Redis *(commit by [@hayk96](https://github.com/hayk96))*

### Bug Fixes
- [`2511779`](https://github.com/hayk96/kubebridge/commit/f7e4e65c125546429ba2f873b9bce70b9c211a19) - **helm-charts**: Fix notes for verifying functionality *(commit by [@hayk96](https://github.com/hayk96))*
- [`f7e4e65`](https://github.com/hayk96/kubebridge/commit/f7e4e65c125546429ba2f873b9bce70b9c211a19) - **helm-charts**: Fix service key *(commit by [@hayk96](https://github.com/hayk96))*


## [v0.1.0-beta.1] - 2025-04-27
### Chores
- [`327109e`](https://github.com/hayk96/kubebridge/commit/327109e8c30ab7b5f9111327316f47a6d9ec0882) - **src**: PEP8 formatting *(commit by [@hayk96](https://github.com/hayk96))*
- [`047a487`](https://github.com/hayk96/kubebridge/commit/047a487f0157c1d12b233d8fc21998df2029b44d) - **chars**: Update K8S API versions and labels *(commit by [@hayk96](https://github.com/hayk96))*
- [`fee9c56`](https://github.com/hayk96/kubebridge/commit/fee9c5652df8438f5d27bab815d94a62a1b62735) - Bump app and chart beta version *(commit by [@hayk96](https://github.com/hayk96))*


## [v0.1.0-alpha.4] - 2025-04-24
### New Features
- [`090f078`](https://github.com/hayk96/kubebridge/commit/090f078c40d5c546b65cb728fc4b7abacf9a8d94) - Add HTTP server and /health endpoint *(commit by [@hayk96](https://github.com/hayk96))*
- [`34c67aa`](https://github.com/hayk96/kubebridge/commit/34c67aa22af503747c17ef43e5348b7b580a967a) - And /ready endpoint in HTTP server *(commit by [@hayk96](https://github.com/hayk96))*

### Chores
- [`354d540`](https://github.com/hayk96/kubebridge/commit/354d540709f5646e6587a8475f5f97b9606a14b6) - Add HTTP 8080 port in Dockerfile *(commit by [@hayk96](https://github.com/hayk96))*
- [`ba6ddae`](https://github.com/hayk96/kubebridge/commit/ba6ddaee74130578e41a723e0849734d4bb21f5b) - Update HTTP server functions *(commit by [@hayk96](https://github.com/hayk96))*
- [`dd6e933`](https://github.com/hayk96/kubebridge/commit/dd6e9337159a35055da7d1802cd033c312007668) - Add labels to K8s resources *(commit by [@hayk96](https://github.com/hayk96))*
- [`2408eab`](https://github.com/hayk96/kubebridge/commit/2408eab80656116212af6bfeb56e0f0402b8c97b) - **charts**: Add livenessProbe *(commit by [@hayk96](https://github.com/hayk96))*
- [`b0f724c`](https://github.com/hayk96/kubebridge/commit/b0f724c116862bcb4a43c99edce52caefc09111f) - **charts**: Update NOTES.txt *(commit by [@hayk96](https://github.com/hayk96))*
- [`ee5bbc0`](https://github.com/hayk96/kubebridge/commit/ee5bbc0d7b79e098ff9ca90d49f716d842de9bcb) - **charts**: Update values.yaml *(commit by [@hayk96](https://github.com/hayk96))*
- [`e67cb57`](https://github.com/hayk96/kubebridge/commit/e67cb57a82fe8d8017036dca94b8cdd64d85e1b1) - Bump release *(commit by [@hayk96](https://github.com/hayk96))*


## [v0.1.0-alpha.3] - 2025-04-16
### New Features
- [`a9238b5`](https://github.com/hayk96/kubebridge/commit/a9238b51a4816e16f549f9809791130bd5d1e490) - **CI**: Enable update-changelog job *(commit by [@hayk96](https://github.com/hayk96))*

### Bug Fixes
- [`35ad9f1`](https://github.com/hayk96/kubebridge/commit/35ad9f1e333d9a5eb1c397f5228dfee35b3f3d87) - **sync**: Fix environment variable names *(commit by [@hayk96](https://github.com/hayk96))*

### Chores
- [`1a1254a`](https://github.com/hayk96/kubebridge/commit/1a1254a862c2c4929afe7c68418f7334032cc3ad) - **sync**: Update Kubernetes cluster config load env variable *(commit by [@hayk96](https://github.com/hayk96))*
- [`69c9a36`](https://github.com/hayk96/kubebridge/commit/69c9a369ce8dee1757a9fa38787048588f6e4801) - Update function and class descriptions *(commit by [@hayk96](https://github.com/hayk96))*
- [`6c98232`](https://github.com/hayk96/kubebridge/commit/6c98232554655c59a18d2558a8248d98cbc69893) - Rename release.yaml tp release.yml *(commit by [@hayk96](https://github.com/hayk96))*
- [`915c07a`](https://github.com/hayk96/kubebridge/commit/915c07a058ba431e378802c1ebfc673c89f337ea) - **Dockerfile**: Add label for maintainer *(commit by [@hayk96](https://github.com/hayk96))*
- [`8bce850`](https://github.com/hayk96/kubebridge/commit/8bce850c2c54097ac5feb11426f896eaf1e5e393) - Improve logging messages *(commit by [@hayk96](https://github.com/hayk96))*


## [v0.1.0-alpha.2] - 2025-04-13
### New Features
- [`f262eab`](https://github.com/hayk96/kubebridge/commit/f262eabf859daf31c2dc85629bf176bdd72a1761) - **feat(CI)**: Update Release workflow *(commit by [@hayk96](https://github.com/hayk96))*
- [`f262eab`](https://github.com/hayk96/kubebridge/commit/f262eabf859daf31c2dc85629bf176bdd72a1761) - **fix(Dockerfile)**: Use slim image to resolve CVE-2025-29087 *(commit by [@hayk96](https://github.com/hayk96))*

## [v0.1.0-alpha.1] - 2025-04-13
### New Features
- [`6313762`](https://github.com/hayk96/kubebridge/commit/63137620c7b9627547c5470f7ca8b55f37d4fa9a) - **feat**: Add KUBECONFIG_FILE_PATH env variable *(commit by [@hayk96](https://github.com/hayk96))*

## [v0.1.0-alpha.0] - 2025-03-30
### New Features
- [ENHANCEMENT] A Service Discovery for Kubernetes

[v0.1.0-alpha.0]: https://github.com/hayk96/kubebridge/tree/v0.1.0-alpha.0
[v0.1.0-alpha.1]: https://github.com/hayk96/kubebridge/compare/v0.1.0-alpha.0...v0.1.0-alpha.1
[v0.1.0-alpha.2]: https://github.com/hayk96/kubebridge/compare/v0.1.0-alpha.1...v0.1.0-alpha.2
[v0.1.0-alpha.3]: https://github.com/hayk96/kubebridge/compare/v0.1.0-alpha.2...v0.1.0-alpha.3
[v0.1.0-alpha.4]: https://github.com/hayk96/kubebridge/compare/v0.1.0-alpha.3...v0.1.0-alpha.4
[v0.1.0-beta.1]: https://github.com/hayk96/kubebridge/compare/v0.1.0-alpha.4...v0.1.0-beta.1
[v0.1.0]: https://github.com/hayk96/kubebridge/compare/v0.1.0-beta.1...v0.1.0
[v0.2.0]: https://github.com/hayk96/kubebridge/compare/v0.1.0...v0.2.0
[v0.2.1]: https://github.com/hayk96/kubebridge/compare/v0.2.0...v0.2.1
