# Market data pull celery decorator
# Prototype for Python Data Pipelines course by kjam with modifications
# expects tasks1 file in directory for functions

from celery import Celery    #import Celery object from celery module


# default rabbitmq login is guest:guest if not configured
# app assumes a vhost has been setup with a user/port

app = Celery('tasks',
			broker='amqp://celery_user:c3l3ry@localhost:5672/celery_vhost',
			backend='rpc://')