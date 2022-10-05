# Weather API Challenge

This is a django API application that allows a user to get the minimum, maximum, average and median temperature for a given city over a period of time.

#### Expected deliverables

Create a Django application with RESTful API

* Django application must run locally
* API must be in the format /api/locations/{city}/?days={number_of_days}
* API must fetch weather data from some public API of your choice
* API must compute min, max, average, and median temperature
* Response format must be in the following structure:

```json
{
  "maximum": "value",
  "minimum": "value",
  "average": "value",
  "median": "value"
}
```

## Deployment

Project can be deployed in two ways.

1. Docker Container
2. Django Server(Development & test)

## Deploy using Docker

For quick setup, use docker.

### Requirements

* Docker
* Docker-compose

### Ports

Ensure below ports are not occupied by any running service.

* 80,443 - `Nginx Webserver`

### Deploying using docker

```shell
bash setup_docker.sh
```

### Admin

```shell
https://<host>/admin
username:admin
password:admin
```


### Requirements

* Python3.6+

### Run

Run develop server.

```shell
# Install required python libraries
pip install -r requirements.txt
# Copy env.example to .env
cp env.example .env
# Migrate migrations
./manage.py migrate
# Run server
./manage.py runserver

```

### Run Test
To run unit test.
```shell
$ ./manage.py pytest
```

### API Documentation
[Documentation](http://localhost:8000/docs/)
### API Collection
[POSTMAN Collection](https://www.getpostman.com/collections/50dc924c6f119d6033f6)
