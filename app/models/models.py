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
    MODERATOR = "moderator"  # Can moderate content from all users

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
        role (UserRole): The role of the user (admin, editor, author, reader, moderator).
        created_at (datetime): The date and time when the user was created.
        bio (str, optional): A short biography of the user.
        last_login (datetime, optional): The last time the user logged in.
        display_name (str, optional): The user's display name.
        avatar_url (str, optional): URL to the user's avatar image.
        status (str, optional): Current status of the user (active, inactive, suspended).
        preferences (dict, optional): User preferences like theme, notifications settings.
        location (str, optional): User's location information.
        website (str, optional): User's personal or professional website.
        social_links (dict, optional): Links to user's social profiles.
    """
    def __init__(self, id, username, email, password_hash=None, role=UserRole.READER,
                 created_at=None, bio=None, last_login=None, display_name=None,
                 avatar_url=None, status="active", preferences=None, location=None,
                 website=None, social_links=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.created_at = created_at or datetime.now()
        self.bio = bio
        self.last_login = last_login
        self.display_name = display_name or username
        self.avatar_url = avatar_url
        self.status = status
        self.preferences = preferences or {}
        self.location = location
        self.website = website
        self.social_links = social_links or {}

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

class PostStatus(Enum):
    """Enum for post status."""
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"
    SCHEDULED = "scheduled"
    UNDER_REVIEW = "under_review"

class PostCategory(Enum):
    """Enum for post categories."""
    TECHNOLOGY = "technology"
    SCIENCE = "science"
    HEALTH = "health"
    BUSINESS = "business"
    ENTERTAINMENT = "entertainment"
    SPORTS = "sports"
    POLITICS = "politics"
    OTHER = "other"

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
        status (PostStatus): The current status of the post.
        category (PostCategory): The category of the post.
        excerpt (str, optional): A short excerpt or summary of the post.
        featured_image_url (str, optional): URL to the featured image for the post.
        read_time (int, optional): Estimated reading time in minutes.
        likes_count (int): Number of likes the post has received.
        comments_count (int): Number of comments on the post.
        views_count (int): Number of views the post has received.
        allow_comments (bool): Whether comments are allowed on this post.
        meta_description (str, optional): Meta description for SEO.
        meta_keywords (list, optional): Meta keywords for SEO.
        publish_date (datetime, optional): When the post was or will be published.
    """
    def __init__(self, id, title, content, author_id, created_at=None, updated_at=None,
                 published=True, tags=None, status=PostStatus.DRAFT, category=PostCategory.OTHER,
                 excerpt=None, featured_image_url=None, read_time=None, likes_count=0,
                 comments_count=0, views_count=0, allow_comments=True, meta_description=None,
                 meta_keywords=None, publish_date=None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.published = published
        self.tags = tags or []
        self.status = PostStatus.PUBLISHED if published else PostStatus.DRAFT
        self.category = category
        self.excerpt = excerpt or (content[:150] + '...' if len(content) > 150 else content)
        self.featured_image_url = featured_image_url
        self.read_time = read_time or max(1, len(content.split()) // 200)  # Rough estimate: 200 words per minute
        self.likes_count = likes_count
        self.comments_count = comments_count
        self.views_count = views_count
        self.allow_comments = allow_comments
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords or []
        self.publish_date = publish_date or (datetime.now() if published else None)

class Comment:
    """
    Comment model representing a comment on a post.

    Attributes:
        id (int): The unique identifier for the comment.
        content (str): The content of the comment.
        author_id (int): The ID of the user who authored the comment.
        post_id (int): The ID of the post this comment is on.
        created_at (datetime): The date and time when the comment was created.
        updated_at (datetime): The date and time when the comment was last updated.
        parent_id (int, optional): The ID of the parent comment if this is a reply.
        likes_count (int): Number of likes the comment has received.
    """
    def __init__(self, id, content, author_id, post_id, created_at=None, updated_at=None,
                 parent_id=None, likes_count=0):
        self.id = id
        self.content = content
        self.author_id = author_id
        self.post_id = post_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.parent_id = parent_id
        self.likes_count = likes_count

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
         datetime(2023, 1, 15),
         "Software developer and tech enthusiast",
         datetime(2023, 10, 1),
         "John Doe",
         "https://example.com/avatars/john.jpg",
         "active",
         {"theme": "dark", "notifications": True},
         "San Francisco, CA",
         "https://johndoe.dev",
         {"github": "johndoe", "twitter": "johndoe_dev"}),
    User(2, "jane_smith", "jane@example.com",
         User.hash_password("password123"),
         UserRole.EDITOR,
         datetime(2023, 2, 20),
         "Digital artist and photographer",
         datetime(2023, 10, 5),
         "Jane Smith",
         "https://example.com/avatars/jane.jpg",
         "active",
         {"theme": "light", "notifications": True},
         "New York, NY",
         "https://janesmith.art",
         {"instagram": "janesmith_art", "dribbble": "janesmith"}),
    User(3, "bob_johnson", "bob@example.com",
         User.hash_password("password123"),
         UserRole.AUTHOR,
         datetime(2023, 3, 10),
         "Travel blogger and adventure seeker",
         datetime(2023, 9, 28),
         "Bob Johnson",
         "https://example.com/avatars/bob.jpg",
         "active",
         {"theme": "auto", "notifications": False},
         "Sydney, Australia",
         "https://bobjohnson.travel",
         {"instagram": "bob_travels", "youtube": "BobJourneys"}),
    User(4, "alice_brown", "alice@example.com",
         User.hash_password("password123"),
         UserRole.READER,
         datetime(2023, 4, 5),
         "Science writer and researcher",
         datetime(2023, 9, 15),
         "Alice Brown",
         "https://example.com/avatars/alice.jpg",
         "active",
         {"theme": "light", "notifications": True},
         "Boston, MA",
         "https://alicebrown.science",
         {"twitter": "alice_science", "linkedin": "alicebrown"}),
    User(5, "sam_moderator", "sam@example.com",
         User.hash_password("password123"),
         UserRole.MODERATOR,
         datetime(2023, 5, 20),
         "Community moderator and content curator",
         datetime(2023, 10, 10),
         "Sam Moderator",
         "https://example.com/avatars/sam.jpg",
         "active",
         {"theme": "dark", "notifications": True},
         "Chicago, IL",
         "https://sam-moderator.com",
         {"twitter": "sam_mod", "reddit": "sam_moderator"})
]

