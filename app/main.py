#!/usr/bin/env python3
"""
Simple Hello World application to demonstrate Python basics.
"""
from typing import Dict, Any
import logging
from datetime import datetime


# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_greeting(name: str = "World") -> Dict[str, Any]:
    """
    Generate a greeting message with timestamp.
    
    Args:
        name: The name to greet. Defaults to "World".
        
    Returns:
        A dictionary containing the greeting message and timestamp.
    """
    logger.info(f"Generating greeting for {name}")
    return {
        "message": f"Hello, {name}!",
        "timestamp": datetime.now().isoformat()
    }


def display_greeting(greeting_data: Dict[str, Any]) -> None:
    """
    Display the greeting information.
    
    Args:
        greeting_data: Dictionary containing greeting message and timestamp.
    """
    print(f"\n{greeting_data['message']}")
    print(f"Generated at: {greeting_data['timestamp']}\n")


def main() -> None:
    """
    Main entry point of the application.
    """
    logger.info("Application started")
    greeting = get_greeting()
    display_greeting(greeting)
    logger.info("Application completed")


if __name__ == "__main__":
    main()