name = ddx-api-gateway
image_name = qlaym/ddx-api-gateway:newest


.PHONY: build
# target: build – build the docker image
build:
	docker-compose -f docker-compose.yml build
	rm -rf packages

.PHONY: up
# target: up – setup the whole system with requirements
up: down
	docker network create exnet || true
	docker-compose -f docker-compose.yml up

.PHONY: down
# target: down – stops and remoces containers
down:
	docker-compose -f docker-compose.yml down -v

.PHONY: clean
# target: clean – clean the project's directory
clean:
	@find . \
		-name *.py[cod] -exec rm -fv {} + -o \
		-name __pycache__ -exec rm -rfv {} +

.PHONY: help
# target: help – display all callable targets
help:
	@echo
	@egrep "^\s*#\s*target\s*:\s*" [Mm]akefile \
	| sed -r "s/^\s*#\s*target\s*:\s*//g"
	@echo
