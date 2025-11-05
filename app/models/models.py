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
        profile_image (str, optional): URL to user's profile image.
        location (str, optional): User's geographical location.
        website (str, optional): User's website URL.
        is_verified (bool): Whether the user's account is verified.
        followers_count (int): Number of followers.
        following_count (int): Number of users being followed.
    """
    def __init__(self, id, username, email, password_hash=None, role=UserRole.READER,
                 created_at=None, bio=None, last_login=None, profile_image=None,
                 location=None, website=None, is_verified=False,
                 followers_count=0, following_count=0):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.created_at = created_at or datetime.now()
        self.bio = bio
        self.last_login = last_login
        self.profile_image = profile_image
        self.location = location
        self.website = website
        self.is_verified = is_verified
        self.followers_count = followers_count
        self.following_count = following_count

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
        summary (str): A short summary of the post content.
        author_id (int): The ID of the user who authored the post.
        created_at (datetime): The date and time when the post was created.
        updated_at (datetime): The date and time when the post was last updated.
        published (bool): Whether the post is published or still in draft.
        tags (list): A list of tags associated with the post.
        category (str): The category of the post.
        likes_count (int): Number of likes the post has received.
        comments_count (int): Number of comments on the post.
        featured_image (str): URL to the featured image for the post.
        read_time (int): Estimated reading time in minutes.
        slug (str): URL-friendly version of the title.
    """
    def __init__(self, id, title, content, author_id, created_at=None, updated_at=None,
                 published=True, tags=None, summary=None, category=None,
                 likes_count=0, comments_count=0, featured_image=None,
                 read_time=None, slug=None):
        self.id = id
        self.title = title
        self.content = content
        self.summary = summary or (content[:100] + '...' if len(content) > 100 else content)
        self.author_id = author_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.published = published
        self.tags = tags or []
        self.category = category
        self.likes_count = likes_count
        self.comments_count = comments_count
        self.featured_image = featured_image
        # Estimate read time if not provided: average person reads about 200 words per minute
        self.read_time = read_time or max(1, len(content.split()) // 200)
        # Create slug from title if not provided
        self.slug = slug or title.lower().replace(' ', '-')

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
         datetime(2023, 1, 15), "Software developer and tech enthusiast",
         datetime(2023, 11, 1), "https://example.com/john.jpg",
         "San Francisco, CA", "https://johndoe.dev", True, 120, 45),
    User(2, "jane_smith", "jane@example.com",
         User.hash_password("password123"),
         UserRole.EDITOR,
         datetime(2023, 2, 20), "Digital artist and photographer",
         datetime(2023, 10, 25), "https://example.com/jane.jpg",
         "New York, NY", "https://janesmith.art", True, 350, 210),
    User(3, "bob_johnson", "bob@example.com",
         User.hash_password("password123"),
         UserRole.AUTHOR,
         datetime(2023, 3, 10), "Travel blogger and adventure seeker",
         datetime(2023, 11, 2), "https://example.com/bob.jpg",
         "Austin, TX", "https://bobtravels.com", False, 75, 120),
    User(4, "alice_brown", "alice@example.com",
         User.hash_password("password123"),
         UserRole.READER,
         datetime(2023, 4, 5), "Science writer and researcher",
         datetime(2023, 10, 30), "https://example.com/alice.jpg",
         "Seattle, WA", "https://alicescience.org", True, 250, 180)
]

full_graphql_content = """This is a beginner's guide to GraphQL. In this comprehensive tutorial, we'll explore the fundamentals of GraphQL, how it differs from REST APIs, and how to build your first GraphQL server.

GraphQL is a query language for APIs and a runtime for executing those queries against your data. It was developed by Facebook in 2012 and released as an open-source project in 2015. Unlike REST, GraphQL allows clients to request exactly the data they need, making it possible to fetch all required data in a single request.

Key concepts we'll cover:
1. Schemas and types
2. Queries and mutations
3. Resolvers
4. GraphQL clients
5. Best practices and common patterns

Let's get started with setting up a basic GraphQL server using Python and Graphene."""

