"""
Flask application setup.

This module initializes the Flask application and sets up the GraphQL endpoint.
"""

from flask import Flask, jsonify
from flask_graphql import GraphQLView
from app.schema import schema

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Configure the application
    app.config['DEBUG'] = True
    app.config['TESTING'] = False

    # Register the GraphQL endpoint
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # Enable the GraphiQL interface
        )
    )

    # Add a basic route for the root path
    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to the GraphQL API",
            "graphql_endpoint": "/graphql",
            "docs": "Visit /graphql to use the GraphiQL interface"
        })

    return app