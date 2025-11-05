"""
GraphQL schema definition.

This module defines the GraphQL schema, types, and resolvers for the API.
"""

import graphene
from graphene import relay
from datetime import datetime
from app.models import (
    # Original model functions
    get_author_by_id,
    get_book_by_id,
    get_books_by_author_id,
    get_all_books,
    get_all_authors,
    # Enhanced User and Post functions
    get_user_by_id,
    get_user_by_username,
    get_post_by_id,
    get_post_by_slug,
    get_posts_by_user_id,
    get_all_users,
    get_users_paginated,
    get_users_by_role,
    get_all_posts,
    get_posts_by_tag,
    get_posts_by_category,
    get_posts_paginated,
    get_posts_search,
    get_popular_tags,
    add_user,
    add_post,
    update_post,
    # Enums
    UserRole
)

class AuthorType(graphene.ObjectType):
    """GraphQL type for the Author model."""
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    birth_date = graphene.String()
    books = graphene.List(lambda: BookType, description="Books written by this author")

    def resolve_books(parent, info):
        """Resolver for the books field."""
        return get_books_by_author_id(parent.id)

class BookType(graphene.ObjectType):
    """GraphQL type for the Book model."""
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    author_id = graphene.Int(required=True)
    publication_year = graphene.Int()
    genre = graphene.String()
    author = graphene.Field(AuthorType, description="Author of this book")

    def resolve_author(parent, info):
        """Resolver for the author field."""
        return get_author_by_id(parent.author_id)

class UserRoleEnum(graphene.Enum):
    """GraphQL enum for user roles."""
    ADMIN = "admin"
    EDITOR = "editor"
    AUTHOR = "author"
    READER = "reader"

    @classmethod
    def from_model_role(cls, role):
        """Convert a model UserRole to a GraphQL UserRoleEnum."""
        return cls[role.name]

class UserType(graphene.ObjectType):
    """GraphQL type for the User model."""
    id = graphene.ID(required=True)
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    created_at = graphene.DateTime(required=True)
    bio = graphene.String()
    role = graphene.Field(UserRoleEnum)
    last_login = graphene.DateTime()
    profile_image = graphene.String()
    location = graphene.String()
    website = graphene.String()
    is_verified = graphene.Boolean()
    followers_count = graphene.Int()
    following_count = graphene.Int()

    # Relationships
    posts = graphene.List(
        lambda: PostType,
        description="Posts written by this user",
        limit=graphene.Int(description="Limit the number of posts returned"),
        published_only=graphene.Boolean(description="Filter to only show published posts")
    )
    posts_count = graphene.Int(description="Total number of posts by this user")

    def resolve_role(parent, info):
        """Resolver for the role field."""
        return UserRoleEnum.from_model_role(parent.role)

    def resolve_posts(parent, info, limit=None, published_only=False):
        """Resolver for the posts field."""
        return get_posts_by_user_id(parent.id, limit, published_only)

    def resolve_posts_count(parent, info):
        """Resolver for the posts_count field."""
        posts = get_posts_by_user_id(parent.id)
        return len(posts)

class PostType(graphene.ObjectType):
    """GraphQL type for the Post model."""
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    content = graphene.String(required=True)
    summary = graphene.String()
    author_id = graphene.Int(required=True)
    created_at = graphene.DateTime(required=True)
    updated_at = graphene.DateTime(required=True)
    published = graphene.Boolean(required=True)
    tags = graphene.List(graphene.String, required=True)
    category = graphene.String()
    likes_count = graphene.Int()
    comments_count = graphene.Int()
    featured_image = graphene.String()
    read_time = graphene.Int(description="Estimated reading time in minutes")
    slug = graphene.String()

    # Relationships
    author = graphene.Field(UserType, description="Author of this post")
    related_posts = graphene.List(
        lambda: PostType,
        description="Related posts with similar tags or by the same author",
        limit=graphene.Int(description="Limit the number of related posts returned")
    )

    def resolve_author(parent, info):
        """Resolver for the author field."""
        return get_user_by_id(parent.author_id)

    def resolve_related_posts(parent, info, limit=3):
        """Resolver for the related_posts field."""
        # Get posts with at least one matching tag
        related_by_tag = []
        for post in get_all_posts(published_only=True):
            if post.id != parent.id and any(tag in parent.tags for tag in post.tags):
                related_by_tag.append(post)

        # Get other posts by same author
        related_by_author = [
            post for post in get_posts_by_user_id(parent.author_id, published_only=True)
            if post.id != parent.id and post not in related_by_tag
        ]

        # Combine and limit results
        related = related_by_tag + related_by_author
        return related[:limit]

