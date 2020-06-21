#!/bin/bash

echo Building Prod Web...
docker-compose -f docker-compose-prod.yml build prod_web
echo Done.
echo Building Prod Tasksworker...
docker-compose -f docker-compose-prod.yml build prod_tasksworker
echo Done.
echo Building Prod Redis-Web
docker-compose -f docker-compose-prod.yml build prod_redis-web
echo Done.


echo Pushing Prod Web...
docker-compose -f docker-compose-prod.yml push prod_web
echo Done.
echo Pushing Prod Tasksworker...
docker-compose -f docker-compose-prod.yml push prod_tasksworker
echo Done.
echo Pushing Prod Redis-Web...
docker-compose -f docker-compose-prod.yml push prod_redis-web
echo Done.

echo Completed.