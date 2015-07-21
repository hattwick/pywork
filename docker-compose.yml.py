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

rng1:
    build: rng


rng2:
    build: rng

rng3:
    build: rng

rng0:
    image: jpetazzo/hamba
    links:
      - rng1
      - rng2
      - rng3
    command: 80 rng1 80 rng2 80 rng3 80
    ports:
      -  "8001:80"

hasher:
    build: hasher
    ports:
      - "8002:80"

webui:
    build: webui
    #links:
    #  - redis
    ports:
      - "8000:80"
    extra_hosts:
      redis: 52.6.86.223
   # volumes:
   #   - "webui/files/:/files/"

#redis:
#    image: redis

worker:
    build: worker
    links:
      - rng
      - hasher
    extra_hosts:
      redis: 52.6.86.223




# FINAL TEST

rng1:
    build: rng


rng2:
    build: rng

rng3:
    build: rng

rng0:
    image: jpetazzo/hamba
    links:
      - rng1
      - rng2
      - rng3
    command: 80 rng1 80 rng2 80 rng3 80
    ports:
      -  "8001:80"

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
   # volumes:
   #   - "webui/files/:/files/"

redis:
    image: jpetazzo/hamba
    command: 6379 52.6.86.223 32768

worker:
    build: worker
    links:
      - rng0
      - hasher
      - redis

