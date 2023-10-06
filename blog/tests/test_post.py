from lib.post import Post

def test_post_constructs():
    post = Post(1, "Title", "Contents")
    assert post.id == 1
    assert post.name == "Title"
    assert post.contents == "Contents"

def test_equality():
    post1 = Post(1, "Title", "Contents")
    post2 = Post(1, "Title", "Contents")
    assert post1 == post2

def test_formats():
    post = Post(1, "Title", "Contents")
    assert str(post) == 'Post(1, Title, Contents)'