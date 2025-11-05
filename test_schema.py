"""
Unit tests for the GraphQL schema.
"""

import json
import pytest
from app.schema import schema

def test_query_all_books():
    """Test querying all books."""
    query = '''
    query {
      books {
        id
        title
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    assert len(result.data['books']) == 5  # We have 5 sample books

def test_query_book_by_id():
    """Test querying a book by ID."""
    query = '''
    query {
      book(id: "1") {
        id
        title
        author {
          name
        }
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    assert result.data['book']['id'] == '1'
    assert result.data['book']['title'] == "Harry Potter and the Philosopher's Stone"
    assert result.data['book']['author']['name'] == "J.K. Rowling"

def test_query_all_authors():
    """Test querying all authors."""
    query = '''
    query {
      authors {
        id
        name
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    assert len(result.data['authors']) == 3  # We have 3 sample authors

def test_query_author_by_id():
    """Test querying an author by ID."""
    query = '''
    query {
      author(id: "2") {
        id
        name
        books {
          title
        }
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    assert result.data['author']['id'] == '2'
    assert result.data['author']['name'] == "George Orwell"
    # George Orwell has 2 books in our sample data
    assert len(result.data['author']['books']) == 2

def test_filter_books_by_genre():
    """Test filtering books by genre."""
    query = '''
    query {
      books(genre: "Fantasy") {
        title
        genre
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    assert len(result.data['books']) == 3  # We have 3 Fantasy books
    for book in result.data['books']:
        assert book['genre'] == "Fantasy"