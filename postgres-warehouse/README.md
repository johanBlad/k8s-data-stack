# Data Warehouse

Postgres Data Warehouse, deployed using Bitnami's official helm chart, packaged as a subchart for easier config. 

## Deployment 

First build the chart and then install it in a separate namespace.

```
kubectl create namespace dwh

helm dependency build ./postgreschart
helm install warehouse ./postgreschart -n dwh
```

## Parameters

Parameters for the Postgres instance is set in the `values.yml` file in the parent chart. To add additional parameters from the original Bitnami chart, copy them under the `postgresql` section in `Values.yml`.