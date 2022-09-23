from classes import helper

if __name__ == '__main__':
    connection = helper.get_redis_connection()
    connection.publish('category_groceries', 'apples are back in stock')
    connection.publish('category_groceries', '5% discount to fruits')
