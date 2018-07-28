# Celery config options
BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERYBEAT_SCHEDULE = {
    "api_response_consumer": {
        "task": "app.tasks.api_response_consumer",
        'schedule': 30.0,
    }
}
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# In case we want py-redis to access a different broker from celery
REDIS_HOSTNAME = 'redis'
REDIS_PORT = 6379
