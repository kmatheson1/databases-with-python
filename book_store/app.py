from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository

#Test Examples

connection = DatabaseConnection()
connection.connect()

repo = BookRepository(connection)

books = repo.all()

for book in books:
    print(book)

