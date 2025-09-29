"""
Models module for the Hello World application.
This demonstrates simple class structure in Python.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Greeting:
    """
    A class representing a greeting message.
    
    Attributes:
        message: The greeting message.
        recipient: The recipient of the greeting.
        timestamp: When the greeting was created.
        metadata: Additional information about the greeting.
    """
    recipient: str
    message: str = "Hello"
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Optional[Dict[str, Any]] = None
    
    def format_greeting(self) -> str:
        """
        Format the greeting as a string.
        
        Returns:
            A formatted greeting string.
        """
        return f"{self.message}, {self.recipient}!"
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the greeting to a dictionary.
        
        Returns:
            Dictionary representation of the greeting.
        """
        return {
            "message": self.message,
            "recipient": self.recipient,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata or {}
        }