from lib.tag import Tag
from lib.tag_repository import TagRepository

"""
When tagRepository#find_by_tag is called
A list of tags with given tag are returned
"""

def test_find_by_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)

    tags = repository.find_by_post(6)

    assert tags == [Tag(2, 'travel'), Tag(3, 'cooking')]