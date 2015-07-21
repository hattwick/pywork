__author__ = 'phil'

# Adding working config file for container orchestration workshop

# ORIGINAL ***********************************************************************************************

rng:
    build: rng
    ports:
      - "8001:80"

hasher:
    build: hasher
    ports:
      - "8002:80"

webui:
    build: webui
    links:
      - redis
    ports:
      - "8000:80"
    volumes:
      - "webui/files/:/files/"

redis:
    image: redis

worker:
    build: worker
    links:
      - rng
      - hasher
      - redis


# VERSION 2

