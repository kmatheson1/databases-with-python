from lib.book_repository import BookRepository
from lib.book import Book

"""
When we call BookRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_get_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)

    books = repository.all()

    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
    ]

"""
len(books) # =>  5
"""
def test_len_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)

    books = repo.all()
    assert len(books) == 5

"""
books[0].id # =>  1
books[0].title # =>  'Nineteen Eighty-Four'
books[0].author_name # =>  'George Orwell'
"""
def test_access_books_index(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)

    books = repo.all()

    assert books[0].id == 1
    assert books[0].title == 'Nineteen Eighty-Four'
    assert books[0].author_name == 'George Orwell'