name = ddxbackend
image_name = qlaym/dxxbackend:newest

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

.PHONY: test
# target: test – run tests
test:
	docker run -v ${PWD}:/usr/src/app \
			   -it $(image_name) sh run_tests.sh

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

.PHONY: init_db
# target: init_db – initialize the database
init_db:
	docker-compose run $(name) bash app/engine/models/wmc_v3/scripts/init_db.sh

test_script_v1:
	docker-compose run $(name) bash app/engine/models/wmc/scripts/test_script.sh
test_script_v2:
	docker-compose run $(name) bash app/engine/models/wmc_optimized/scripts/test_script.sh
test_script_v3:
	docker-compose run $(name) bash app/engine/models/wmc_v3/scripts/test_script.sh

performance:
	docker-compose run $(name) bash app/performance_comparison/performance.sh