

class Recipe:
    def __init__(self, id, title, avg_cooking_time_mins, rating):
        self.id = id
        self.title = title
        self.avg_cooking_time_mins = avg_cooking_time_mins
        self.rating = rating

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Recipe({self.id}, {self.title}, {self.avg_cooking_time_mins}, {self.rating})'