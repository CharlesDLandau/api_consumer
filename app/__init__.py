import managers
from flask_redis import FlaskRedis
from flask import Flask

# Instantiate and config flask
flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL=managers.celery_config.CELERY_BROKER_URL,
    CELERY_RESULT_BACKEND=managers.celery_config.CELERY_RESULT_BACKEND,
    REDIS_URL=managers.celery_config.REDIS_URL
)

# Instantiate and config celery from flask
celery = managers.make_celery(flask_app)
celery.config_from_object(managers.celery_config)

# Instantiate py-redis
redis_store = FlaskRedis(flask_app)

# We need this for task discovery
from app import tasks
