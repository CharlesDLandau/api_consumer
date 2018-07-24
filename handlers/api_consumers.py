from app import flask_app, redis_store
import managers
import requests


def api_consumer():
    """To customize the consumption behavior, write your code here. When
    you're finished, don't forget to update api_consumer_config.py's
    USE_CUSTOM_API_CONSUMER to True.
    """
    pass


def default_api_consumer():
    """Consumes the example API at the lovely jsonplaceholder.typicode.com
    and sends to the message queue."""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code != 200:
        msg = "ERROR: API returned status code {}.".format(r.status_code)
        redis_store.publish(managers.REDIS_PUBSUB_CHANNEL, msg)
        return msg
    msg = r.json()
    pb = redis_store.publish(managers.REDIS_PUBSUB_CHANNEL, msg)
    flask_app.logger.info(pb)
    return msg
