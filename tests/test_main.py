"""
Tests for the main module.
"""
import pytest
from datetime import datetime

from app.main import get_greeting, display_greeting


def test_get_greeting_default():
    """Test the get_greeting function with default parameters."""
    greeting = get_greeting()
    
    assert isinstance(greeting, dict)
    assert greeting["message"] == "Hello, World!"
    assert isinstance(greeting["timestamp"], str)
    # Verify the timestamp is in ISO format
    datetime.fromisoformat(greeting["timestamp"])


def test_get_greeting_custom_name():
    """Test the get_greeting function with a custom name."""
    name = "Python"
    greeting = get_greeting(name)
    
    assert isinstance(greeting, dict)
    assert greeting["message"] == f"Hello, {name}!"
    assert isinstance(greeting["timestamp"], str)


def test_display_greeting(capsys):
    """Test the display_greeting function with a mock greeting."""
    mock_timestamp = "2023-09-28T12:34:56.789012"
    mock_greeting = {
        "message": "Hello, Test!",
        "timestamp": mock_timestamp
    }
    
    display_greeting(mock_greeting)
    
    captured = capsys.readouterr()
    assert "Hello, Test!" in captured.out
    assert f"Generated at: {mock_timestamp}" in captured.out