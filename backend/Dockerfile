FROM python:3.10.12-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG ALLOWED_HOSTS
ENV ALLOWED_HOSTS=$ALLOWED_HOSTS

ARG MYSQL_HOST
ENV MYSQL_HOST=$MYSQL_HOST


# Set work directory
WORKDIR /backend

RUN apt-get update -y
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config
RUN pip install --upgrade pip


# Copy project
COPY . /backend/

# Install dependencies
RUN pip install -r requirements.txt

CMD ["sh", "entrypoint.sh"]

