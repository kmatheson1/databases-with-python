from lib.post import Post
from lib.comment import Comment

class PostRepository():
    def __init__(self, connection):
        self._connection = connection

    def find_with_comments(self, post_id):
        rows = self._connection.execute('SELECT posts.id as post_id, posts.name, ' \
                                        'posts.contents, comments.id as comment_id, ' \
                                        'comments.name as comment_name, comments.contents as comment_contents FROM posts ' \
                                        'JOIN comments ON posts.id = comments.post_id ' \
                                        'WHERE posts.id = %s', [post_id])
        comments = []
        for row in rows:
            comment = Comment(row['comment_id'], row['comment_name'], row['comment_contents'], row['post_id'])
            comments.append(comment)
        print(comments)
        return Post(rows[0]["post_id"], rows[0]['name'], rows[0]['contents'], comments)
