"""
Tests for the app module.
"""
import pytest

from app.app import SimpleApp, create_app


def test_create_app():
    """Test the create_app factory function."""
    app = create_app()
    
    assert isinstance(app, SimpleApp)
    assert app.name == "Hello World App"
    assert len(app.requests) == 0


def test_app_handle_request_root():
    """Test handling requests to the root path."""
    app = create_app()
    
    # Test with default name
    response = app.handle_request("/")
    assert response["status"] == "success"
    assert "data" in response
    assert response["data"]["message"] == "Hello"
    assert response["data"]["recipient"] == "World"
    
    # Test with custom name
    response = app.handle_request("/", {"name": "Python"})
    assert response["status"] == "success"
    assert "data" in response
    assert response["data"]["message"] == "Hello"
    assert response["data"]["recipient"] == "Python"
    
    # Verify requests were recorded
    assert len(app.requests) == 2
    assert app.requests[0]["path"] == "/"
    assert app.requests[1]["path"] == "/"
    assert app.requests[1]["query_params"]["name"] == "Python"


def test_app_handle_request_about():
    """Test handling requests to the about path."""
    app = create_app()
    
    response = app.handle_request("/about")
    assert response["status"] == "success"
    assert "data" in response
    assert response["data"]["app_name"] == "Hello World App"
    assert response["data"]["request_count"] == 1
    assert isinstance(response["data"]["uptime_seconds"], float)


def test_app_handle_request_not_found():
    """Test handling requests to an unknown path."""
    app = create_app()
    
    response = app.handle_request("/not-found")
    assert response["status"] == "error"
    assert "message" in response
    assert "not found" in response["message"]