from lib.tag import Tag

def test_tag_constructs():
    tag = Tag(1, "test name")
    assert tag.id == 1
    assert tag.name == "test name"

def test_equality():
    tag1 = Tag(1, "test name")
    tag2 = Tag(1, "test name")
    assert tag1 == tag2

def test_formats():
    tag = Tag(1, "test name")
    assert str(tag) == 'Tag(1, test name)'