class TagCountType(graphene.ObjectType):
    """GraphQL type for tag counts."""
    tag = graphene.String(required=True)
    count = graphene.Int(required=True)

class UserInputType(graphene.InputObjectType):
    """Input type for creating a new user."""
    username = graphene.String(required=True, description="Username for the new user")
    email = graphene.String(required=True, description="Email address for the new user")
    bio = graphene.String(description="Biography for the new user")

class PostInputType(graphene.InputObjectType):
    """Input type for creating a new post."""
    title = graphene.String(required=True, description="Title of the post")
    content = graphene.String(required=True, description="Content of the post")
    author_id = graphene.Int(required=True, description="ID of the post author")
    tags = graphene.List(graphene.String, description="Tags for the post")
    published = graphene.Boolean(description="Whether the post is published")

class PostUpdateInputType(graphene.InputObjectType):
    """Input type for updating an existing post."""
    title = graphene.String(description="New title for the post")
    content = graphene.String(description="New content for the post")
    tags = graphene.List(graphene.String, description="New tags for the post")
    published = graphene.Boolean(description="New published status for the post")

class CreateUserMutation(graphene.Mutation):
    """Mutation for creating a new user."""
    class Arguments:
        input = UserInputType(required=True)

    user = graphene.Field(UserType)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input):
        """Mutation resolver for creating a new user."""
        # Validate input
        if len(input.username) < 3:
            raise ValueError("Username must be at least 3 characters long")

        # Simple email validation
        if "@" not in input.email or "." not in input.email:
            raise ValueError("Invalid email address")

        # Create new user
        user = add_user(
            username=input.username,
            email=input.email,
            bio=input.bio
        )

        return CreateUserMutation(user=user, ok=True)

class CreatePostMutation(graphene.Mutation):
    """Mutation for creating a new post."""
    class Arguments:
        input = PostInputType(required=True)

    post = graphene.Field(PostType)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, input):
        """Mutation resolver for creating a new post."""
        # Validate input
        if len(input.title) < 3:
            raise ValueError("Title must be at least 3 characters long")

        if len(input.content) < 10:
            raise ValueError("Content must be at least 10 characters long")

        # Check if author exists
        user = get_user_by_id(input.author_id)
        if not user:
            raise ValueError(f"No user found with ID {input.author_id}")

        # Create new post
        post = add_post(
            title=input.title,
            content=input.content,
            author_id=input.author_id,
            tags=input.tags,
            published=input.published if input.published is not None else True
        )

        return CreatePostMutation(post=post, ok=True)

class UpdatePostMutation(graphene.Mutation):
    """Mutation for updating an existing post."""
    class Arguments:
        id = graphene.ID(required=True)
        input = PostUpdateInputType(required=True)

    post = graphene.Field(PostType)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id, input):
        """Mutation resolver for updating an existing post."""
        # Validate ID
        post = get_post_by_id(int(id))
        if not post:
            raise ValueError(f"No post found with ID {id}")

        # Validate input fields if provided
        if input.title is not None and len(input.title) < 3:
            raise ValueError("Title must be at least 3 characters long")

        if input.content is not None and len(input.content) < 10:
            raise ValueError("Content must be at least 10 characters long")

        # Update post
        updated_post = update_post(
            id=int(id),
            title=input.title,
            content=input.content,
            tags=input.tags,
            published=input.published
        )

        return UpdatePostMutation(post=updated_post, ok=True)

