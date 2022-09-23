from classes import helper

if __name__ == '__main__':
    print(helper.get_redis_connection().smembers('vegetables_instock'))
