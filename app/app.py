"""
Flask application setup.

This module initializes the Flask application and sets up the GraphQL endpoint.
"""

import os
from flask import Flask, jsonify, request, g
from flask_graphql import GraphQLView
from app.schema import schema
from app.middleware import (
    AuthenticationMiddleware,
    LoggingMiddleware,
    ErrorHandlingMiddleware
)
from app.auth import get_authenticated_user

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Configure the application
    app.config['DEBUG'] = True
    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-secret-key-for-jwt')

    # Setup middleware stack
    middleware = [
        ErrorHandlingMiddleware(),
        AuthenticationMiddleware(),
        LoggingMiddleware()
    ]

    # Register the GraphQL endpoint with middleware
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True,  # Enable the GraphiQL interface
            middleware=middleware,
            context={'request': request}  # Pass request to context
        )
    )

    # Setup before request handler to process authentication
    @app.before_request
    def authenticate_request():
        """Authenticate the user for the current request."""
        user = get_authenticated_user()
        if user:
            g.user = user

    # Add a basic route for the root path
    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to the GraphQL API",
            "graphql_endpoint": "/graphql",
            "docs": "Visit /graphql to use the GraphiQL interface",
            "auth_info": "Use JWT tokens in the Authorization header for authenticated requests"
        })

    return app