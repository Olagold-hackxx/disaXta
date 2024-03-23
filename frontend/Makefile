LOCAL_WEB_CONTAINER_NAME=frontend
LOCAL_DOCKER_OPTIONS= -f docker-compose.yml


up:
	docker-compose  $(LOCAL_DOCKER_OPTIONS) up -d

down:
	docker-compose $(LOCAL_DOCKER_OPTIONS) down

stop:
	docker-compose $(LOCAL_DOCKER_OPTIONS) stop

server:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) npm run dev

build:
	docker-compose $(LOCAL_DOCKER_OPTIONS) build

rebuild:
	docker-compose $(LOCAL_DOCKER_OPTIONS) build --force-recreate --no-deps
