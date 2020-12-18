# DDx Frontend

[![CircleCI](https://circleci.com/bb/qlaym/ddx-frontend.svg?style=svg)](https://circleci.com/bb/qlaym/ddx-frontend)
[![codecov](https://codecov.io/bb/qlaym/ddx-frontend/branch/master/graph/badge.svg?token=3J6WBDL6NV)](https://codecov.io/bb/qlaym/ddx-frontend)

## Project structure
- **package.json**: contains react extensions which are needed for the project
- **Dockerfile-dev**: contains the definition of the frontend docker-image for development
- **Dockerfile**: contains the definition of the frontend docker-image for productive use
- **nginx.conf**: the productive service is running inside a nginx-server. Nginx.conf contains the configuration of the routing of this server
- **docker-compose.yml**: contains stuff like volume mapping, port definitions, env-vars for a container
- **src**: contains frontend specific files
-- src/components: contains frontend-components which can be used in different pages
-- src/containers: contains frontend-pages
-- src/context: contains variables which can be accessed from all components
-- src/hooks: contains the file for periodical backend requests. Debounce is used for the autocomplete component
-- src/styles: contains css files for styling
-- src/api: contains the definition for the backend-endpoint
-- src/App: react-wrapper for react-pages and components
-- src/app.module.scss: contains the general positional styling of the frontend
-- src/config.js: read in of ENV-Variables
-- src/index.js: entrypoint for the react components
-- src/routes.js: contains routes of different pages





## Development in Docker Container

First, build the image:

```
make build
```

Then, start up the container for development:

```
make up
```

The app can be viewed in the browser by accessing:

```
http://localhost:3000/
```


## Local Development

First, install all the necessary packages:

```
npm install
```

Then, use the following command in order to start the development server:

```
npm start
```

The app can be viewed in the browser by accessing:

```
http://localhost:80/
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
