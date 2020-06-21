#!/bin/bash

docker-compose build mysql
docker-compose build web-www
docker-compose build tasksworker
docker-compose build redis-web

docker-compose push mysql
docker-compose push web-www
docker-compose push tasksworker
docker-compose push redis-web