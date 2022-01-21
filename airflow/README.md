# Airflow 

## Todo

- [ ] Deploy on local K8s cluster 
- [ ] Set up K8s PVC for Airflow to hold dags
- [ ] Set up Airflow project, DAGs, operators etc.
- [ ] Configure KubernetesExecutor
- [ ] Deploy on EKS cluster 

## Kubernetes deployment

Create a namespace for Airflow in your cluster 
```
kubectl create namespace airflow
```

Pull down the official Airflow helm chart

```
helm repo add apache-airflow https://airflow.apache.org
helm repo update
helm repo ls
```

To edit config variables for the Airflow helm deployment, pull down the config into a local file, and edit it, for example by changing the docker image tag. Then install the helm chart with updated variables.

```
helm show values apache-airflow/airflow > k8s/values.yml
helm upgrade --install airflow apache-airflow/airflow -n airflow -f values.yml --debug --timeout 10m0s
```

After the helm chart is successfully deployed, you can access the webserver through https://localhost:8080, after port forwarding from you cluster:
```
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow
```


To delete the helm deployment from you cluster:
```
helm delete airflow --namespace airflow
```

## Set up DAGs 

The Airflow DAG directory is hosted as a Kubernetes Persistent Volume under `dags/` on the host machine. To create the PV and PVC, apply the following resources.
```
kubectl apply -f k8s/dag-pv.yml
kubectl apply -f k8s/dag-pvc.yml
```

If needed, update `values.yml` to point to that PVC, and redeploy the helm chart. All files under `dags/` on the host machine should now be mapped to `/opt/airflow/dags` on the Airflow containers running on Kubernetes.