class Query(graphene.ObjectType):
    """Root query object for the GraphQL API."""
    # Original queries
    book = graphene.Field(
        BookType,
        id=graphene.ID(required=True),
        description="Get a book by its ID"
    )
    books = graphene.List(
        BookType,
        description="Get all books",
        genre=graphene.String(description="Filter books by genre")
    )
    author = graphene.Field(
        AuthorType,
        id=graphene.ID(required=True),
        description="Get an author by their ID"
    )
    authors = graphene.List(
        AuthorType,
        description="Get all authors"
    )

    # Enhanced User queries
    user = graphene.Field(
        UserType,
        id=graphene.ID(description="User ID"),
        username=graphene.String(description="Username"),
        description="Get a user by ID or username"
    )
    users = graphene.List(
        UserType,
        description="Get users with various filters",
        limit=graphene.Int(description="Limit the number of users returned"),
        offset=graphene.Int(description="Skip the specified number of users"),
        role=graphene.String(description="Filter users by role")
    )

    # Enhanced Post queries
    post = graphene.Field(
        PostType,
        id=graphene.ID(description="Post ID"),
        slug=graphene.String(description="Post slug"),
        description="Get a post by ID or slug"
    )
    posts = graphene.List(
        PostType,
        description="Get posts with advanced filtering and pagination",
        published_only=graphene.Boolean(description="Filter to only show published posts"),
        tag=graphene.String(description="Filter posts by tag"),
        category=graphene.String(description="Filter posts by category"),
        author_id=graphene.ID(description="Filter posts by author ID"),
        search=graphene.String(description="Search term to find in title, content, or tags"),
        order_by=graphene.String(description="Order posts by field: created_at, updated_at, likes_count, or comments_count"),
        limit=graphene.Int(description="Limit the number of posts returned"),
        offset=graphene.Int(description="Skip the specified number of posts")
    )

    # Additional specialized queries
    popular_tags = graphene.List(
        TagCountType,
        limit=graphene.Int(description="Limit the number of tags returned"),
        min_count=graphene.Int(description="Minimum count to include a tag"),
        description="Get popular tags with their usage counts"
    )
    posts_by_category = graphene.List(
        graphene.String,
        description="Get all unique post categories"
    )

    # Original resolvers
    def resolve_book(root, info, id):
        """Resolver for the book field."""
        return get_book_by_id(int(id))

    def resolve_books(root, info, genre=None):
        """Resolver for the books field."""
        books = get_all_books()
        if genre:
            return [book for book in books if book.genre == genre]
        return books

    def resolve_author(root, info, id):
        """Resolver for the author field."""
        return get_author_by_id(int(id))

    def resolve_authors(root, info):
        """Resolver for the authors field."""
        return get_all_authors()

    # Enhanced resolvers for User and Post
    def resolve_user(root, info, id=None, username=None):
        """
        Resolver for the user field.

        Allows fetching a user by either ID or username.
        """
        if id:
            return get_user_by_id(int(id))
        elif username:
            return get_user_by_username(username)
        else:
            raise ValueError("Either id or username must be provided")

    def resolve_users(root, info, limit=None, offset=None, role=None):
        """
        Resolver for the users field.

        Supports pagination and filtering by role.
        """
        users = get_all_users()

        # Filter by role if specified
        if role:
            try:
                role_enum = UserRole[role.upper()]
                users = [user for user in users if user.role == role_enum]
            except KeyError:
                raise ValueError(f"Invalid role: {role}")

        # Apply pagination if specified
        if offset is not None or limit is not None:
            offset = offset or 0
            if limit is not None:
                users = users[offset:offset + limit]
            else:
                users = users[offset:]

        return users

    def resolve_post(root, info, id=None, slug=None):
        """
        Resolver for the post field.

        Allows fetching a post by either ID or slug.
        """
        if id:
            return get_post_by_id(int(id))
        elif slug:
            return get_post_by_slug(slug)
        else:
            raise ValueError("Either id or slug must be provided")

    def resolve_posts(root, info, published_only=False, tag=None, category=None,
                     author_id=None, search=None, order_by=None, limit=None, offset=None):
        """
        Resolver for the posts field.

        Supports advanced filtering, sorting and pagination.
        """
        # Handle search separately since it needs different logic
        if search:
            return get_posts_search(search, offset or 0, limit or 10, published_only)

        # Get posts with all the filtering options
        posts = get_posts_paginated(
            offset=offset or 0,
            limit=limit or 10,
            published_only=published_only,
            order_by=order_by,
            category=category,
            tag=tag
        )

        # Apply author filter if specified
        if author_id:
            posts = [post for post in posts if post.author_id == int(author_id)]

        return posts

    def resolve_popular_tags(root, info, limit=10, min_count=1):
        """
        Resolver for the popular_tags field.

        Returns popular tags with their counts.
        """
        tag_counts = get_popular_tags(limit, min_count)
        return [TagCountType(tag=tag, count=count) for tag, count in tag_counts]

    def resolve_posts_by_category(root, info):
        """
        Resolver for the posts_by_category field.

        Returns a list of all unique post categories.
        """
        categories = set()
        for post in get_all_posts():
            if post.category:
                categories.add(post.category)
        return sorted(list(categories))

class Mutation(graphene.ObjectType):
    """Root mutation object for the GraphQL API."""
    create_user = CreateUserMutation.Field()
    create_post = CreatePostMutation.Field()
    update_post = UpdatePostMutation.Field()

# Create the schema
schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    types=[BookType, AuthorType, UserType, PostType, TagCountType]
)