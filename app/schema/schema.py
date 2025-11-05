"""
GraphQL schema definition.

This module defines the GraphQL schema, types, and resolvers for the API.
"""

import graphene
from graphene import relay
from app.models import (
    get_author_by_id,
    get_book_by_id,
    get_books_by_author_id,
    get_all_books,
    get_all_authors
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

class Query(graphene.ObjectType):
    """Root query object for the GraphQL API."""
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

# Create the schema
schema = graphene.Schema(query=Query, types=[BookType, AuthorType])