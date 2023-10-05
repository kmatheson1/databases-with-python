from lib.user import User

"""
Constructs with a username and emial address
"""
def test_constructs():
    user = User(1, "Test Email", "Test Username")
    assert user.id == 1
    assert user.email_address == "Test Email"
    assert user.username == "Test Username"