full_advanced_graphql = """In this post, we'll explore advanced GraphQL features and techniques that will help you build more robust and efficient APIs. We'll go beyond the basics and dive into real-world scenarios that require sophisticated solutions.

Topics covered:
1. Implementing authentication and authorization
2. Optimizing performance with dataloader
3. Managing GraphQL subscriptions for real-time features
4. Error handling patterns
5. Schema stitching and federation
6. Testing GraphQL APIs
7. Monitoring and metrics

Each section includes practical code examples and best practices from production environments."""

full_travel_content = """Recently I visited the amazing landscapes of Patagonia, where the mountains meet glaciers and the wilderness stretches as far as the eye can see. This trip was a photographer's dream and an adventurer's paradise.

My journey began in El Calafate, Argentina, where I witnessed the massive Perito Moreno Glacier. The crackling sounds of the ice and the occasional dramatic calving events left me in awe of nature's power. From there, I trekked through Torres del Paine National Park in Chile, navigating the famous W Circuit over 5 challenging but rewarding days.

The highlight was watching the sunrise cast its golden light on the granite towers that give the park its name. Despite the unpredictable weather and physically demanding hikes, every moment spent in this pristine wilderness was worth it."""

full_photography_content = """Here are my top 10 photography tips for beginners that will immediately improve your photos, regardless of what camera you're using:

1. Master the exposure triangle: Understand how aperture, shutter speed, and ISO work together
2. Follow the rule of thirds: Place important elements along the grid lines or at their intersections
3. Find good light: Photography is all about light, so learn to recognize quality light
4. Change your perspective: Don't just shoot from eye level
5. Focus on composition: Pay attention to what you include in the frame
6. Understand depth of field: Control which parts of your image are in focus
7. Invest time in post-processing: Learn basic editing techniques
8. Practice with different focal lengths: Understand how they affect your image
9. Capture the decisive moment: Anticipate and be ready for the perfect timing
10. Shoot in RAW: Give yourself more flexibility in post-processing

The most important tip? Practice consistently and analyze your results."""

full_ai_content = """Artificial intelligence is rapidly evolving, transforming industries and reshaping our daily lives. From self-driving cars to personalized medicine, AI technologies are creating unprecedented possibilities while raising important ethical questions.

Recent breakthroughs in large language models like GPT-4 and multimodal models that can process text, images, and audio simultaneously have accelerated AI adoption. These advances are enabling more natural human-computer interactions and more sophisticated problem-solving capabilities.

Looking ahead, researchers are focusing on developing more energy-efficient AI systems, improving interpretability and transparency, and addressing bias in training data. The concept of artificial general intelligence (AGI) remains a long-term goal, though opinions vary widely on when or if it will be achieved.

As AI becomes more integrated into critical systems, establishing robust governance frameworks and ethical guidelines becomes increasingly important. Balancing innovation with responsible development will be key to realizing AI's potential to address global challenges."""

