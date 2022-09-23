from classes import helper

if __name__ == '__main__':
    connection = helper.get_redis_connection()
    channel = connection.pubsub()
    print(channel.subscribe('category_groceries'))
    print(channel.get_message())
