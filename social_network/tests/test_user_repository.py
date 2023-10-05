from lib.user import User
from lib.user_repository import UserRepository

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user_names = repository.all()

    assert user_names == [
        User(1, 'boomzilla@aol.com', 'capacity'),
        User(2, 'microfab@gmail.com', 'skirt'),
        User(3, 'ilikered@mac.com', 'hefty'),
        User(4, 'schumer@mac.com', 'bob'),
        User(5, 'podmaster@live.com', 'ladder'),
        User(6, 'smartfart@hotmail.com', 'delight'),
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    result = repository.find(1)

    assert result == User(1, 'boomzilla@aol.com', 'capacity')


def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = User(None, "test@test.net", "test")
    repository.create(user)
    assert repository.all() == [
        User(1, 'boomzilla@aol.com', 'capacity'),
        User(2, 'microfab@gmail.com', 'skirt'),
        User(3, 'ilikered@mac.com', 'hefty'),
        User(4, 'schumer@mac.com', 'bob'),
        User(5, 'podmaster@live.com', 'ladder'),
        User(6, 'smartfart@hotmail.com', 'delight'),
        User(7, "test@test.net", "test")
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(1)
    assert repository.all() == [
        User(2, 'microfab@gmail.com', 'skirt'),
        User(3, 'ilikered@mac.com', 'hefty'),
        User(4, 'schumer@mac.com', 'bob'),
        User(5, 'podmaster@live.com', 'ladder'),
        User(6, 'smartfart@hotmail.com', 'delight'),
    ]

def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    print(repository.all())
    user = repository.find(1)
    print(repository.all())
    user.username = "Rainbows"
    assert repository.update(user) is None
    print(repository.all())
    assert repository.all() == [
        User(1, 'boomzilla@aol.com', 'Rainbows'),
        User(2, 'microfab@gmail.com', 'skirt'),
        User(3, 'ilikered@mac.com', 'hefty'),
        User(4, 'schumer@mac.com', 'bob'),
        User(5, 'podmaster@live.com', 'ladder'),
        User(6, 'smartfart@hotmail.com', 'delight'),
    ]


