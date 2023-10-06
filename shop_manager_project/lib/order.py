
class Order():
    def __init__(self, id, customer_name, date_ordered, items = []):
        self.id = id
        self.customer_name = customer_name
        self.date_ordered = date_ordered
        self.items = items

    def __eq__(self, other):
        if other == None:
            return False
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Order({self.id}, {self.customer_name}, {self.date_ordered})'