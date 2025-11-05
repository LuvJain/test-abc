"""
Data models for the GraphQL API.
This module defines the core data models for the User, Post, Book, and Author entities.
"""

from datetime import datetime, date

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

class User:
    """
    User model representing a user of the application.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        created_at (datetime): The date and time when the user was created.
        bio (str, optional): A short biography of the user.
    """
    def __init__(self, id, username, email, created_at=None, bio=None):
        self.id = id
        self.username = username
        self.email = email
        self.created_at = created_at or datetime.now()
        self.bio = bio

class Post:
    """
    Post model representing a user's post.

    Attributes:
        id (int): The unique identifier for the post.
        title (str): The title of the post.
        content (str): The content of the post.
        author_id (int): The ID of the user who authored the post.
        created_at (datetime): The date and time when the post was created.
        updated_at (datetime): The date and time when the post was last updated.
        published (bool): Whether the post is published or still in draft.
        tags (list): A list of tags associated with the post.
    """
    def __init__(self, id, title, content, author_id, created_at=None, updated_at=None, published=True, tags=None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.published = published
        self.tags = tags or []

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

sample_users = [
    User(1, "john_doe", "john@example.com", datetime(2023, 1, 15), "Software developer and tech enthusiast"),
    User(2, "jane_smith", "jane@example.com", datetime(2023, 2, 20), "Digital artist and photographer"),
    User(3, "bob_johnson", "bob@example.com", datetime(2023, 3, 10), "Travel blogger and adventure seeker"),
    User(4, "alice_brown", "alice@example.com", datetime(2023, 4, 5), "Science writer and researcher")
]

sample_posts = [
    Post(1, "Getting Started with GraphQL", "This is a beginner's guide to GraphQL...", 1, datetime(2023, 5, 10), datetime(2023, 5, 10), True, ["GraphQL", "API", "Tutorial"]),
    Post(2, "Advanced GraphQL Techniques", "In this post, we'll explore advanced GraphQL features...", 1, datetime(2023, 6, 15), datetime(2023, 6, 20), True, ["GraphQL", "Advanced"]),
    Post(3, "My Travel Adventures", "Recently I visited the amazing landscapes of...", 3, datetime(2023, 7, 5), datetime(2023, 7, 5), True, ["Travel", "Adventure"]),
    Post(4, "Photography Tips", "Here are my top 10 photography tips for beginners...", 2, datetime(2023, 8, 12), datetime(2023, 8, 15), True, ["Photography", "Tutorial"]),
    Post(5, "The Future of AI", "Artificial intelligence is rapidly evolving...", 4, datetime(2023, 9, 1), datetime(2023, 9, 3), True, ["AI", "Technology", "Future"]),
    Post(6, "Draft: New Project Ideas", "Working on some new project ideas...", 1, datetime(2023, 10, 1), datetime(2023, 10, 1), False, ["Projects", "Ideas"])
]

# Helper functions for original models
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

# Helper functions for User and Post models
def get_user_by_id(id):
    """Get a user by their ID."""
    for user in sample_users:
        if user.id == id:
            return user
    return None

def get_post_by_id(id):
    """Get a post by its ID."""
    for post in sample_posts:
        if post.id == id:
            return post
    return None

def get_posts_by_user_id(user_id):
    """Get all posts written by a specific user."""
    return [post for post in sample_posts if post.author_id == user_id]

def get_all_users():
    """Get all users."""
    return sample_users

def get_all_posts(published_only=False):
    """
    Get all posts.

    Args:
        published_only (bool): If True, return only published posts.
    """
    if published_only:
        return [post for post in sample_posts if post.published]
    return sample_posts

def get_posts_by_tag(tag):
    """Get all posts with a specific tag."""
    return [post for post in sample_posts if tag in post.tags]

def get_posts_paginated(offset=0, limit=10, published_only=False):
    """
    Get posts with pagination support.

    Args:
        offset (int): The number of posts to skip.
        limit (int): The maximum number of posts to return.
        published_only (bool): If True, return only published posts.
    """
    posts = get_all_posts(published_only)
    return posts[offset:offset + limit]

def add_user(username, email, bio=None):
    """
    Add a new user.

    Args:
        username (str): The username of the user.
        email (str): The email address of the user.
        bio (str, optional): A short biography of the user.

    Returns:
        User: The newly created user.
    """
    new_id = max(user.id for user in sample_users) + 1
    new_user = User(new_id, username, email, datetime.now(), bio)
    sample_users.append(new_user)
    return new_user

def add_post(title, content, author_id, tags=None, published=True):
    """
    Add a new post.

    Args:
        title (str): The title of the post.
        content (str): The content of the post.
        author_id (int): The ID of the user who authored the post.
        tags (list, optional): A list of tags associated with the post.
        published (bool): Whether the post is published or still in draft.

    Returns:
        Post: The newly created post.
    """
    new_id = max(post.id for post in sample_posts) + 1
    now = datetime.now()
    new_post = Post(new_id, title, content, author_id, now, now, published, tags)
    sample_posts.append(new_post)
    return new_post

def update_post(id, title=None, content=None, tags=None, published=None):
    """
    Update an existing post.

    Args:
        id (int): The ID of the post to update.
        title (str, optional): The new title of the post.
        content (str, optional): The new content of the post.
        tags (list, optional): The new tags for the post.
        published (bool, optional): The new published status of the post.

    Returns:
        Post: The updated post or None if the post was not found.
    """
    post = get_post_by_id(id)
    if post is None:
        return None

    if title is not None:
        post.title = title
    if content is not None:
        post.content = content
    if tags is not None:
        post.tags = tags
    if published is not None:
        post.published = published

    post.updated_at = datetime.now()
    return post