from lib.item import Item

def test_item_constructs():
    item = Item(1, "test name", 1.2, 20)
    assert item.id == 1
    assert item.name == "test name"
    assert item.unit_price == 1.2
    assert item.quantity == 20

def test_equality():
    item1 = Item(1, "test name", 1.2, 20)
    item2 = Item(1, "test name", 1.2, 20)
    assert item1 == item2

def test_formats():
    item = Item(1, "test name", 1.2, 20)
    assert str(item) == 'Item(1, test name, 1.2, 20)'