sample_posts = [
    Post(
        id=1,
        title="Getting Started with GraphQL",
        content=full_graphql_content,
        author_id=1,
        created_at=datetime(2023, 5, 10),
        updated_at=datetime(2023, 5, 10),
        published=True,
        tags=["GraphQL", "API", "Tutorial"],
        summary="A comprehensive beginner's guide to GraphQL, covering fundamentals and how to build your first GraphQL server.",
        category="Programming",
        likes_count=145,
        comments_count=32,
        featured_image="https://example.com/images/graphql-intro.png",
        read_time=7,
        slug="getting-started-with-graphql"
    ),
    Post(
        id=2,
        title="Advanced GraphQL Techniques",
        content=full_advanced_graphql,
        author_id=1,
        created_at=datetime(2023, 6, 15),
        updated_at=datetime(2023, 6, 20),
        published=True,
        tags=["GraphQL", "Advanced", "Performance"],
        summary="Dive deep into advanced GraphQL features including authentication, performance optimization, and real-time subscriptions.",
        category="Programming",
        likes_count=87,
        comments_count=24,
        featured_image="https://example.com/images/advanced-graphql.png",
        read_time=12,
        slug="advanced-graphql-techniques"
    ),
    Post(
        id=3,
        title="My Travel Adventures in Patagonia",
        content=full_travel_content,
        author_id=3,
        created_at=datetime(2023, 7, 5),
        updated_at=datetime(2023, 7, 5),
        published=True,
        tags=["Travel", "Adventure", "Photography", "Patagonia"],
        summary="A journey through the breathtaking landscapes of Patagonia, from massive glaciers to stunning mountain peaks.",
        category="Travel",
        likes_count=210,
        comments_count=45,
        featured_image="https://example.com/images/patagonia.jpg",
        read_time=8,
        slug="travel-adventures-patagonia"
    ),
    Post(
        id=4,
        title="Photography Tips for Beginners",
        content=full_photography_content,
        author_id=2,
        created_at=datetime(2023, 8, 12),
        updated_at=datetime(2023, 8, 15),
        published=True,
        tags=["Photography", "Tutorial", "Beginner"],
        summary="Ten essential photography tips for beginners that will immediately improve your photos regardless of your equipment.",
        category="Photography",
        likes_count=320,
        comments_count=78,
        featured_image="https://example.com/images/photography-tips.jpg",
        read_time=5,
        slug="photography-tips-beginners"
    ),
    Post(
        id=5,
        title="The Future of AI and Its Impact",
        content=full_ai_content,
        author_id=4,
        created_at=datetime(2023, 9, 1),
        updated_at=datetime(2023, 9, 3),
        published=True,
        tags=["AI", "Technology", "Future", "Ethics"],
        summary="An exploration of how artificial intelligence is evolving and its potential impact on society, industries, and ethics.",
        category="Technology",
        likes_count=176,
        comments_count=53,
        featured_image="https://example.com/images/ai-future.jpg",
        read_time=6,
        slug="future-of-ai-impact"
    ),
    Post(
        id=6,
        title="Draft: New Project Ideas",
        content="Working on some new project ideas including a machine learning application for sustainable agriculture and a community platform for developers.",
        author_id=1,
        created_at=datetime(2023, 10, 1),
        updated_at=datetime(2023, 10, 1),
        published=False,
        tags=["Projects", "Ideas", "Innovation"],
        summary="Collection of new project ideas for future development",
        category="Projects",
        likes_count=0,
        comments_count=0,
        featured_image=None,
        read_time=2,
        slug="draft-new-project-ideas"
    )
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

def get_user_by_username(username):
    """Get a user by their username."""
    for user in sample_users:
        if user.username == username:
            return user
    return None

def get_post_by_id(id):
    """Get a post by its ID."""
    for post in sample_posts:
        if post.id == id:
            return post
    return None

def get_post_by_slug(slug):
    """Get a post by its slug."""
    for post in sample_posts:
        if post.slug == slug:
            return post
    return None

def get_posts_by_user_id(user_id, limit=None, published_only=False):
    """
    Get posts written by a specific user.

    Args:
        user_id (int): The ID of the user.
        limit (int, optional): Limit the number of posts returned.
        published_only (bool): If True, return only published posts.
    """
    posts = [post for post in sample_posts if post.author_id == user_id]

    if published_only:
        posts = [post for post in posts if post.published]

    if limit:
        return posts[:limit]
    return posts

def get_all_users():
    """Get all users."""
    return sample_users

def get_users_paginated(offset=0, limit=10):
    """
    Get users with pagination support.

    Args:
        offset (int): The number of users to skip.
        limit (int): The maximum number of users to return.
    """
    return sample_users[offset:offset + limit]

def get_users_by_role(role):
    """
    Get users filtered by role.

    Args:
        role (UserRole): The role to filter by.
    """
    return [user for user in sample_users if user.role == role]

def get_all_posts(published_only=False):
    """
    Get all posts.

    Args:
        published_only (bool): If True, return only published posts.
    """
    if published_only:
        return [post for post in sample_posts if post.published]
    return sample_posts

def get_posts_by_tag(tag, limit=None, published_only=False):
    """
    Get posts with a specific tag.

    Args:
        tag (str): The tag to filter by.
        limit (int, optional): Limit the number of posts returned.
        published_only (bool): If True, return only published posts.
    """
    posts = [post for post in sample_posts if tag in post.tags]

    if published_only:
        posts = [post for post in posts if post.published]

    if limit:
        return posts[:limit]
    return posts

def get_posts_by_category(category, limit=None, published_only=False):
    """
    Get posts with a specific category.

    Args:
        category (str): The category to filter by.
        limit (int, optional): Limit the number of posts returned.
        published_only (bool): If True, return only published posts.
    """
    posts = [post for post in sample_posts if post.category == category]

    if published_only:
        posts = [post for post in posts if post.published]

    if limit:
        return posts[:limit]
    return posts

def get_posts_paginated(offset=0, limit=10, published_only=False, order_by=None, category=None, tag=None):
    """
    Get posts with advanced pagination and filtering support.

    Args:
        offset (int): The number of posts to skip.
        limit (int): The maximum number of posts to return.
        published_only (bool): If True, return only published posts.
        order_by (str): Field to sort by ('created_at', 'updated_at', 'likes_count', 'comments_count').
        category (str, optional): Filter posts by category.
        tag (str, optional): Filter posts by tag.
    """
    # Start with all posts or only published posts
    posts = get_all_posts(published_only)

    # Apply category filter if specified
    if category:
        posts = [post for post in posts if post.category == category]

    # Apply tag filter if specified
    if tag:
        posts = [post for post in posts if tag in post.tags]

    # Apply sorting if specified
    if order_by:
        if order_by == 'created_at':
            posts = sorted(posts, key=lambda p: p.created_at, reverse=True)
        elif order_by == 'updated_at':
            posts = sorted(posts, key=lambda p: p.updated_at, reverse=True)
        elif order_by == 'likes_count':
            posts = sorted(posts, key=lambda p: p.likes_count, reverse=True)
        elif order_by == 'comments_count':
            posts = sorted(posts, key=lambda p: p.comments_count, reverse=True)
    else:
        # Default sort by created_at (newest first)
        posts = sorted(posts, key=lambda p: p.created_at, reverse=True)

    # Apply pagination
    return posts[offset:offset + limit]

def get_posts_search(search_term, offset=0, limit=10, published_only=True):
    """
    Search posts by term in title, content, or tags.

    Args:
        search_term (str): The term to search for.
        offset (int): The number of posts to skip.
        limit (int): The maximum number of posts to return.
        published_only (bool): If True, search only published posts.
    """
    # Get the base posts depending on published status
    posts = get_all_posts(published_only)

    # Filter posts that match the search term in title, content, or tags
    search_term = search_term.lower()
    filtered_posts = []

    for post in posts:
        if (search_term in post.title.lower() or
            search_term in post.content.lower() or
            search_term in post.summary.lower() or
            any(search_term in tag.lower() for tag in post.tags)):
            filtered_posts.append(post)

    # Return paginated results
    return filtered_posts[offset:offset + limit]

def get_popular_tags(limit=10, min_count=1):
    """
    Get popular tags with their usage count.

    Args:
        limit (int): Maximum number of tags to return.
        min_count (int): Minimum count to include a tag.
    """
    # Count tag occurrences
    tag_counts = {}
    for post in sample_posts:
        for tag in post.tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    # Filter by minimum count and sort by count (descending)
    popular_tags = [(tag, count) for tag, count in tag_counts.items() if count >= min_count]
    popular_tags.sort(key=lambda x: x[1], reverse=True)

    # Return limited results
    return popular_tags[:limit]

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