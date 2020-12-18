#!/bin/bash
is_healthy() {
    service="$1"
    health_status="$(docker inspect -f "{{.State.Health.Status}}" "$service")"

    if [ "$health_status" = "healthy" ]; then
        return 1
    else
        return 0
    fi
}



echo "starting ddx-authentication-api services..."
cd ./ddx-authentication-api
docker-compose up -d
echo "waiting for the ddx-db container..."
while ! is_healthy ddx-db; do sleep 1; done

echo "initializing authentication db..."
make init_db

echo "starting ddx-backend service..."
cd ../
cd ./ddx-backend
docker-compose up -d
echo "initializing ddx-backend db..."
make init_db
cd ../

echo "starting ddx-website service..."
cd ./ddx-website
docker-compose up -d
cd ../

echo "starting ddx-gateway-api service..."
cd ./ddx-gateway-api
docker-compose up -d
cd ../

echo "starting ddx-frontend service ..."
cd ./ddx-frontend
docker-compose up -d
cd ../
	echo "all services are ready for connections now!"

