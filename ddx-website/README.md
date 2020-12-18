## DDx Website


This service contains the autocomplete functionality of the frontend from backend side of view.

## Project structure
- **requirements.txt**: contains libraries which are used by this component
- **Dockerfile**: contains the definition of the frontend docker-image for productive use
- **run.sh**: defines the entrypoint for the container
- **docker-compose.yml**: contains stuff like volume mapping, port definitions, env-vars for the container
- **Makefile**: contains shortcutted command for starting,stopping and testing container. The file contains also the command definition for the initialization of the database
- **main**: contains the definition of the fastapi-router and middleware
- **app**: contains the api with the autocomplete-module
-- app/api/v1: contains the definitions of the api endpoints
-- app/core/config.py: contains actual api version and the service-name
-- app/models: contains the definition of the objects which can be passed over to the api-endpoints
-- app/crud: for now this folder contains an interface for getting data from the knowledgebase
-- app/engine: contains the knowledgebase.csv and a script for creating a list of symptoms which is used by /app/crud/knowledge_base.py
- **app/autocomplete**: contains the Autocomplete-Module 


## Getting Started

To start the service:
```python
make build
make up
```

Explore the routes in browser:

```python
http://localhost:8003/docs
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
