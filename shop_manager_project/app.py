from lib.database_connection import DatabaseConnection
from lib.order_repository import OrderRepository
from lib.item_repository import ItemRepository


class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/shop_directory1.sql")

    def run(self):
        # order_repository = OrderRepository(self._connection)
        # item_repository = ItemRepository(self._connection)
        
        while True:
            print('\nWelcome to the shop management program!')
            print('\nWhat do you want to do?')
            print('  1 = list all shop items')
            print('  2 = create a new item')
            print('  3 = list all orders')
            print('  4 = create a new order')

            choice = input('\nEnter your choice: ')

            if choice == '1':
                item_repository = ItemRepository(self._connection)
                print('\nHere\'s a list of all shop items:\n')
                for item in item_repository.all():
                    print(f'{item.name.capitalize()} - Unit Price: {item.unit_price} - Quantity: {item.quantity}')

            if choice == 2:
                break

            if choice == 3:
                break

            if choice == 4:
                break

            break

if __name__ == '__main__':
    app = Application()
    app.run()
