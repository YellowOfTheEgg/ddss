.PHONY: up
up: 
	./scripts/run.sh

.PHONY: down
down: 
	./scripts/stop.sh

.PHONY: cleanup
cleanup: 
	./scripts/cleanup.sh
