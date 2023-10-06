from lib.order import Order
from lib.item import Item

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
    
    def find_with_items(self, order_id):
        rows = self._connection.execute('SELECT orders.id as order_id, ' \
                                        'orders.customer_name, orders.date_ordered, ' \
                                        'items.id as item_id, items.name, items.unit_price, ' \
                                        'items.quantity FROM orders ' \
                                        'JOIN items_orders ON items_orders.order_id = orders.id ' \
                                        'JOIN items ON items_orders.item_id = items.id ' \
                                        'WHERE orders.id = %s', [order_id])
        
        items = [Item(row['item_id'], row['name'], row['unit_price'], row['quantity']) 
                for row in rows]
        return Order(rows[0]['order_id'], rows[0]['customer_name'], str(rows[0]['date_ordered']), items)