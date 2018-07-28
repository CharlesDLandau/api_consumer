from app import celery
from app import redis_store
from managers import api_consumer_config


@celery.task()
def api_response_consumer():
    # Replace with your favorite API call and publish the output...
    print("Hello World!!!")
    redis_store.publish(
        api_consumer_config.REDIS_PUBSUB_CHANNEL, ["Hello World!"]
    )
