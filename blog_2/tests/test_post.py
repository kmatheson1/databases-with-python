from lib.post import Post

def test_post_constructs():
    post = Post(1, "test title")
    assert post.id == 1
    assert post.title == "test title"

def test_equality():
    post1 = Post(1, "test title")
    post2 = Post(1, "test title")
    assert post1 == post2

def test_formats():
    post = Post(1, "test title")
    assert str(post) == 'Post(1, test title)'
