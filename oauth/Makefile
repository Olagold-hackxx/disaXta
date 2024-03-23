LOCAL_WEB_CONTAINER_NAME=oauth.web
LOCAL_DB_CONTAINER_NAME=oauth.db
LOCAL_DOCKER_OPTIONS= -f docker-compose.yml


up:
	docker-compose  $(LOCAL_DOCKER_OPTIONS) up -d 

down:
	docker-compose $(LOCAL_DOCKER_OPTIONS) down

stop:
	docker-compose $(LOCAL_DOCKER_OPTIONS) stop

server:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) npm start

build:
	docker-compose $(LOCAL_DOCKER_OPTIONS) build

rebuild:
	docker-compose $(LOCAL_DOCKER_OPTIONS) build --force-recreate --no-deps

ssh:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) /bin/sh

db-shell:
	docker exec -it $(LOCAL_DB_CONTAINER_NAME) mysql -u disaXta -p

db-ssh:
	docker exec -it $(LOCAL_DB_CONTAINER_NAME) /bin/sh
