"""
GraphQL schema definition.

This module defines the GraphQL schema, types, and resolvers for the API.
"""

import graphene
from graphene import relay
from datetime import datetime
from graphql import GraphQLError
from app.models import (
    get_author_by_id,
    get_book_by_id,
    get_books_by_author_id,
    get_all_books,
    get_all_authors,
    get_user_by_id,
    get_user_by_username,
    get_users_by_role,
    get_post_by_id,
    get_posts_by_user_id,
    get_posts_by_category,
    get_posts_by_status,
    get_posts_by_date_range,
    get_all_users,
    get_users_paginated,
    get_all_posts,
    get_posts_by_tag,
    get_posts_paginated,
    get_posts_with_advanced_filtering,
    get_comment_by_id,
    get_comments_by_post_id,
    get_comments_by_user_id,
    get_comment_replies,
    get_comments_paginated,
    add_user,
    add_post,
    add_comment,
    update_post,
    authenticate_user,
    login_user,
    user_can_modify_post,
    UserRole,
    PostStatus,
    PostCategory,
    JWT_EXPIRATION_DELTA,
)
from app.auth import (
    require_auth,
    require_role,
    user_owns_resource,
    get_authenticated_user,
    logger as auth_logger,
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
    """GraphQL enum for UserRole."""
    ADMIN = UserRole.ADMIN.value
    EDITOR = UserRole.EDITOR.value
    AUTHOR = UserRole.AUTHOR.value
    READER = UserRole.READER.value
    MODERATOR = UserRole.MODERATOR.value

class PostStatusEnum(graphene.Enum):
    """GraphQL enum for PostStatus."""
    DRAFT = PostStatus.DRAFT.value
    PUBLISHED = PostStatus.PUBLISHED.value
    ARCHIVED = PostStatus.ARCHIVED.value
    SCHEDULED = PostStatus.SCHEDULED.value
    UNDER_REVIEW = PostStatus.UNDER_REVIEW.value

class PostCategoryEnum(graphene.Enum):
    """GraphQL enum for PostCategory."""
    TECHNOLOGY = PostCategory.TECHNOLOGY.value
    SCIENCE = PostCategory.SCIENCE.value
    HEALTH = PostCategory.HEALTH.value
    BUSINESS = PostCategory.BUSINESS.value
    ENTERTAINMENT = PostCategory.ENTERTAINMENT.value
    SPORTS = PostCategory.SPORTS.value
    POLITICS = PostCategory.POLITICS.value
    OTHER = PostCategory.OTHER.value

class UserType(graphene.ObjectType):
    """GraphQL type for the User model."""
    id = graphene.ID(required=True)
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    role = graphene.Field(UserRoleEnum, required=True)
    created_at = graphene.DateTime(required=True)
    bio = graphene.String()
    last_login = graphene.DateTime()
    posts = graphene.List(lambda: PostType, description="Posts written by this user")

    def resolve_posts(parent, info):
        """Resolver for the posts field."""
        # Get current user from context
        current_user = info.context.get('user', None)

        # For draft posts, only show to the author or admins/editors
        if current_user and (current_user.id == parent.id or
                           current_user.role in [UserRole.ADMIN, UserRole.EDITOR]):
            # Show all posts including drafts
            return get_posts_by_user_id(parent.id)
        else:
            # Show only published posts
            return [post for post in get_posts_by_user_id(parent.id) if post.published]

    def resolve_email(parent, info):
        """Resolver for the email field with privacy protection."""
        current_user = info.context.get('user', None)

        # Users can see their own email
        if current_user and current_user.id == parent.id:
            return parent.email

        # Admins can see any email
        if current_user and current_user.role == UserRole.ADMIN:
            return parent.email

        # For others, return a placeholder or partial email
        if parent.email:
            username, domain = parent.email.split('@')
            return f"{username[0]}{'*' * (len(username)-2)}{username[-1]}@{domain}"
        return None

class PostType(graphene.ObjectType):
    """GraphQL type for the Post model."""
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    content = graphene.String(required=True)
    author_id = graphene.Int(required=True)
    created_at = graphene.DateTime(required=True)
    updated_at = graphene.DateTime(required=True)
    published = graphene.Boolean(required=True)
    tags = graphene.List(graphene.String, required=True)
    author = graphene.Field(UserType, description="Author of this post")

    def resolve_author(parent, info):
        """Resolver for the author field."""
        return get_user_by_id(parent.author_id)

class TagCountType(graphene.ObjectType):
    """GraphQL type for tag counts."""
    tag = graphene.String(required=True)
    count = graphene.Int(required=True)

class AuthPayloadType(graphene.ObjectType):
    """GraphQL type for authentication response."""
    token = graphene.String(required=True, description="JWT token for authentication")
    user = graphene.Field(UserType, required=True, description="The authenticated user")
    expires_in = graphene.Int(required=True, description="Token expiration time in seconds")

class UserInputType(graphene.InputObjectType):
    """Input type for creating a new user."""
    username = graphene.String(required=True, description="Username for the new user")
    email = graphene.String(required=True, description="Email address for the new user")
    password = graphene.String(required=True, description="Password for the new user")
    role = graphene.Field(UserRoleEnum, description="Role for the new user")
    bio = graphene.String(description="Biography for the new user")

class LoginInputType(graphene.InputObjectType):
    """Input type for user login."""
    username = graphene.String(required=True, description="Username")
    password = graphene.String(required=True, description="Password")

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

    # New queries for User and Post
    user = graphene.Field(
        UserType,
        id=graphene.ID(required=True),
        description="Get a user by their ID"
    )
    users = graphene.List(
        UserType,
        description="Get all users"
    )
    post = graphene.Field(
        PostType,
        id=graphene.ID(required=True),
        description="Get a post by its ID"
    )
    posts = graphene.List(
        PostType,
        description="Get all posts",
        published_only=graphene.Boolean(description="Filter to only show published posts"),
        tag=graphene.String(description="Filter posts by tag"),
        limit=graphene.Int(description="Limit the number of posts returned"),
        offset=graphene.Int(description="Skip the specified number of posts")
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

    # New resolvers for User and Post
    def resolve_user(root, info, id):
        """Resolver for the user field."""
        return get_user_by_id(int(id))

    def resolve_users(root, info):
        """Resolver for the users field."""
        return get_all_users()

    def resolve_post(root, info, id):
        """Resolver for the post field."""
        return get_post_by_id(int(id))

    def resolve_posts(root, info, published_only=None, tag=None, limit=None, offset=None):
        """Resolver for the posts field."""
        # Apply filtering for published posts
        posts = get_all_posts(published_only=published_only if published_only is not None else False)

        # Apply tag filtering if specified
        if tag:
            posts = [post for post in posts if tag in post.tags]

        # Apply pagination if specified
        if offset is not None or limit is not None:
            offset = offset or 0
            if limit is not None:
                posts = posts[offset:offset + limit]
            else:
                posts = posts[offset:]

        return posts

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