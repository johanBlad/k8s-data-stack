## Airflow 

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
helm show values apache-airflow/airflow > values.yml
helm upgrade --install airflow apache-airflow/airflow -n airflow -f values.yml --debug --timeout 10m0s
```

To delete the helm deployment from you cluster:

```
helm delete airflow --namespace airflow
```