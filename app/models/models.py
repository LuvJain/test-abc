"""
Data models for the GraphQL API.
This module defines the core data models for the Book and Author entities.
"""

class Author:
    """
    Author model representing a book author.

    Attributes:
        id (int): The unique identifier for the author.
        name (str): The name of the author.
        birth_date (str): The birth date of the author in ISO format.
    """
    def __init__(self, id, name, birth_date):
        self.id = id
        self.name = name
        self.birth_date = birth_date

class Book:
    """
    Book model representing a book in the library.

    Attributes:
        id (int): The unique identifier for the book.
        title (str): The title of the book.
        author_id (int): The ID of the author of the book.
        publication_year (int): The year the book was published.
        genre (str): The genre of the book.
    """
    def __init__(self, id, title, author_id, publication_year, genre):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.publication_year = publication_year
        self.genre = genre

# Sample data for demonstration purposes
sample_authors = [
    Author(1, "J.K. Rowling", "1965-07-31"),
    Author(2, "George Orwell", "1903-06-25"),
    Author(3, "J.R.R. Tolkien", "1892-01-03")
]

sample_books = [
    Book(1, "Harry Potter and the Philosopher's Stone", 1, 1997, "Fantasy"),
    Book(2, "1984", 2, 1949, "Dystopian"),
    Book(3, "Animal Farm", 2, 1945, "Political Satire"),
    Book(4, "The Hobbit", 3, 1937, "Fantasy"),
    Book(5, "The Lord of the Rings", 3, 1954, "Fantasy")
]

# Helper functions to retrieve data
def get_author_by_id(id):
    """Get an author by their ID."""
    for author in sample_authors:
        if author.id == id:
            return author
    return None

def get_book_by_id(id):
    """Get a book by its ID."""
    for book in sample_books:
        if book.id == id:
            return book
    return None

def get_books_by_author_id(author_id):
    """Get all books written by a specific author."""
    return [book for book in sample_books if book.author_id == author_id]

def get_all_books():
    """Get all books."""
    return sample_books

def get_all_authors():
    """Get all authors."""
    return sample_authors