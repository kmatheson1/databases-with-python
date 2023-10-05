from lib.post import Post

class PostRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from posts ORDER BY id ASC')
        return [Post(row["id"], row["title"], row["contents"], row["views"], row["user_id"]) for row in rows] 
    
    def find(self, id):
        rows = self._connection.execute('SELECT * from posts WHERE id = %s', [id])
        row = rows[0]
        return Post(row["id"], row["title"], row["contents"], row["views"], row["user_id"])
    
    def create(self, post):
        self._connection.execute('INSERT INTO posts (title, contents, views, user_id) VALUES (%s, %s, %s, %s)', [post.title, post.contents, post.views, post.user_id])
        return None
    
    def delete(self, id):
        self._connection.execute('DELETE from posts WHERE id = %s', [id])
        return None
    
    def update(self, post):
        self._connection.execute(
            'UPDATE posts SET title = %s, contents = %s, views = %s, user_id = %s WHERE id = %s', 
            [post.title, post.contents, post.views, post.user_id, post.id]
        )
        return None
