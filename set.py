from classes import helper

if __name__ == '__main__':
    connection = helper.get_redis_connection()
    connection.set('cabbage_qty', 10)

    print(connection.get('cabbage_qty'))
