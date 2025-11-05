"""
Models package initialization.
"""
from app.models.models import (
    Author,
    Book,
    User,
    Post,
    get_author_by_id,
    get_book_by_id,
    get_books_by_author_id,
    get_all_books,
    get_all_authors,
    get_user_by_id,
    get_post_by_id,
    get_posts_by_user_id,
    get_all_users,
    get_all_posts,
    get_posts_by_tag,
    get_posts_paginated,
    add_user,
    add_post,
    update_post,
)