from lib.post_repository import PostRepository
from lib.post import Post
from lib.comment import Comment

"""
If we call post#find_with_comments
returns a post and comments with one query
"""
def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blog_posts_comments.sql")
    repository = PostRepository(db_connection)

    post = repository.find_with_comments(1)
    assert post == Post(1,'James', 'Hello World', [
        Comment(1, 'Kieran', 'Hello', 1), Comment(2, 'Jane', 'Nice', 1)
    ])