
class Post():
    def __init__(self, id, name, contents, comments = None):
        self.id = id
        self.name = name
        self.contents = contents
        self.comments = comments or []

    def __eq__(self, other):
        if other is None:
            return False
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Post({self.id}, {self.name}, {self.contents})'