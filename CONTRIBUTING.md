# Contributing

The KubeBridge uses GitHub to manage and review pull requests.

* If you are a new contributor see: [Steps to Contribute](#steps-to-contribute)

* If you have a minor fix or enhancement, feel free to submit a pull request.
* If you're considering a more complex change, please first share your ideas on our discussion [discussions](https://github.com/hayk96/kubebridge/discussions/new/choose).
  This approach will prevent unnecessary effort and will undoubtedly provide both you and us with a great deal of inspiration.

* Relevant coding style guidelines and formatting are the [PEP 8](https://peps.python.org/pep-0008/).

* Be sure to sign off on the [DCO](https://github.com/probot/dco#how-it-works).

## Steps to Contribute

If you'd like to tackle an issue, please claim it by commenting on the GitHub issue to indicate your intention to work on it. This helps avoid multiple contributors working on the same issue simultaneously.

To quickly run the project locally and test your changes, please do the following:

__Please make sure you already have the following prerequisites:__
* Redis server
* Kubernetes cluster

```bash
git clone https://github.com/hayk96/kubebridge.git
cd kubebridge
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Sync component
```bash
export APP_NAME=sync
export DEPLOYMENT_ENV=development
export KUBECONFIG_FILE=~/.kube/your_kubeconfig_file
export LOG_LEVEL=debug
export REDIS_HOST=127.0.0.1
export REDIS_PORT=6379
export REDIS_USER=default
export REDIS_PASSWORD=xxx-yyy-zzz
export ALLOW_NAMESPACES=["*"]
export DENY_NAMESPACES=["kube-system","kube-public"]
export ALLOW_SERVICE_TYPES=["ClusterIP", "NodePort", "LoadBalancer"]

python3 main.py
```

#### DNS component
```bash
export APP_NAME=dns
export LOG_LEVEL=debug
export REDIS_HOST=127.0.0.1
export REDIS_PORT=6379
export REDIS_USER=default
export REDIS_PASSWORD=xxx-yyy-zzz
export DOMAIN=kube.bridge
export EXTRA_DNS_CONFIG='{"A": {"kubebridge.io.": ["127.0.0.1"]}, "CNAME": {"kube-bridge.io": "kubebridge.io."}}'

python3 main.py
```

We use [`ruff-action`](https://github.com/chartboost/ruff-action) for linting the code. This means the committed code can be reported by the linter when it exits with failures. In some cases, your changes can also be fixed or modified by the linter.

All our issues are regularly tagged, allowing you to filter down to the issues related to the components you are interested in working on.

## Pull Request Checklist

* Branch from the main branch and, if needed, rebase to the current main branch before submitting your pull request. If it doesn't merge cleanly with main you may be asked to rebase your changes.

* Commits should be as small as possible, while ensuring that each commit is correct independently.
* PR descriptions should contain comprehensive descriptions of all commits introduced by the appropriate PR. You can find and example [here](https://github.com/hayk96/kubebridge/pull/1).
