from lib.item import Item

class ItemRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM items')
        return [Item(row['id'], row['name'], row['unit_price'], row['quantity']) for row in rows]

    def create(self, item):
        self._connection.execute('INSERT INTO items (name, unit_price, quantity) ' \
                                'VALUES (%s, %s, %s)', [item.name, item.unit_price, item.quantity])
        return None