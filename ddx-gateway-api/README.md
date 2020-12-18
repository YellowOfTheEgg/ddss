## QRT API Gateway

[![CircleCI](https://circleci.com/bb/qlaym/ddx-api-gateway/tree/master.svg?style=svg)](https://circleci.com/bb/qlaym/ddx-api-gateway/tree/master)

An API Gateway for the DDX Backend Services. The gateway api is an entrypoint for the frontend which routes and forwards all requests to the backend services. 

## Project structure
- **requirements.txt**: contains libraries which are used by this component
- **Dockerfile**: contains the definition of the frontend docker-image for productive use
- **run.sh**: defines the entrypoint for the container
- **docker-compose.yml**: contains stuff like volume mapping, port definitions, env-vars for the container
- **Makefile**: contains shortcutted command for starting,stopping and testing container. The file contains also the command definition for the initialization of the database
- **main**: contains the definition of the fastapi-router and middleware
- **app**: contains the api with a proxy which forwards requests to the backend services
-- app/api/v1: contains the definitions of the api endpoints
-- app/core/config.py: contains actual api version and the service-name
-- app/models: contains the definition of the objects which can be passed over to the api-endpoints

## Introduction
Ths API Gateway is the single entry point for all clients. The requests are simply proxied/routed to the appropriate service. It also takes care of authentication, so that it is not anymore necessary in other services to implement the authentication logic.

Following services are currently integrated into the gateway:

#### 1. DDX Authentication API


## Getting Started
To start the service:

```python
make build
make up
```

## Documentation
Explore the routes in browser:
```
http://localhost:8000/doc
```
Notice that the documentation of the gateway is not really useful currently. See how requests can be done in the corresponding services behid the gateway, such as [DDX Authentication API](https://bitbucket.org/qlaym/ddx-authentication-api/src/master/).

To connect the frontend with the gateway u have to customize CORS_ORIGINS in the .env file.
Add the origin based on your external docker-ip and the port of your frontend.


# Testing
To run the tests:

```python
make up
make test
```

## Deployment
Here, with deployment we mean pushing an updated version of the Docker image to ECR, which can be used for deploying the application on different environments, such as in-house cluster or AWS. Please always make sure, that the build was successful before deployment. Do the following to create a new version of the image:

```
git tag vX.Y.Z
git push origin tag vX.Y.Z
```

Semantic Versioning is a 3-component number in the format of X.Y.Z, where :

X stands for a major version.
Y stands for a minor version.
Z stands for a patch.

## ELK Stack
In case you want to use ELK stack in development use the following command to start the ELK stack. Starting the stack will take a while and will consume lots of resources, but it helps to write better logging messages in the code.

```
git clone https://bitbucket.org/qlaym/elk/src/master/
NETWORK_NAME=authentication-api_default make up
```

Notice that ```NETWORK_NAME``` is the name of the network, in which authentication-api in running. It could be something else on your machine.

The Kibana dashboard can be accessed in the following URL:

```
http://localhost:5601/
```


