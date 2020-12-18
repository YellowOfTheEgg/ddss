## DDx Backend

[![CircleCI](https://circleci.com/bb/qlaym/ddx-backend.svg?style=svg)](https://circleci.com/bb/qlaym/ddx-backend)
[![codecov](https://codecov.io/bb/qlaym/ddx-backend/branch/master/graph/badge.svg?token=5XCNMNR4I2)](https://codecov.io/bb/qlaym/ddx-backend)

This service calculates probabilities for diseases based on given symptoms. The calculation is based on WMC1-Encoding, WMC1-Zerlegung, Noisy-Or-Model, WMC-Solver (Cachet)

## Project structure
- **requirements.txt**: contains libraries which are used by this component
- **Dockerfile**: contains the definition of the frontend docker-image for productive use
- **run.sh**: defines the entrypoint for the container
- **docker-compose.yml**: contains stuff like volume mapping, port definitions, env-vars for the container
- **Makefile**: contains shortcutted command for starting,stopping and testing container. The file contains also the command definition for the initialization of the database
- **test**: contains some tests for the project
- **main**: contains the definition of the fastapi-router and middleware
- **app**: contains the api with the ml-module
-- app/api/v1: contains the definitions of the api endpoints
-- app/core/config.py: contains actual api version and the service-name
-- app/models: contains the definition of the objects which can be passed over to the api-endpoints
- **app/engine/wmc_v3**: contains the ML-Module (WMC1-Encoding, Cachet and WMC1-Zerlegung)
-- app/engine/wmc_v3/cachet: contains the cachet wmc-solver
-- app/engine/wmc_v3/core: contains the WMC1-Encoding, Zerlegung and DIMACS-Convertion of the entered symptoms
-- app/engine/wmc_v3/crud: contains the database operations which are needed for the WMC1-Encoding
-- app/engine/wmc_v3/db: contains db-session-functionality and table definitions
-- app/engine/wmc_v3/scripts: contains the database initialization based on the given Knowledgebase.csv
-- app/engine/wmc_v3/config: contains the db credentials
-- app/engine/wmc_v3/ddx: entrypoint for the ml-module

## Getting Started

To start the service:
```python
make build
make up
```

Explore the routes in browser:

```python
http://localhost:8000/docs
```

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
