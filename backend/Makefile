LOCAL_WEB_CONTAINER_NAME=disaXta.web
LOCAL_DB_CONTAINER_NAME=disaXta.db
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

requiremelnts:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) pip install -r requirements.txt

migrations:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) python manage.py makemigrations $(app)

migrate:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) python manage.py migrate

db-shell:
	docker exec -it $(LOCAL_DB_CONTAINER_NAME) mysql -u disaXta

db-ssh:
	docker exec -it $(LOCAL_DB_CONTAINER_NAME) /bin/sh

reset-db:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) python manage.py reset_db

apply-fixtures:
	docker exec -it $(LOCAL_WEB_CONTAINER_NAME) python manage.py loaddata fixtures/*.yaml

help:
	@echo "Management commands for Celsius:"
	@echo
	@echo "Usage:"
	@echo "    make build           Build the development containers"
	@echo "    make rebuild         Rebuild the development containers"
	@echo "    make up              Create and start development containers"
	@echo "    make down            Stop and remove development containers"
	@echo "    make stop            Stop development containers"
	@echo "    make server          Start the Django development server"
	@echo "    make collectstatic   Collect static files"
	@echo "    make ssh             SSH to the web container"
	@echo "    make requirements    Install Python requirements"
	@echo "    make db-shell        Open a terminal shell to the database container"
	@echo "    make db-ssh          SSH to the database container"
	@echo "    make reset-db        Reset the database"
	@echo "    make test            Run tests"
	@echo "    make flake8          Run flake8"
	@echo "    make migrations      Make migrations"
	@echo "    make migrate         Migrate database"
	@echo "    make help            This help text."

.PHONY: build rebuild up down stop server collectstatic ssh flake8 requirements db-shell db-ssh test migrations migrate reset-db help
.DEFAULT_GOAL := help

## native
_install_pip_tools:
	python -m piptools > /dev/null 2>&1 || pip install pip-tools

install_req: _install_pip_tools  ## install python requirements
	pip install -r requirements.txt

apply-fixtures-native:
	python manage.py migrate
	python manage.py loaddata fixtures/accounts_user.yaml
