"""
Tests for the models module.
"""
import pytest
from datetime import datetime

from app.models import Greeting


def test_greeting_default_values():
    """Test the Greeting class with default values."""
    recipient = "World"
    greeting = Greeting(recipient=recipient)
    
    assert greeting.recipient == recipient
    assert greeting.message == "Hello"
    assert isinstance(greeting.timestamp, datetime)
    assert greeting.metadata is None


def test_greeting_custom_values():
    """Test the Greeting class with custom values."""
    recipient = "Python"
    message = "Hi"
    timestamp = datetime(2023, 9, 28, 12, 34, 56)
    metadata = {"version": "1.0.0", "language": "en"}
    
    greeting = Greeting(
        recipient=recipient,
        message=message,
        timestamp=timestamp,
        metadata=metadata
    )
    
    assert greeting.recipient == recipient
    assert greeting.message == message
    assert greeting.timestamp == timestamp
    assert greeting.metadata == metadata


def test_greeting_format_greeting():
    """Test the format_greeting method."""
    recipient = "Python"
    message = "Hi"
    
    greeting = Greeting(recipient=recipient, message=message)
    formatted = greeting.format_greeting()
    
    assert formatted == f"{message}, {recipient}!"


def test_greeting_to_dict():
    """Test the to_dict method."""
    recipient = "Python"
    message = "Hi"
    timestamp = datetime(2023, 9, 28, 12, 34, 56)
    metadata = {"version": "1.0.0"}
    
    greeting = Greeting(
        recipient=recipient,
        message=message,
        timestamp=timestamp,
        metadata=metadata
    )
    
    result = greeting.to_dict()
    
    assert result["recipient"] == recipient
    assert result["message"] == message
    assert result["timestamp"] == timestamp.isoformat()
    assert result["metadata"] == metadata


def test_greeting_to_dict_empty_metadata():
    """Test the to_dict method with no metadata."""
    recipient = "Python"
    
    greeting = Greeting(recipient=recipient)
    result = greeting.to_dict()
    
    assert result["metadata"] == {}