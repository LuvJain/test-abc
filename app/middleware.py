"""
Middleware for GraphQL requests.

This module contains middleware functions for processing GraphQL requests.
"""

import json
import time
import logging
from flask import request, g
from graphql import GraphQLError
from app.auth import get_authenticated_user
from app.models import logger as auth_logger

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('graphql_middleware')

class AuthenticationMiddleware:
    """
    Middleware that processes authentication for GraphQL requests.

    This middleware checks for an Authorization header and authenticates the user.
    """

    def resolve(self, next, root, info, **args):
        """
        Process the GraphQL request to authenticate the user.

        Args:
            next (callable): The next resolver in the chain.
            root (any): The root value.
            info (ResolveInfo): The resolve info.
            **args: The arguments passed to the resolver.

        Returns:
            any: The result of the next resolver.
        """
        # Try to authenticate the user
        user = get_authenticated_user()

        # Add user to context if authenticated
        if user:
            info.context['user'] = user
            logger.info(f"Request authenticated as user: {user.username} (ID: {user.id}, Role: {user.role.value})")
        else:
            logger.info("Unauthenticated request")

        # Continue the resolver chain
        return next(root, info, **args)

class LoggingMiddleware:
    """
    Middleware that logs GraphQL request information.

    This middleware logs information about each GraphQL request for security monitoring.
    """

    def resolve(self, next, root, info, **args):
        """
        Process the GraphQL request to log information.

        Args:
            next (callable): The next resolver in the chain.
            root (any): The root value.
            info (ResolveInfo): The resolve info.
            **args: The arguments passed to the resolver.

        Returns:
            any: The result of the next resolver.
        """
        operation_name = info.operation.name.value if info.operation.name else "anonymous"
        field_name = info.field_name

        # Log the request
        logger.info(
            f"GraphQL Request: operation={operation_name}, field={field_name}, "
            f"path={info.path}, ip={request.remote_addr}"
        )

        # Record start time
        start_time = time.time()

        # Get authenticated user if any
        user = getattr(g, 'user', None)
        user_info = f"user={user.username}, id={user.id}" if user else "unauthenticated"

        # Execute the resolver
        try:
            result = next(root, info, **args)
            # Log successful execution
            elapsed_time = time.time() - start_time
            logger.info(
                f"GraphQL Success: operation={operation_name}, field={field_name}, "
                f"{user_info}, time={elapsed_time:.4f}s"
            )
            return result
        except GraphQLError as e:
            # Log GraphQL errors
            elapsed_time = time.time() - start_time
            logger.warning(
                f"GraphQL Error: operation={operation_name}, field={field_name}, "
                f"{user_info}, time={elapsed_time:.4f}s, error={str(e)}"
            )
            raise
        except Exception as e:
            # Log unexpected errors
            elapsed_time = time.time() - start_time
            logger.error(
                f"GraphQL Exception: operation={operation_name}, field={field_name}, "
                f"{user_info}, time={elapsed_time:.4f}s, error={str(e)}"
            )
            # Convert to GraphQL error for better client handling
            auth_logger.error(f"Unexpected error in resolver: {str(e)}")
            raise GraphQLError(f"An unexpected error occurred: {str(e)}")

class ErrorHandlingMiddleware:
    """
    Middleware that handles errors in GraphQL resolvers.

    This middleware provides consistent error handling for GraphQL resolvers.
    """

    def resolve(self, next, root, info, **args):
        """
        Process the GraphQL request to handle errors.

        Args:
            next (callable): The next resolver in the chain.
            root (any): The root value.
            info (ResolveInfo): The resolve info.
            **args: The arguments passed to the resolver.

        Returns:
            any: The result of the next resolver.

        Raises:
            GraphQLError: A formatted error for the client.
        """
        try:
            return next(root, info, **args)
        except GraphQLError:
            # Pass GraphQL errors through (already formatted)
            raise
        except ValueError as e:
            # Convert ValueError to GraphQL error
            auth_logger.warning(f"Validation error in resolver: {str(e)}")
            raise GraphQLError(str(e), extensions={"code": "VALIDATION_ERROR"})
        except PermissionError as e:
            # Convert PermissionError to GraphQL error
            auth_logger.warning(f"Permission error in resolver: {str(e)}")
            raise GraphQLError(str(e), extensions={"code": "FORBIDDEN"})
        except Exception as e:
            # Convert other exceptions to GraphQL error
            auth_logger.error(f"Unexpected error in resolver: {str(e)}")
            raise GraphQLError("An internal error occurred", extensions={"code": "INTERNAL_SERVER_ERROR"})