
class Post():
    def __init__(self, id, title, contents):
        self.id = id
        self.title = title
        self.contents = contents

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Post({self.id}, {self.title}, {self.contents})'