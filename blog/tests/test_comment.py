from lib.comment import Comment

def test_comment_constructs():
    comment = Comment(1, "Name", "Contents", 1)
    assert comment.id == 1
    assert comment.name == "Name"
    assert comment.contents == "Contents"

def test_equality():
    comment1 = Comment(1, "Name", "Contents", 1)
    comment2 = Comment(1, "Name", "Contents", 1)
    assert comment1 == comment2

def test_formats():
    comment = Comment(1, "Name", "Contents", 1)
    assert str(comment) == 'Comment(1, Name, Contents, 1)'