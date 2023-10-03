from lib.book import Book

"""
Book constructs with id, title, author name
"""
def test_book_constructs():
    books = Book(1, "Test Title", "Test Author Name")
    assert books.id == 1
    assert books.title == "Test Title"
    assert books.author_name == "Test Author Name"

"""
We can compare two identical books
And have them as equal
"""
def test_books_are_equal():
    book1 = Book(1, "Test Title", "Test Author")
    book2 = Book(1, "Test Title", "Test Author")
    assert book1 == book2

"""
We can format the books to strings that can be printed
"""
def test_books_format_as_expected():
    book = Book(1, "Test Title", "Test Author")
    assert str(book) == "1 - Test Title - Test Author"