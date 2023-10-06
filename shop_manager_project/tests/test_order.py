from lib.order import Order

def test_order_constructs():
    order = Order(1, "test name", '09/10/2023')
    assert order.id == 1
    assert order.customer_name == "test name"
    assert order.date_ordered == '09/10/2023'
    

def test_equality():
    order1 = Order(1, "test name", '09/10/2023')
    order2 = Order(1, "test name", '09/10/2023')
    assert order1 == order2

def test_formats():
    order = Order(1, "test name", '09/10/2023')
    assert str(order) == 'Order(1, test name, 09/10/2023)'