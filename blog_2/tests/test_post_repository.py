from lib.post import Post
from lib.post_repository import PostRepository

"""
When PostRepository#find_by_tag is called
A list of posts with given tag are returned
"""

def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)

    posts = repository.find_by_tag('education')

    assert posts == [Post(2, 'Fun classes'), Post(3, 'Using a REPL')]