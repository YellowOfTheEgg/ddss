name = ddx-authentication-api
image_name = qlaym/ddx-authentication-api:newest


.PHONY: build
# target: build – build the docker image
build:
	docker-compose -f docker-compose.yml build

.PHONY: up
# target: up – setup the whole system with requirements
up: down
	docker-compose -f docker-compose.yml up

.PHONY: down
# target: down – stops and remoces containers
down:
	docker-compose -f docker-compose.yml down -v

.PHONY: init_db
# target: init_db – initialize the database
init_db:
	docker-compose run $(name) bash scripts/init_db.sh

.PHONY: test
# target: test – run tests
test: init_db
	docker-compose run $(name) bash run_tests.sh

.PHONY: coverage
# target: coverage – run coverage
coverage:
	docker run -v ${PWD}:/usr/src/app \
			   -it $(image_name) bash run_coverage.sh

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
