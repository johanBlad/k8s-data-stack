
## Kubernetes Cluster for development (KinD)

Create the local development cluster defined in `k8s-cluster-local/kind-cluster.yaml` by moving into the file's directory and running

```
kind create cluster --name data-stack-cluster --config kind-cluster.yaml
```

You can see your cluster by `kind get clusters` and interact with your cluster through `kubectl`

Interact images in your cluster by `crictl`:  

```
docker exec -it <node> crictl images
docker exec -it <node> crictl ps -a 
docker exec -it <node> crictl pods
docker exec -it <node> crictl rmi <image-id>
```

Pull down the docker image  that you want to use, from a registry like docker hub or similar, and then load it into you cluster.

```
docker pull apache/airflow:2.2.3-python3.9
kind load docker-image apache/airflow:2.2.3-python3.9 --name data-stack-cluster
```

<br>

# Todo
- [ ] fix TLS connection timeout to Kind cluster 
