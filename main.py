from app import redis_store
import redis
import managers

# We need this for task discovery at main.
from app import celery


if __name__ == '__main__':
    """ Check the connection to the MQ, in this case
        redis. You can write your own... """
    try:
        print("Trying to ping redis...")
        i = redis_store.ping()
        print("{}".format(i))

        p = redis_store.pubsub(ignore_subscribe_messages=True)
        p.subscribe(managers.REDIS_PUBSUB_CHANNEL)
        redis_ready = True
    except redis.exceptions.ConnectionError as e:
        redis_ready = False
        print("redis failed to ping!")
        print(e)
