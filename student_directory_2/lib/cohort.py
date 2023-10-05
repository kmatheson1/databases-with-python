from lib.student import Student

class Cohort():
    def __init__(self, id, name, starting_date, student = None):
        self.id = id
        self.name = name
        self. starting_date = str(starting_date)
        self.student = student or []

    def __eq__(self, other):
        if other is None:
            return False  # None objects are not equal to anything
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Cohort({self.id}, {self.name}, {self.starting_date})'