sample_posts = [
    Post(1, "Getting Started with GraphQL",
         "This is a beginner's guide to GraphQL. GraphQL is a query language for your API and a runtime for executing those queries against your data. GraphQL provides a complete description of the data in your API, gives clients the power to ask for exactly what they need, makes it easier to evolve APIs over time, and enables powerful developer tools.",
         1, datetime(2023, 5, 10), datetime(2023, 5, 10), True,
         ["GraphQL", "API", "Tutorial"], PostStatus.PUBLISHED, PostCategory.TECHNOLOGY,
         "An introduction to GraphQL for beginners...",
         "https://example.com/images/graphql-intro.jpg",
         5, 120, 25, 5000, True,
         "Learn the basics of GraphQL and how to implement it in your applications",
         ["GraphQL", "API", "Web Development", "Tutorial"],
         datetime(2023, 5, 10)),
    Post(2, "Advanced GraphQL Techniques",
         "In this post, we'll explore advanced GraphQL features including fragments, directives, interfaces, and union types. We'll also cover pagination strategies, caching, and optimizing performance in production GraphQL APIs.",
         1, datetime(2023, 6, 15), datetime(2023, 6, 20), True,
         ["GraphQL", "Advanced"], PostStatus.PUBLISHED, PostCategory.TECHNOLOGY,
         "Exploring advanced GraphQL features for production applications...",
         "https://example.com/images/advanced-graphql.jpg",
         10, 85, 15, 3200, True,
         "Take your GraphQL skills to the next level with advanced techniques",
         ["GraphQL", "API", "Advanced", "Performance"],
         datetime(2023, 6, 15)),
    Post(3, "My Travel Adventures",
         "Recently I visited the amazing landscapes of New Zealand. From the majestic mountains of Queenstown to the serene beaches of the Coromandel Peninsula, this country offers breathtaking views at every turn. In this post, I share my journey, tips for fellow travelers, and the best spots for photography.",
         3, datetime(2023, 7, 5), datetime(2023, 7, 5), True,
         ["Travel", "Adventure"], PostStatus.PUBLISHED, PostCategory.ENTERTAINMENT,
         "Exploring the natural wonders of New Zealand...",
         "https://example.com/images/nz-travel.jpg",
         8, 210, 42, 7500, True,
         "A journey through New Zealand's most beautiful landscapes",
         ["Travel", "New Zealand", "Adventure", "Photography"],
         datetime(2023, 7, 5)),
    Post(4, "Photography Tips",
         "Here are my top 10 photography tips for beginners. Photography is an art form that requires both technical knowledge and creative vision. In this guide, I'll share techniques that will help you capture stunning images regardless of your equipment. From composition rules to lighting techniques, these tips will elevate your photography skills.",
         2, datetime(2023, 8, 12), datetime(2023, 8, 15), True,
         ["Photography", "Tutorial"], PostStatus.PUBLISHED, PostCategory.ENTERTAINMENT,
         "Essential photography tips for capturing stunning images...",
         "https://example.com/images/photo-tips.jpg",
         7, 175, 38, 6400, True,
         "Learn 10 essential photography techniques to improve your skills",
         ["Photography", "Tutorial", "Beginner", "Creative"],
         datetime(2023, 8, 12)),
    Post(5, "The Future of AI",
         "Artificial intelligence is rapidly evolving, transforming industries and reshaping our daily lives. From machine learning algorithms that power recommendation systems to advanced language models capable of generating human-like text, AI technologies are becoming increasingly sophisticated. This post explores current trends and makes predictions about the future landscape of artificial intelligence.",
         4, datetime(2023, 9, 1), datetime(2023, 9, 3), True,
         ["AI", "Technology", "Future"], PostStatus.PUBLISHED, PostCategory.SCIENCE,
         "Exploring current trends and future predictions in artificial intelligence...",
         "https://example.com/images/ai-future.jpg",
         12, 150, 30, 5800, True,
         "An in-depth look at how AI is evolving and what the future holds",
         ["AI", "Machine Learning", "Technology", "Future"],
         datetime(2023, 9, 1)),
    Post(6, "Draft: New Project Ideas",
         "Working on some new project ideas for the upcoming quarter. This post will outline potential directions for our team's innovation efforts, including potential technologies to explore and market needs to address.",
         1, datetime(2023, 10, 1), datetime(2023, 10, 1), False,
         ["Projects", "Ideas"], PostStatus.DRAFT, PostCategory.BUSINESS,
         "Brainstorming new project directions for Q4...",
         None, 4, 0, 0, 0, True,
         "Internal planning document for upcoming projects",
         ["Planning", "Innovation", "Projects"],
         None),
    Post(7, "Healthy Eating Habits",
         "Developing healthy eating habits is essential for maintaining good health and wellbeing. This comprehensive guide covers nutrition fundamentals, meal planning strategies, and practical tips for busy professionals. Learn how small, sustainable changes to your diet can lead to significant improvements in energy levels, mood, and overall health.",
         5, datetime(2023, 9, 15), datetime(2023, 9, 15), True,
         ["Health", "Nutrition", "Wellness"], PostStatus.PUBLISHED, PostCategory.HEALTH,
         "A comprehensive guide to developing sustainable healthy eating habits...",
         "https://example.com/images/healthy-eating.jpg",
         9, 190, 45, 8200, True,
         "Practical nutrition advice for improving your diet and health",
         ["Health", "Nutrition", "Diet", "Wellness"],
         datetime(2023, 9, 15)),
    Post(8, "Web Development in 2023",
         "The landscape of web development continues to evolve at a rapid pace. This post examines the current state of web technologies, highlighting emerging trends and tools that are shaping the industry. From framework advancements to new browser capabilities, stay updated on what's important for modern web developers.",
         1, datetime(2023, 10, 5), datetime(2023, 10, 5), True,
         ["Web Development", "Technology", "Programming"], PostStatus.PUBLISHED, PostCategory.TECHNOLOGY,
         "An overview of current trends in web development...",
         "https://example.com/images/webdev-2023.jpg",
         11, 165, 32, 6100, True,
         "Stay updated on the latest web development technologies and trends",
         ["Web Development", "JavaScript", "Frontend", "Backend"],
         datetime(2023, 10, 5)),
    Post(9, "Introduction to React Hooks",
         "React Hooks have revolutionized how we build components in React. This tutorial provides a comprehensive introduction to Hooks, explaining how they simplify state management and side effects in functional components. With practical examples and best practices, you'll learn how to leverage useState, useEffect, useContext, and custom hooks in your applications.",
         1, datetime(2023, 7, 20), datetime(2023, 7, 22), True,
         ["React", "JavaScript", "Frontend", "Hooks"], PostStatus.PUBLISHED, PostCategory.TECHNOLOGY,
         "Learn how to use React Hooks to build more maintainable components...",
         "https://example.com/images/react-hooks.jpg",
         8, 200, 40, 9200, True,
         "A comprehensive guide to React Hooks with practical examples",
         ["React", "JavaScript", "Web Development", "Hooks"],
         datetime(2023, 7, 20)),
    Post(10, "Climate Change: Facts and Solutions",
         "Climate change presents one of the most pressing challenges of our time. This article examines the scientific evidence behind climate change, its current and projected impacts, and the range of solutions being developed to address this global issue. From renewable energy to policy reforms, discover how innovation and collective action are essential for a sustainable future.",
         4, datetime(2023, 8, 5), datetime(2023, 8, 8), True,
         ["Climate", "Environment", "Science", "Sustainability"], PostStatus.PUBLISHED, PostCategory.SCIENCE,
         "Examining the evidence and potential solutions for climate change...",
         "https://example.com/images/climate-change.jpg",
         15, 180, 35, 7800, True,
         "Understanding the science of climate change and exploring viable solutions",
         ["Climate Change", "Environment", "Science", "Sustainability"],
         datetime(2023, 8, 5))
]

