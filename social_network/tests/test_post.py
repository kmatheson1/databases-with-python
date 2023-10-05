from lib.post import Post

def test_constructs():
    post = Post(1, "Test", "Test Contents", 3, 1)
    assert post.id ==1
    assert post.title == "Test"
    assert post.contents == "Test Contents"
    assert post.views == 3
    assert post.user_id == 1

def test_equality():
    post1 = Post(1, "Test", "Test Contents", 3, 1)
    post2 = Post(1, "Test", "Test Contents", 3, 1)
    assert post1 == post2