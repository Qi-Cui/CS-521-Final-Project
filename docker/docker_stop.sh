#!/usr/bin/env bash

source "$(dirname $0)/_docker_utils.sh"
sudo docker-compose -f docker/docker-compose.yml down --volumes --remove-orphans

docker_compose stop
