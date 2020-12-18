## DDX-Authentication-API

[![CircleCI](https://circleci.com/bb/qlaym/ddx-authentication-api/tree/master.svg?style=svg)](https://circleci.com/bb/qlaym/ddx-authentication-api/tree/master)
[![codecov](https://codecov.io/bb/qlaym/ddx-authentication-api/branch/master/graph/badge.svg?token=4Y7G1VCRN3)](https://codecov.io/bb/qlaym/ddx-authentication-api)

A Microservice for for user management and authentication.



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
-- app/core/security.py: contains the token generation for the authentication of the user
-- app/models: contains the definition of the objects which can be passed over to the api-endpoints and the db table definitions
-- app/crud: contains db-operations which are needed for the authentication of the user
-- app/db: contains the functionality of the db-initialization and session management
-- app/utils: contains the email functionality for this service which is disabled for the masterthesis
-- app/scripts: contains the script for the db-initialization

## Introduction
This microservice provides the basic functionalities for user management. This repository is intended to be the base repository to be forked in different projects. In the forked repositories you can add the required business logic in your specific project, but in the current base repository, only changes common to all projects should be performed.

The service provides two main routes

#### /users
This route is used for typical CRUD operations on the User resource. Some operations like creating a new user also support additional functionalities like sending a registration E-Mail to the user.

#### /login
This route is used for getting an OAuth2 compatible access token, which can be used for future requests without the need to renter credentials.

The project uses PostgreSQL as Database. When using this service you can either following the "database per service pattern" (recommended) or create a single database for your project containing user table and all other project-specific tables.


## Getting Started
Don't forget to initialize the database after starting the service.

To start the service:

```python
make build
make up
```

To initialize the database:

```python
make init_db
```

## PGAdmin, PostgreSQL web administration
To access the management tool for Postgres:
```
http://localhost:5050
```

## Documentation
Explore the routes in browser:
```
http://localhost:8000/doc
```

### Migrations

Make sure you create a "revision" of your models and that you "upgrade" your database with that revision every time you change them. 
* Start an interactive session in the backend container:

```console
$ docker-compose exec authentication-api bash
```

* After changing a model create a revision, e.g.:

```console
$ alembic revision --autogenerate -m "Add column last_name to User model"
```

* Commit to the git repository the files generated in the alembic directory.

* After creating the revision, run the migration in the database (this is what will actually change the database):

```console
$ alembic upgrade head
```


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

Notice that ```NETWORK_NAME``` is the name of the network, in which ddx-authentication-api in running. It could be something else on your machine.

The Kibana dashboard can be accessed in the following URL:

```
http://localhost:5601/
```


