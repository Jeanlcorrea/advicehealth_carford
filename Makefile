.PHONY: stop remove build

stop:
    @containers=$$(docker ps -aq); \
    if [ -n "$$containers" ]; then \
    	docker stop $$containers; \
    else \
        echo "No containers to stop."; \
    fi

remove: stop
    @containers=$$(docker ps -aq); \
    if [ -n "$$containers" ]; then \
        docker rm $$containers; \
    else \
        echo "No containers to remove."; \
    fi

# RECREATE DOCKER BUILD
build: remove
	docker-compose up --build

.PHONY: up down

containers-up:
	docker-compose up

containers-down:
	docker-compose down
