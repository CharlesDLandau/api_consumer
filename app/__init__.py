from celery import Celery
import redis
import managers.celery_config as celery_conf

# Instantiate and config celery
celery = Celery()
celery.config_from_object(celery_conf)

# Instantiate py-redis
redis_store = redis.StrictRedis(
    host=celery_conf.REDIS_HOSTNAME,
    port=celery_conf.REDIS_PORT)

# We need this for task discovery
from app import tasks
