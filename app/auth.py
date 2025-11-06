"""
Authentication and authorization utilities for GraphQL.

This module provides decorators and utilities for implementing authentication
and authorization in GraphQL resolvers.
"""

import functools
import logging
from flask import request, g
from graphql import GraphQLError
from app.models import (
    get_user_by_token,
    UserRole,
    logger as auth_logger,
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('graphql_auth')

def get_authenticated_user():
    """
    Get the authenticated user from the request.

    This function checks for an Authorization header in the request,
    validates the JWT token, and returns the authenticated user.

    Returns:
        User: The authenticated user or None if authentication failed.
    """
    # Check if we've already authenticated this request
    if hasattr(g, 'user'):
        return g.user

    # Get the Authorization header
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        logger.info("Request missing Authorization header")
        return None

    # Check if it's a Bearer token
    parts = auth_header.split()
    if len(parts) != 2 or parts[0].lower() != 'bearer':
        logger.warning(f"Invalid Authorization header format: {auth_header}")
        return None

    token = parts[1]

    # Validate the token and get the user
    user = get_user_by_token(token)

    # Store in Flask global to avoid authenticating again for the same request
    if user:
        g.user = user

    return user

def require_auth(func):
    """
    Decorator that requires authentication for a resolver.

    Args:
        func (callable): The resolver function to decorate.

    Returns:
        callable: The decorated resolver function.

    Raises:
        GraphQLError: If authentication fails.
    """
    @functools.wraps(func)
    def wrapper(parent, info, *args, **kwargs):
        # Check if user is authenticated
        user = get_authenticated_user()

        if not user:
            auth_logger.warning(f"Unauthorized access attempt to {func.__name__}")
            raise GraphQLError("Authentication required")

        # Add the user to the context for the resolver
        info.context['user'] = user
        logger.info(f"User {user.username} (ID: {user.id}) authenticated for {func.__name__}")

        # Call the resolver
        return func(parent, info, *args, **kwargs)

    return wrapper

def require_role(roles):
    """
    Decorator that requires specific role(s) for a resolver.

    Args:
        roles (list|UserRole): The required role(s) for accessing the resolver.

    Returns:
        callable: A decorator function.

    Raises:
        GraphQLError: If authorization fails.
    """
    if not isinstance(roles, list):
        roles = [roles]

    def decorator(func):
        @functools.wraps(func)
        def wrapper(parent, info, *args, **kwargs):
            # First check if user is authenticated
            user = get_authenticated_user()

            if not user:
                auth_logger.warning(f"Unauthorized access attempt to {func.__name__}")
                raise GraphQLError("Authentication required")

            # Check if user has the required role
            if user.role not in roles:
                auth_logger.warning(
                    f"Authorization failure: User {user.username} (ID: {user.id}) with role "
                    f"{user.role.value} attempted to access {func.__name__} which requires "
                    f"one of these roles: {[r.value for r in roles]}"
                )
                raise GraphQLError("You don't have permission to perform this action")

            # Add the user to the context for the resolver
            info.context['user'] = user
            logger.info(f"User {user.username} (ID: {user.id}, Role: {user.role.value}) authorized for {func.__name__}")

            # Call the resolver
            return func(parent, info, *args, **kwargs)

        return wrapper

    return decorator

def user_owns_resource(get_owner_id):
    """
    Decorator that ensures a user can only access their own resources.

    Args:
        get_owner_id (callable): A function that gets the owner ID from the parent object.

    Returns:
        callable: A decorator function.

    Raises:
        GraphQLError: If authorization fails.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(parent, info, *args, **kwargs):
            # First check if user is authenticated
            user = get_authenticated_user()

            if not user:
                auth_logger.warning(f"Unauthorized access attempt to {func.__name__}")
                raise GraphQLError("Authentication required")

            # Admin and Editor roles can access any resource
            if user.role in [UserRole.ADMIN, UserRole.EDITOR]:
                info.context['user'] = user
                return func(parent, info, *args, **kwargs)

            # Get the owner ID of the resource
            owner_id = get_owner_id(parent)

            # Check if the user is the owner
            if user.id != owner_id:
                auth_logger.warning(
                    f"Authorization failure: User {user.username} (ID: {user.id}) attempted to "
                    f"access resource owned by user {owner_id}"
                )
                raise GraphQLError("You don't have permission to access this resource")

            # Add the user to the context for the resolver
            info.context['user'] = user

            # Call the resolver
            return func(parent, info, *args, **kwargs)

        return wrapper

    return decorator