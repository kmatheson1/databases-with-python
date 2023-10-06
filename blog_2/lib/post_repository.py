from lib.post import Post

class PostRepository():
    def __init__(self, connection):
        self._connection = connection

    def find_by_tag(self, tag):
        rows = self._connection.execute('SELECT posts.id, posts.title ' \
	                                    'FROM posts ' \
		                                'JOIN posts_tags ON posts_tags.post_id = posts.id ' \
		                                'JOIN tags ON posts_tags.tag_id = tags.id ' \
		                                'WHERE tags.name = %s', [tag])
        return [Post(row['id'], row['title']) for row in rows]