# Sample comments data
sample_comments = [
    Comment(1, "Great introduction to GraphQL! Really helped me understand the basics.", 2, 1,
            datetime(2023, 5, 11), datetime(2023, 5, 11), None, 5),
    Comment(2, "I've been using GraphQL for a while now, and this post covers all the essentials.", 3, 1,
            datetime(2023, 5, 12), datetime(2023, 5, 12), None, 3),
    Comment(3, "Thanks for the feedback! Glad you found it helpful.", 1, 1,
            datetime(2023, 5, 12), datetime(2023, 5, 12), 1, 2),
    Comment(4, "This advanced guide is exactly what I needed. The section on pagination is particularly useful.", 4, 2,
            datetime(2023, 6, 16), datetime(2023, 6, 16), None, 4),
    Comment(5, "Have you considered adding information about Apollo Client?", 2, 2,
            datetime(2023, 6, 17), datetime(2023, 6, 17), None, 1),
    Comment(6, "Good suggestion! I'll add that in a future post.", 1, 2,
            datetime(2023, 6, 18), datetime(2023, 6, 18), 5, 0),
    Comment(7, "New Zealand is now on my bucket list after reading this. Beautiful photos!", 5, 3,
            datetime(2023, 7, 6), datetime(2023, 7, 6), None, 7),
    Comment(8, "Which month would you recommend visiting?", 4, 3,
            datetime(2023, 7, 7), datetime(2023, 7, 7), None, 2),
    Comment(9, "December through February is summer there, so that's a great time to visit!", 3, 3,
            datetime(2023, 7, 8), datetime(2023, 7, 8), 8, 3),
    Comment(10, "These photography tips are so practical. I've already improved my shots using rule #3.", 3, 4,
             datetime(2023, 8, 13), datetime(2023, 8, 13), None, 6),
    Comment(11, "The AI predictions are fascinating. I think language models will continue to be a major focus.", 1, 5,
             datetime(2023, 9, 2), datetime(2023, 9, 2), None, 4),
    Comment(12, "The ethical considerations section was particularly thoughtful.", 2, 5,
             datetime(2023, 9, 3), datetime(2023, 9, 3), None, 5),
    Comment(13, "I agree completely. Ethics in AI needs more attention.", 5, 5,
             datetime(2023, 9, 4), datetime(2023, 9, 4), 12, 2),
    Comment(14, "The meal planning templates are super helpful, thank you!", 4, 7,
             datetime(2023, 9, 16), datetime(2023, 9, 16), None, 8),
    Comment(15, "Do you have any recommendations for plant-based diets?", 2, 7,
             datetime(2023, 9, 17), datetime(2023, 9, 17), None, 3)
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

def get_users_by_role(role):
    """Get all users with a specific role."""
    return [user for user in sample_users if user.role == role]

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

def get_users_paginated(offset=0, limit=10):
    """
    Get users with pagination support.

    Args:
        offset (int): The number of users to skip.
        limit (int): The maximum number of users to return.
    """
    users = get_all_users()
    return users[offset:offset + limit]

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

def get_posts_by_category(category):
    """Get all posts in a specific category."""
    return [post for post in sample_posts if post.category == category]

def get_posts_by_status(status):
    """Get all posts with a specific status."""
    return [post for post in sample_posts if post.status == status]

def get_posts_by_date_range(start_date, end_date):
    """
    Get all posts created within a date range.

    Args:
        start_date (datetime): The start date (inclusive).
        end_date (datetime): The end date (inclusive).
    """
    return [
        post for post in sample_posts
        if start_date <= post.created_at <= end_date
    ]

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

def get_posts_with_advanced_filtering(
    author_id=None,
    tags=None,
    category=None,
    status=None,
    published_only=None,
    start_date=None,
    end_date=None,
    search_term=None,
    sort_by="created_at",
    sort_direction="desc",
    offset=0,
    limit=10
):
    """
    Get posts with advanced filtering and sorting.

    Args:
        author_id (int, optional): Filter by author ID.
        tags (list, optional): Filter by tags (posts must have ALL specified tags).
        category (PostCategory, optional): Filter by category.
        status (PostStatus, optional): Filter by status.
        published_only (bool, optional): If True, return only published posts.
        start_date (datetime, optional): Filter by posts created after this date.
        end_date (datetime, optional): Filter by posts created before this date.
        search_term (str, optional): Search in title and content.
        sort_by (str, optional): Field to sort by (created_at, updated_at, title, etc.).
        sort_direction (str, optional): Sort direction (asc or desc).
        offset (int): The number of posts to skip.
        limit (int): The maximum number of posts to return.

    Returns:
        list: Filtered and sorted posts.
    """
    # Start with all posts
    filtered_posts = sample_posts.copy()

    # Apply filters
    if author_id is not None:
        filtered_posts = [post for post in filtered_posts if post.author_id == author_id]

    if tags is not None and len(tags) > 0:
        filtered_posts = [
            post for post in filtered_posts
            if all(tag in post.tags for tag in tags)
        ]

    if category is not None:
        filtered_posts = [post for post in filtered_posts if post.category == category]

    if status is not None:
        filtered_posts = [post for post in filtered_posts if post.status == status]

    if published_only is not None:
        filtered_posts = [post for post in filtered_posts if post.published == published_only]

    if start_date is not None:
        filtered_posts = [post for post in filtered_posts if post.created_at >= start_date]

    if end_date is not None:
        filtered_posts = [post for post in filtered_posts if post.created_at <= end_date]

    if search_term is not None and search_term.strip():
        search_term = search_term.lower()
        filtered_posts = [
            post for post in filtered_posts
            if search_term in post.title.lower() or search_term in post.content.lower()
        ]

    # Sort the results
    reverse = sort_direction.lower() == "desc"
    if sort_by in ["created_at", "updated_at", "publish_date"]:
        filtered_posts.sort(key=lambda post: getattr(post, sort_by) or datetime.min, reverse=reverse)
    elif sort_by in ["likes_count", "comments_count", "views_count", "read_time"]:
        filtered_posts.sort(key=lambda post: getattr(post, sort_by) or 0, reverse=reverse)
    else:  # Default to string comparison for fields like title
        filtered_posts.sort(key=lambda post: str(getattr(post, sort_by) or "").lower(), reverse=reverse)

    # Apply pagination
    return filtered_posts[offset:offset + limit]

# Comment helper functions
def get_comment_by_id(id):
    """Get a comment by its ID."""
    for comment in sample_comments:
        if comment.id == id:
            return comment
    return None

def get_comments_by_post_id(post_id):
    """Get all comments for a specific post."""
    return [comment for comment in sample_comments if comment.post_id == post_id]

def get_comments_by_user_id(user_id):
    """Get all comments made by a specific user."""
    return [comment for comment in sample_comments if comment.author_id == user_id]

def get_comment_replies(comment_id):
    """Get all replies to a specific comment."""
    return [comment for comment in sample_comments if comment.parent_id == comment_id]

def get_comments_paginated(post_id=None, offset=0, limit=10, parent_id=None):
    """
    Get comments with pagination support.

    Args:
        post_id (int, optional): Filter by post ID.
        offset (int): The number of comments to skip.
        limit (int): The maximum number of comments to return.
        parent_id (int, optional): Filter by parent comment ID for replies.

    Returns:
        list: Filtered comments with pagination.
    """
    comments = sample_comments

    if post_id is not None:
        comments = [comment for comment in comments if comment.post_id == post_id]

    if parent_id is not None:
        comments = [comment for comment in comments if comment.parent_id == parent_id]
    else:
        # If not looking for replies, get top-level comments (no parent)
        if parent_id is None and post_id is not None:
            comments = [comment for comment in comments if comment.parent_id is None]

    # Sort by creation date (newest first)
    comments.sort(key=lambda comment: comment.created_at, reverse=True)

    return comments[offset:offset + limit]

def add_comment(content, author_id, post_id, parent_id=None):
    """
    Add a new comment.

    Args:
        content (str): The content of the comment.
        author_id (int): The ID of the user who authored the comment.
        post_id (int): The ID of the post this comment is on.
        parent_id (int, optional): The ID of the parent comment if this is a reply.

    Returns:
        Comment: The newly created comment.
    """
    # Create a new comment ID
    new_id = max(comment.id for comment in sample_comments) + 1
    now = datetime.now()

    # Create the comment
    new_comment = Comment(
        id=new_id,
        content=content,
        author_id=author_id,
        post_id=post_id,
        created_at=now,
        updated_at=now,
        parent_id=parent_id,
        likes_count=0
    )

    # Add comment to the sample data
    sample_comments.append(new_comment)

    # Update comment count on the post
    post = get_post_by_id(post_id)
    if post:
        post.comments_count += 1

    return new_comment

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

def update_post(id, title=None, content=None, tags=None, published=None, status=None, category=None,
                excerpt=None, featured_image_url=None, read_time=None, allow_comments=None,
                meta_description=None, meta_keywords=None, publish_date=None):
    """
    Update an existing post.

    Args:
        id (int): The ID of the post to update.
        title (str, optional): The new title of the post.
        content (str, optional): The new content of the post.
        tags (list, optional): The new tags for the post.
        published (bool, optional): The new published status of the post.
        status (PostStatus, optional): The new status of the post.
        category (PostCategory, optional): The new category of the post.
        excerpt (str, optional): The new excerpt of the post.
        featured_image_url (str, optional): The new featured image URL.
        read_time (int, optional): The new estimated reading time in minutes.
        allow_comments (bool, optional): Whether comments are allowed on this post.
        meta_description (str, optional): The new meta description for SEO.
        meta_keywords (list, optional): The new meta keywords for SEO.
        publish_date (datetime, optional): When the post was or will be published.

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
        # Update status to match published state if status is not explicitly set
        if status is None:
            post.status = PostStatus.PUBLISHED if published else PostStatus.DRAFT
    if status is not None:
        post.status = status
    if category is not None:
        post.category = category
    if excerpt is not None:
        post.excerpt = excerpt
    if featured_image_url is not None:
        post.featured_image_url = featured_image_url
    if read_time is not None:
        post.read_time = read_time
    if allow_comments is not None:
        post.allow_comments = allow_comments
    if meta_description is not None:
        post.meta_description = meta_description
    if meta_keywords is not None:
        post.meta_keywords = meta_keywords
    if publish_date is not None:
        post.publish_date = publish_date

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