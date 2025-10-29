#!/bin/bash
set -e

# Get the container ID of the running container (if any)
containerid=$(docker ps -q)

# If a container is running, stop and remove it
if [ -n "$containerid" ]; then
    echo "Stopping and removing existing container(s)..."
    docker rm -f $containerid
else
    echo "No running container found."
fi
