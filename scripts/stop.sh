#!/bin/bash
echo "stopping ddx-frontend service..."
cd ./ddx-frontend
docker-compose down
cd ../

echo "stopping ddx-gateway-api service..."
cd ./ddx-gateway-api
docker-compose down
cd ../

echo "stopping the ddx-backend service..."
cd ./ddx-backend
docker-compose down
cd ../

echo "stopping ddx-authentication services..."
cd ./ddx-authentication-api
docker-compose down
cd ../

echo "stopping ddx-website service..."
cd ./ddx-website
docker-compose down
cd ../



