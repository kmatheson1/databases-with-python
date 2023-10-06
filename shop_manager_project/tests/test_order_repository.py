from lib.order_repository import OrderRepository
from lib.order import Order
from lib.item import Item
from datetime import date


"""
if OrderRepository#all is called
List of all orders from database returned
"""
def test_all(db_connection):
    db_connection.seed("seeds/shop_directory1.sql")
    repository = OrderRepository(db_connection)

    date_format = '%Y-%m-%d'

    orders = repository.all()
    assert orders == [
                    Order(1, 'Kieran', date(2023, 9, 10).strftime(date_format)),
                    Order(2, 'James', date(2023, 9, 11).strftime(date_format)),
                    Order(3, 'Jack', date(2023, 9, 12).strftime(date_format)),
                    Order(4, 'Jane', date(2023, 9, 11).strftime(date_format)),
                    Order(5, 'Leo', date(2023, 9, 10).strftime(date_format))
                    ]
    
"""
if OrderRepository#create is called
the order passed is added to the list
"""
def test_create(db_connection):
    db_connection.seed("seeds/shop_directory1.sql")
    repository = OrderRepository(db_connection)

    order = Order(customer_name='Hannah', date_ordered='11/30/2023', id=None)

    repository.create(order)

    date_format = '%Y-%m-%d'

    assert repository.all() == [
                    Order(1, 'Kieran', date(2023, 9, 10).strftime(date_format)),
                    Order(2, 'James', date(2023, 9, 11).strftime(date_format)),
                    Order(3, 'Jack', date(2023, 9, 12).strftime(date_format)),
                    Order(4, 'Jane', date(2023, 9, 11).strftime(date_format)),
                    Order(5, 'Leo', date(2023, 9, 10).strftime(date_format)),
                    Order(6, 'Hannah', date(2023, 11, 30).strftime(date_format))
                    ]

"""
If OrderRepository#findwithitems is called
the order with list of items is returned
"""
def test_find_with_items(db_connection):
    db_connection.seed("seeds/shop_directory1.sql")
    repository = OrderRepository(db_connection)

    date_format = '%Y-%m-%d'

    order = repository.find_with_items(1)
    assert order == Order(1, 'Kieran', date(2023, 9, 10).strftime(date_format), [
        Item(1, 'Banana', 0.8, 30),
        Item(2, 'Apple', 0.9, 20),
        Item(4, 'Orange Juice', 1.8, 10)
    ])