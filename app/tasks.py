from app import celery
import managers
import handlers

# In case you assign a custom API consumer
if managers.api_consumer_config.USE_CUSTOM_API_CONSUMER:
    api_consumer = handlers.api_consumer
else:
    api_consumer = handlers.default_api_consumer


@celery.task()
def api_response_consumer():
    return api_consumer()
