# NCSA CHECKS

The goal of this project is to have a simple set of functions that
can be used as init containers in your kubernetes deployment. Each
of the checks will see if the service is ready to accept
connections.

For example the following snippet will wait for rabbitmq and 
postgresql to be ready before starting the actual container:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mywebapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mywebapp
  template:
    metadata:
      labels:
        app: mywebapp
    spec:
      initContainers:
        - name: check-rabbitmq
          image: "ncsa/check:1.0.0"
          env:
            - name: RABBITMQ_URI
              value: "amqp://user:pass@rabbitmq/%2F"
        - name: check-postgresql
          image: "ncsa/check:1.0.0"
          env:
            - name: PGHOST
              value: "postgres"
            - name: PGUSER
              value: "postgres"
            - name: PGTABLE
              value: "users"
      containers:
        - name: mywebapp
          image: mywebapp:1.0
          ports:
            - containerPort: 80
          env:
            - name: RABBITMQ_URI
              value: "amqp://user:pass@rabbitmq/%2F"
            - name: PGHOST
              value: "postgres"
            - name: PGUSER
              value: "postgres"
```

## Tests Supported

RabbitMQ
- description : checks to see if can connect to RabbitMQ Server
- exit code : 1
- parameters
  - RABBITMQ_URI [required] : URI for RabbitMQ server 

Mongo
- description : checks to see if can connect to MongoDB Server
- exit code : 2
- parameters
  - MONGO_URI [required] : URI for MongoDB server 

URL
- description : checks to see if URL is reachable and returns status 
  code of 200. If optional text is given the text needs to be in the
  returned body.
- exit code : 3
- parameters
  - URL [required] : URL to check
  - URL_TEXT [optional] : text to be found in body returned 
  
PostgreSQL
- description : checks to see if database is up. Will check to see
  if the optional table exists
- exit code : 4
- parameters
  - PG_URI [required*] : URI to connect to postgresql.
  - PGTABLE [optional] : table that should exist 

## Version History

### 1.0 - 2020-08-07

#### Added
- support for RabbitMQ
- support for MongoDB
- support for URL
- support for PostgreSQL


## TODO:

check_postgres: support for standard postgresql parameters
check_service: check if host:port is reachable

create simple tests for each check
github actions
