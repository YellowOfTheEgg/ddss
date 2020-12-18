
# Differential Diagnosis Decision Support System
## Introduction
This project includes the implementation of the diagnostic decision system. The project is divided into several services.
- ddx-backend: contains the ML-service based on noisy-or model and weighted model counting for inference
- ddx-frontend: contains the user interface
- ddx-website: contains additional services to improve the usability of the app. For now this service contains only the autofill backend functionality for entered symptoms
- ddx-gateway-api: this service is an interface between front and backend
- ddx-authentication-api: contains the backend functionality like registration and login


## Prequisites
- Docker version 19.03
- Docker-compose version 1.26.0
- Ubuntu 20.04
- Makefile
- npm version 6.14.4
## Getting Started
To start the whole service stack go into the project folder and run:
```python
make up
```
After all services have been started up, the frontend can be accessed over 
```
http://localhost:80
```
Credentials for the default login are:
- username: admin@qoactive.com
- password: admin

To stop all services, run in the project folder:
```python
make down
```
To remove all downloaded and created images, run:
```python
make cleanup
```
