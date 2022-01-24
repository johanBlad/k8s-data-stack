# Postgres source database 

## Todo

- [ ] Change absolute paths for PVs to relative paths for the project

## Deployment

To run the database with persistance locally, first create a dedicated PV and PVC in your cluster. Then, deploy the database to your cluster as a Stateful Set, exposed behind a service.

```
kubectl apply -f pg-pv-pvc.yml 
kubectl apply -f stateful-set.yml
```

You should now be able to interact with your database like so:

```
kubectl exec -n pg-source -it <pod-id> -- psql -d maindb -U admin
```

## Postgres settings

psql cheat sheet:
```
\l                  list all databases
\dt                 list all tables 
\dn                 list all schemas
show all;           list all Postgres settings
```

We can change the default transaction isolation level for a database, or change it on individual transactions or sessions.
```
alter database "maindb" set default_transaction_isolation to 'serializable';

select current_setting('transaction_isolation');

begin transaction isolation level repeatable read;
...
commit;
```

