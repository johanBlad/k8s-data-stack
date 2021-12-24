# Kuberneters Data Stack POC 

POC to host data stack on Kubernetes 

# Components 
- Kubernetes Cluster for development (KinD)
- Kubernetes Cluster for production  (EKS on AWS)
- Postgres Data Warehouse 
- Postgres OLTP Source 
- External Vendor Source (Slack, Github, ?)
- Airbyte 
- Airflow 
- SuperSet 

# Requirements
- kubectl
- kind
- helm
- docker


## Kubernetes Cluster for development (KinD)

Create the local development cluster defined in `k8s-cluster-local/kind-cluster.yaml` by moving into the file's directory and running

```
kind create cluster --name data-stack-cluster --config kind-cluster.yaml
```

You can see your cluster by `kind get clusters` and interact with your cluster through `kubectl`

## Airflow 

Create a namespace for Airflow in your cluster 
```
kubectl create namespace airflow
```



Deploy Airflow helm chart

```
helm repo add apache-airflow https://airflow.apache.org
helm repo update
helm repo ls

helm install airflow apache-airflow/airflow --namespace airflow --debug --timeout 10m0s
```


