from lib.database_connection import DatabaseConnection
from lib.order_repository import OrderRepository
from lib.item_repository import ItemRepository
from lib.item import Item
from lib.order import Order
from datetime import date


class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/shop_directory1.sql")

    def run(self):
        # order_repository = OrderRepository(self._connection)
        # item_repository = ItemRepository(self._connection)
        print('\nWelcome to the shop management program!')
        while True:

            print('\nWhat do you want to do?')
            print('  1 = list all shop items')
            print('  2 = create a new item')
            print('  3 = list all orders')
            print('  4 = create a new orde5')
            print('  5 = exit')


            choice = input('\nEnter your choice: ')

            if choice == '1':
                item_repository = ItemRepository(self._connection)
                print('\nHere\'s a list of all shop items:\n')
                for item in item_repository.all():
                    print(f'{item.name} - Unit Price: {item.unit_price} - Quantity: {item.quantity}')

            if choice == '2':
                item_repository = ItemRepository(self._connection)
                item_name = input('\nItem Name: ')
                unit_price = input('\nPrice: ')
                quantity = input('\nAmmount in Stock: ')
                new_item = Item(None, item_name, unit_price, quantity)
                item_repository.create(new_item)


            if choice == '3':
                order_repository = OrderRepository(self._connection)
                print('\nHere\'s a list of all shop orders:\n')
                for item in order_repository.all():
                    print(f'Customer Name: {item.customer_name}  Date Ordered: {item.date_ordered}')

            if choice == '4':
                order_repository = OrderRepository(self._connection)
                customer_name = input('\nName: ')
                new_order = Order(None, customer_name, date.today())
                order_repository.create(new_order)

            if choice == '5':
                break

if __name__ == '__main__':
    app = Application()
    app.run()
