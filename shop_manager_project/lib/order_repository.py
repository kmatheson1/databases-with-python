from lib.order import Order

class OrderRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM orders')
        return [Order(row['id'], row['customer_name'], str(row['date_ordered'])) for row in rows]
    
    def create(self, order):
        self._connection.execute('INSERT INTO orders (customer_name, date_ordered) ' \
                                'VALUES (%s, %s)', [order.customer_name, order.date_ordered])
        return None