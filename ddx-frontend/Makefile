name = ddxfrontend
image_name = qlaym/ddxfrontend:newest

.PHONY: build
# target: build – build the docker image
build:
	docker-compose -f docker-compose.yml build

.PHONY: up
# target: up – setup the whole system with requirements
up: down
	docker-compose up $(name)

.PHONY: down
# target: down – stops and remoces containers
down:
	docker-compose -f docker-compose.yml down -v

.PHONY: test
# target: test – run tests
test:
	docker run -v ${PWD}:/usr/src/app \
			   -it $(image_name) bash run_tests.sh

.PHONY: test_ci
# target: test – run tests & coverage for circleci
test_ci:
	docker run -v ${PWD}:/usr/src/app \
			   -it $(image_name) bash run_tests_ci.sh
