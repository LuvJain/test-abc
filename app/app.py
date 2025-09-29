"""
Simple web application to demonstrate basic web functionality.
This is a minimal example that can be extended with actual web frameworks.
"""
from typing import Dict, Any, List, Optional
import json
from datetime import datetime

from app.models import Greeting


class SimpleApp:
    """
    A simple application class to demonstrate basic application structure.
    """
    
    def __init__(self, name: str = "Hello World App"):
        """
        Initialize the application.
        
        Args:
            name: The name of the application.
        """
        self.name = name
        self.started_at = datetime.now()
        self.requests: List[Dict[str, Any]] = []
    
    def handle_request(self, path: str, query_params: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Handle a simple request.
        
        Args:
            path: The request path.
            query_params: Optional query parameters.
            
        Returns:
            A response dictionary.
        """
        query_params = query_params or {}
        
        # Record the request
        request_record = {
            "path": path,
            "query_params": query_params,
            "timestamp": datetime.now().isoformat()
        }
        self.requests.append(request_record)
        
        # Simple routing
        if path == "/":
            name = query_params.get("name", "World")
            greeting = Greeting(recipient=name)
            return {
                "status": "success",
                "data": greeting.to_dict()
            }
        elif path == "/about":
            return {
                "status": "success",
                "data": {
                    "app_name": self.name,
                    "uptime_seconds": (datetime.now() - self.started_at).total_seconds(),
                    "request_count": len(self.requests)
                }
            }
        else:
            return {
                "status": "error",
                "message": f"Path {path} not found"
            }
    
    def __str__(self) -> str:
        return f"{self.name} (running since {self.started_at.isoformat()})"


def create_app() -> SimpleApp:
    """
    Factory function to create a new application instance.
    
    Returns:
        A new SimpleApp instance.
    """
    return SimpleApp()


# Example usage
if __name__ == "__main__":
    app = create_app()
    
    # Simulate some requests
    responses = [
        app.handle_request("/"),
        app.handle_request("/", {"name": "Python Learner"}),
        app.handle_request("/about")
    ]
    
    # Print the responses
    for i, response in enumerate(responses, 1):
        print(f"\nRequest {i} response:")
        print(json.dumps(response, indent=2))