LOCAL_WEB_CONTAINER_NAME=backend.web
LOCAL_DB_CONTAINER_NAME=backend.db
LOCAL_DOCKER_OPTIONS= -f docker-compose.yml


up:
	docker-compose  $(LOCAL_DOCKER_OPTIONS) up -d

down:
	docker-compose $(LOCAL_DOCKER_OPTIONS) down

stop:
	docker-compose $(LOCAL_DOCKER_OPTIONS) stop

server:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) python manage.py runserver 0:8000

collectstatic:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) python manage.py collectstatic --noinput

build:
	docker-compose $(LOCAL_DOCKER_OPTIONS) build

rebuild:
	docker-compose $(LOCAL_DOCKER_OPTIONS) build --force-recreate --no-deps

test:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) pytest

ssh:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) /bin/sh

superuser:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) python manage.py createsuperuser

requirements:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) pip install -r requirements.txt

migrations:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) python manage.py makemigrations

migrate:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) python manage.py migrate

db-shell:
	docker exec -it $(LOCAL_DB_CONTAINER_NAME) mysql -u disaXta -p

db-ssh:
	docker exec -it $(LOCAL_DB_CONTAINER_NAME) /bin/sh

reset-db:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) python manage.py reset_db

apply-fixtures:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) python manage.py loaddata fixtures/*.yaml
