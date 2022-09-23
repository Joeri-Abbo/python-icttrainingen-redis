
import redis

quick24X7 = redis.Redis(host='localhost', port=6379, db=0)
if __name__ == '__main__':
    print(quick24X7.get('cabbage_qty'))
