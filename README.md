# Self-Healing Kubernetes Cluster

## Introduction

This project demonstrates a self-healing Kubernetes cluster that automatically detects, diagnoses, and recovers from failures such as pod crashes, node failures, and service disruptions. 

## Setup Instructions

### Prerequisites

- Kubernetes cluster (e.g., Minikube, GKE, EKS, AKS)
- Helm
- Python 3.6+

### Installation

1. **Deploy Prometheus and Grafana**:
    ```bash
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update
    helm install prometheus prometheus-community/prometheus --namespace monitoring --create-namespace
    helm install grafana prometheus-community/grafana --namespace monitoring
    ```

2. **Apply Kubernetes Manifests**:
    ```bash
    kubectl apply -f k8s-manifests/deployment.yaml
    kubectl apply -f k8s-manifests/service.yaml
    ```

3. **Configure Alertmanager**:
    ```bash
    kubectl apply -f scripts/alertmanager_config.yml
    ```

4. **Set up Self-Healing Scripts**:
    - Ensure the `self_healing.py` and `remediation.py` scripts are executable.
    - You may need to adjust the scripts to match your environment.

### Usage

- The self-healing script (`self_healing.py`) can be run manually or scheduled as a cron job.
- The script logs all actions to `logs/remediation.log`.

### Customisation

- Modify the Prometheus and Grafana configurations as needed.
- Adjust the self-healing logic in `self_healing.py` and `remediation.py`.
