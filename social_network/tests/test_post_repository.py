from lib.post import Post
from lib.post_repository import PostRepository

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    posts = repository.all()

    assert posts == [
        Post(1,'Man Of The East', 'test post content 1', 100, 1),
        Post(2,'Invader Of Rainbows', 'test post content 2', 50, 1),
        Post(3,'Spiders Of Time', 'test post content 3', 20, 2),
        Post(4,'Cats Of Utopia', 'test post content 4', 20, 3),
        Post(5,'Butchers And Priests', 'test post content 5', 10, 3),
        Post(6,'Kings And Criminals', 'test post content 6', 100, 3),
        Post(7,'Extinction Of The Gods', 'test post content 7', 50, 4),
        Post(8,'Disruption With Vigor', 'test post content 8', 20, 5),
        Post(9,'Leading The Hunter', 'test post content 9', 20, 5),
        Post(10,'Traces In The Graveyard', 'test post content 10', 20, 6)
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    result = repository.find(1)

    assert result == Post(1,'Man Of The East', 'test post content 1', 100, 1)

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = Post(None, "Title", "Contents", 3, 1)
    repository.create(post)
    assert repository.all() == [
        Post(1,'Man Of The East', 'test post content 1', 100, 1),
        Post(2,'Invader Of Rainbows', 'test post content 2', 50, 1),
        Post(3,'Spiders Of Time', 'test post content 3', 20, 2),
        Post(4,'Cats Of Utopia', 'test post content 4', 20, 3),
        Post(5,'Butchers And Priests', 'test post content 5', 10, 3),
        Post(6,'Kings And Criminals', 'test post content 6', 100, 3),
        Post(7,'Extinction Of The Gods', 'test post content 7', 50, 4),
        Post(8,'Disruption With Vigor', 'test post content 8', 20, 5),
        Post(9,'Leading The Hunter', 'test post content 9', 20, 5),
        Post(10,'Traces In The Graveyard', 'test post content 10', 20, 6),
        Post(11, "Title", "Contents", 3, 1)
    ]

# def test_delete(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = PostRepository(db_connection)
#     repository.delete(1)
#     assert repository.all() == [
#         Post(2,'Invader Of Rainbows', 'test post content 2', 50, 1),
#         Post(3,'Spiders Of Time', 'test post content 3', 20, 2),
#         Post(4,'Cats Of Utopia', 'test post content 4', 20, 3),
#         Post(5,'Butchers And Priests', 'test post content 5', 10, 3),
#         Post(6,'Kings And Criminals', 'test post content 6', 100, 3),
#         Post(7,'Extinction Of The Gods', 'test post content 7', 50, 4),
#         Post(8,'Disruption With Vigor', 'test post content 8', 20, 5),
#         Post(9,'Leading The Hunter', 'test post content 9', 20, 5),
#         Post(10,'Traces In The Graveyard', 'test post content 10', 20, 6)
#     ]

def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    print(repository.all())
    post = repository.find(1)
    print(repository.all())
    post.title = "Rainbows"
    assert repository.update(post) is None
    print(repository.all())
    assert repository.all() == [
        Post(1,'Rainbows', 'test post content 1', 100, 1),
        Post(2,'Invader Of Rainbows', 'test post content 2', 50, 1),
        Post(3,'Spiders Of Time', 'test post content 3', 20, 2),
        Post(4,'Cats Of Utopia', 'test post content 4', 20, 3),
        Post(5,'Butchers And Priests', 'test post content 5', 10, 3),
        Post(6,'Kings And Criminals', 'test post content 6', 100, 3),
        Post(7,'Extinction Of The Gods', 'test post content 7', 50, 4),
        Post(8,'Disruption With Vigor', 'test post content 8', 20, 5),
        Post(9,'Leading The Hunter', 'test post content 9', 20, 5),
        Post(10,'Traces In The Graveyard', 'test post content 10', 20, 6),
    ]




