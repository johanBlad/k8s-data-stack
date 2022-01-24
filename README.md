# Kuberneters Data Stack POC 

POC to host data stack on Kubernetes 

## Components 
- Kubernetes Cluster for development (KinD)
- Kubernetes Cluster for production  (EKS on AWS)
- Postgres Data Warehouse 
- Postgres OLTP Source 
- External Vendor Source (Slack, Github, ?)
- Airbyte 
- Airflow 
- SuperSet 
- dbt as a service

## Todo

- [x] Local Kubernetes cluster 
- [x] Airflow project and K8s deployment
- [ ] Postgres source deployment and mock data
- [ ] Postgres Data Warehouse 
- [ ] Airbyte deployment 
- [ ] SuperSet deployment
- [ ] EKS Kubernetes cluster and deployment 


## Requirements
- kubectl
- kind / k3s / docker k8s / minikube 
- helm
- docker

