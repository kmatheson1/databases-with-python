from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users ORDER BY id ASC')
        return [
            User(row["id"], row["email_address"], row["username"]) for row in rows
        ]

    def find(self, id):
        rows = self._connection.execute('SELECT * from users WHERE id = %s ', [id])
        row = rows[0]
        return User(row["id"], row["email_address"], row["username"])
        
    def create(self, user):
        self._connection.execute('INSERT INTO users (email_address, username) VALUES (%s, %s)', [user.email_address, user.username])
        return None

    def delete(self, id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [id])
        return None

    def update(self, user):
        self._connection.execute(
            'UPDATE users SET email_address = %s, username = %s WHERE id = %s', 
            [user.email_address, user.username, user.id]
        )
        return None