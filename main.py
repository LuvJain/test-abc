"""
Main application entry point.

This script initializes and runs the Flask application with the GraphQL endpoint.
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting GraphQL server...")
    print("GraphiQL UI is available at: http://127.0.0.1:5000/graphql")
    app.run(host='0.0.0.0', port=5000)