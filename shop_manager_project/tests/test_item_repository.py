from lib.item_repository import ItemRepository
from lib.item import Item

"""
if ItemRepository#all is called
List of all items from database returned
"""
def test_all(db_connection):
    db_connection.seed("seeds/shop_directory1.sql")
    repository = ItemRepository(db_connection)

    items = repository.all()
    assert items == [
                        Item(1, 'Banana', 0.8, 30),
                        Item(2, 'Apple', 0.9, 20),
                        Item(3, 'White Bread', 1.5, 15),
                        Item(4, 'Orange Juice', 1.8, 10),
                        Item(5, 'Apple Juice', 1.8, 12),
                        Item(6, 'Wine', 6, 30),
                        Item(7, 'Beer', 3.2, 60)
            ]
    
"""
if ItemRepository#create is called
the item passed is added to the list
"""
def test_create(db_connection):
    db_connection.seed("seeds/shop_directory1.sql")
    repository = ItemRepository(db_connection)

    item = Item(name='Burgers', unit_price=2.5, quantity=10, id=None)

    repository.create(item)

    assert repository.all() == [
                        Item(1, 'Banana', 0.8, 30),
                        Item(2, 'Apple', 0.9, 20),
                        Item(3, 'White Bread', 1.5, 15),
                        Item(4, 'Orange Juice', 1.8, 10),
                        Item(5, 'Apple Juice', 1.8, 12),
                        Item(6, 'Wine', 6, 30),
                        Item(7, 'Beer', 3.2, 60),
                        Item(8, 'Burgers', 2.5, 10)
            ]