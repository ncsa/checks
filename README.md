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
          image: "ncsa/checks:1.0.0"
          env:
            - name: RABBITMQ_URI
              value: "amqp://user:pass@rabbitmq/%2F"
        - name: check-postgresql
          image: "ncsa/checks:1.0.0"
          env:
            - name: PGURI
              value: "postgresql://postgres:secret@postgresql:5432/mydb"
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
  - PGURI [required*] : URI to connect to postgresql.
  - PGUSER [required*] : 
  - PGPASSWORD [required*] : 
  - PGHOST [required*] : 
  - PGPORT [required*] : 
  - PGDATABASE [required*] : 
  - PGTABLE [optional] : table that should exist 

* either PG_URI or on of the PG* should be provided. 

## TODO:

- check_service: check if host:port is reachable
- create simple tests for each check
- add db/collection for mongo to test access
