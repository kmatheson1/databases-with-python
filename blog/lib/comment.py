
class Comment():
    def __init__(self, id, name, contents, post_id):
        self.id = id
        self.name = name
        self.contents = contents
        self.post_id = post_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Comment({self.id}, {self.name}, {self.contents}, {self.post_id})'