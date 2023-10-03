from lib.album import Album

"""
Artist constructs with an id, title, release year, artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Title", 9999, 1)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 9999
    assert album.id == 1

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Album", 9999, 1)
    assert str(album) == "Album(1, Test Album, 9999, 1)"

"""
We can compare two identical artists
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test Title", 9999, 1)
    album2 = Album(1, "Test Title", 9999, 1)
    assert album1 == album2