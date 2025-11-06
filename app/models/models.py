"""
Data models for the GraphQL API.
This module defines the core data models for the User, Post, Book, and Author entities.
"""

import logging
import os
import bcrypt
import jwt
from datetime import datetime, date, timedelta
from enum import Enum

# Configure logging for authentication events
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('auth')

# JWT configuration
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'super-secret-key-for-jwt')  # In production, use environment variable
JWT_ALGORITHM = 'HS256'
JWT_EXPIRATION_DELTA = timedelta(days=1)  # Token expiration time

class UserRole(Enum):
    """Enum for user roles with different permission levels."""
    ADMIN = "admin"      # Full access to all resources
    EDITOR = "editor"    # Can create and edit own content, edit others
    AUTHOR = "author"    # Can create and edit own content
    READER = "reader"    # Read-only access

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
        password_hash (str): The hashed password of the user.
        role (UserRole): The role of the user (admin, editor, author, reader).
        created_at (datetime): The date and time when the user was created.
        bio (str, optional): A short biography of the user.
        last_login (datetime, optional): The last time the user logged in.
    """
    def __init__(self, id, username, email, password_hash=None, role=UserRole.READER,
                 created_at=None, bio=None, last_login=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.created_at = created_at or datetime.now()
        self.bio = bio
        self.last_login = last_login

    def check_password(self, password):
        """Check if the provided password matches the stored password hash."""
        if not self.password_hash:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def generate_auth_token(self):
        """Generate a JWT token for this user."""
        payload = {
            'user_id': self.id,
            'username': self.username,
            'role': self.role.value,
            'exp': datetime.utcnow() + JWT_EXPIRATION_DELTA
        }
        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
        logger.info(f"Generated token for user {self.username} (ID: {self.id})")
        return token

    @staticmethod
    def hash_password(password):
        """Hash a password using bcrypt."""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

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

# Create sample users with predefined password hashes (in real app, these would be properly generated)
sample_users = [
    User(1, "john_doe", "john@example.com",
         User.hash_password("password123"),
         UserRole.ADMIN,
         datetime(2023, 1, 15), "Software developer and tech enthusiast"),
    User(2, "jane_smith", "jane@example.com",
         User.hash_password("password123"),
         UserRole.EDITOR,
         datetime(2023, 2, 20), "Digital artist and photographer"),
    User(3, "bob_johnson", "bob@example.com",
         User.hash_password("password123"),
         UserRole.AUTHOR,
         datetime(2023, 3, 10), "Travel blogger and adventure seeker"),
    User(4, "alice_brown", "alice@example.com",
         User.hash_password("password123"),
         UserRole.READER,
         datetime(2023, 4, 5), "Science writer and researcher")
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

def add_user(username, email, password, role=UserRole.READER, bio=None):
    """
    Add a new user.

    Args:
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The plain text password (will be hashed).
        role (UserRole, optional): The role of the user. Defaults to UserRole.READER.
        bio (str, optional): A short biography of the user.

    Returns:
        User: The newly created user.
    """
    # Hash the password
    password_hash = User.hash_password(password)

    # Create a new user ID
    new_id = max(user.id for user in sample_users) + 1

    # Create the user
    new_user = User(
        id=new_id,
        username=username,
        email=email,
        password_hash=password_hash,
        role=role,
        created_at=datetime.now(),
        bio=bio
    )

    # Add user to the sample data
    sample_users.append(new_user)
    logger.info(f"Created new user: {username} (ID: {new_id}) with role: {role.value}")

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

# Authentication and authorization functions
def authenticate_user(username, password):
    """
    Authenticate a user by username and password.

    Args:
        username (str): The username of the user to authenticate.
        password (str): The password to check.

    Returns:
        User: The authenticated user or None if authentication failed.
    """
    # Find user by username
    for user in sample_users:
        if user.username == username:
            # Check password
            if user.check_password(password):
                # Log successful login
                logger.info(f"User {username} (ID: {user.id}) authenticated successfully")
                # Update last login time
                user.last_login = datetime.now()
                return user
            else:
                # Log failed login
                logger.warning(f"Failed login attempt for user: {username}")
                return None

    # Log invalid username
    logger.warning(f"Login attempt with invalid username: {username}")
    return None

def get_user_by_token(token):
    """
    Validate a JWT token and return the corresponding user.

    Args:
        token (str): The JWT token to validate.

    Returns:
        User: The user associated with the token or None if the token is invalid.
    """
    try:
        # Decode the token
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])

        # Get the user_id from the payload
        user_id = payload.get('user_id')

        # Find the user
        user = get_user_by_id(user_id)

        if user:
            logger.info(f"Token validated for user: {user.username} (ID: {user.id})")
            return user
        else:
            logger.warning(f"Token contains unknown user ID: {user_id}")
            return None

    except jwt.ExpiredSignatureError:
        # Token has expired
        logger.warning("Expired token used for authentication")
        return None
    except jwt.InvalidTokenError:
        # Invalid token
        logger.warning("Invalid token used for authentication")
        return None

def login_user(username, password):
    """
    Login a user and generate a JWT token.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        tuple: (token, user) if authentication succeeds, (None, None) otherwise
    """
    # Authenticate user
    user = authenticate_user(username, password)

    if user:
        # Generate a token
        token = user.generate_auth_token()
        return token, user

    return None, None

def user_can_modify_post(user, post):
    """
    Check if a user has permission to modify a post.

    Args:
        user (User): The user requesting the modification.
        post (Post): The post to be modified.

    Returns:
        bool: True if the user has permission, False otherwise.
    """
    # Admins can modify any post
    if user.role == UserRole.ADMIN:
        return True

    # Editors can modify any post
    if user.role == UserRole.EDITOR:
        return True

    # Authors can only modify their own posts
    if user.role == UserRole.AUTHOR and post.author_id == user.id:
        return True

    # Log unauthorized attempt
    logger.warning(f"Unauthorized modification attempt: User {user.username} (ID: {user.id}) tried to modify post {post.id} by user {post.author_id}")

    # Default is to deny access
    return False