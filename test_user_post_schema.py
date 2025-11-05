"""
Unit tests for the User and Post GraphQL schema.
"""

import json
import pytest
from app.schema import schema

def test_query_all_users():
    """Test querying all users."""
    query = '''
    query {
      users {
        id
        username
        email
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    assert len(result.data['users']) == 4  # We have 4 sample users

def test_query_user_by_id():
    """Test querying a user by ID."""
    query = '''
    query {
      user(id: "1") {
        id
        username
        email
        bio
        posts {
          title
        }
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    assert result.data['user']['id'] == '1'
    assert result.data['user']['username'] == "john_doe"
    assert result.data['user']['email'] == "john@example.com"
    # Check that the posts relationship works
    assert len(result.data['user']['posts']) >= 2  # John Doe has at least 2 posts

def test_query_all_posts():
    """Test querying all posts."""
    query = '''
    query {
      posts {
        id
        title
        content
        published
        author {
          username
        }
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    assert len(result.data['posts']) >= 5  # We have at least 5 sample posts

def test_query_post_by_id():
    """Test querying a post by ID."""
    query = '''
    query {
      post(id: "1") {
        id
        title
        content
        published
        tags
        author {
          username
          email
        }
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    assert result.data['post']['id'] == '1'
    assert result.data['post']['title'] == "Getting Started with GraphQL"
    assert "GraphQL" in result.data['post']['content']
    assert result.data['post']['author']['username'] == "john_doe"

def test_filter_posts_by_tag():
    """Test filtering posts by tag."""
    query = '''
    query {
      posts(tag: "GraphQL") {
        title
        tags
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    # We should have at least 2 posts with the GraphQL tag
    assert len(result.data['posts']) >= 2
    for post in result.data['posts']:
        assert "GraphQL" in post['tags']

def test_filter_posts_by_published():
    """Test filtering posts by published status."""
    query = '''
    query {
      posts(published_only: true) {
        title
        published
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    for post in result.data['posts']:
        assert post['published'] is True

def test_posts_pagination():
    """Test post pagination."""
    query = '''
    query {
      posts(limit: 2, offset: 1) {
        id
        title
      }
    }
    '''
    result = schema.execute(query)
    assert not result.errors
    assert len(result.data['posts']) == 2

def test_create_user_mutation():
    """Test creating a new user."""
    mutation = '''
    mutation {
      createUser(input: {
        username: "test_user",
        email: "test@example.com",
        bio: "This is a test user"
      }) {
        ok
        user {
          id
          username
          email
          bio
        }
      }
    }
    '''
    result = schema.execute(mutation)
    assert not result.errors
    assert result.data['createUser']['ok'] is True
    assert result.data['createUser']['user']['username'] == "test_user"
    assert result.data['createUser']['user']['email'] == "test@example.com"
    assert result.data['createUser']['user']['bio'] == "This is a test user"

def test_create_user_validation():
    """Test validation when creating a user."""
    mutation = '''
    mutation {
      createUser(input: {
        username: "t",
        email: "invalid-email"
      }) {
        ok
        user {
          id
        }
      }
    }
    '''
    result = schema.execute(mutation)
    assert result.errors  # We expect validation errors

def test_create_post_mutation():
    """Test creating a new post."""
    mutation = '''
    mutation {
      createPost(input: {
        title: "Test Post",
        content: "This is a test post content",
        authorId: 1,
        tags: ["Test", "GraphQL"],
        published: true
      }) {
        ok
        post {
          id
          title
          content
          tags
          published
          author {
            username
          }
        }
      }
    }
    '''
    result = schema.execute(mutation)
    assert not result.errors
    assert result.data['createPost']['ok'] is True
    assert result.data['createPost']['post']['title'] == "Test Post"
    assert result.data['createPost']['post']['content'] == "This is a test post content"
    assert "Test" in result.data['createPost']['post']['tags']
    assert "GraphQL" in result.data['createPost']['post']['tags']
    assert result.data['createPost']['post']['published'] is True
    assert result.data['createPost']['post']['author']['username'] == "john_doe"

def test_create_post_validation():
    """Test validation when creating a post."""
    mutation = '''
    mutation {
      createPost(input: {
        title: "T",
        content: "Short",
        authorId: 1
      }) {
        ok
        post {
          id
        }
      }
    }
    '''
    result = schema.execute(mutation)
    assert result.errors  # We expect validation errors

def test_update_post_mutation():
    """Test updating an existing post."""
    mutation = '''
    mutation {
      updatePost(
        id: "1",
        input: {
          title: "Updated Post Title",
          content: "This is the updated content for the post.",
          tags: ["Updated", "GraphQL"],
          published: true
        }
      ) {
        ok
        post {
          id
          title
          content
          tags
          published
          updatedAt
        }
      }
    }
    '''
    result = schema.execute(mutation)
    assert not result.errors
    assert result.data['updatePost']['ok'] is True
    assert result.data['updatePost']['post']['id'] == "1"
    assert result.data['updatePost']['post']['title'] == "Updated Post Title"
    assert result.data['updatePost']['post']['content'] == "This is the updated content for the post."
    assert "Updated" in result.data['updatePost']['post']['tags']
    assert "GraphQL" in result.data['updatePost']['post']['tags']
    assert result.data['updatePost']['post']['published'] is True

def test_update_post_validation():
    """Test validation when updating a post."""
    mutation = '''
    mutation {
      updatePost(
        id: "1",
        input: {
          title: "A",
          content: "Short"
        }
      ) {
        ok
        post {
          id
        }
      }
    }
    '''
    result = schema.execute(mutation)
    assert result.errors  # We expect validation errors