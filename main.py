from app import flask_app
from app import redis_store
from flask import jsonify
import redis
import json
import managers

# We need this for task discovery at main.
from app import celery

# Check the connection to the MQ, in this case redis. You can write your own...
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


@flask_app.route('/')
def hello():
    # Simply expose the base route
    msg = "Hello Flask!"
    return jsonify(msg)


@flask_app.route('/expose_redis/')
def expose_redis():
    """Demonstrates that the celery and redis behavior can be bound
    to REST endpoint(s), e.g. for health checks."""
    msg = p.get_message()
    if isinstance(msg, dict):
        return jsonify(json.loads(
            # The data came in with illegal single quotes on the keys.
            msg['data'].decode('utf8').replace("'", '"')))
    else:
        return jsonify("No messages left in the queue...")


if __name__ == "__main__":
    # Replace with gunicorn for prod, I guess
    flask_app.run('0.0.0.0', 8000, debug=True)
