import redis


def get_redis_connection():
    return redis.Redis(host='localhost', port=6379, db=0)