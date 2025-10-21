"""
Models for the FastAPI and CLI application.

This module contains Pydantic models used for data validation and serialization
in both the FastAPI application and the CLI interface.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from enum import Enum


class UserRole(str, Enum):
    """Enumeration of possible user roles."""
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class UserInput(BaseModel):
    """
    Model for user input data.

    This model is used to validate and parse user input data from both
    the API and the CLI interface.
    """
    username: str = Field(...,
                          description="User's unique identifier",
                          min_length=3,
                          max_length=50)
    email: str = Field(...,
                       description="User's email address")
    role: UserRole = Field(default=UserRole.USER,
                           description="User's role in the system")
    full_name: Optional[str] = Field(None,
                                    description="User's full name")
    age: Optional[int] = Field(None,
                              description="User's age",
                              gt=0,
                              lt=120)

    class Config:
        """Configuration for the Pydantic model."""
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "john.doe@example.com",
                "role": "user",
                "full_name": "John Doe",
                "age": 30
            }
        }


class UserOutput(BaseModel):
    """
    Model for user output data.

    This model represents the data structure returned to the client
    after successful processing of user input.
    """
    id: int = Field(..., description="Unique identifier for the user")
    username: str = Field(..., description="User's unique identifier")
    email: str = Field(..., description="User's email address")
    role: UserRole = Field(..., description="User's role in the system")
    full_name: Optional[str] = Field(None, description="User's full name")
    age: Optional[int] = Field(None, description="User's age")

    class Config:
        """Configuration for the Pydantic model."""
        schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email": "john.doe@example.com",
                "role": "user",
                "full_name": "John Doe",
                "age": 30
            }
        }


class TaskInput(BaseModel):
    """
    Model for task input data.

    This model is used to validate and parse task input data from both
    the API and the CLI interface.
    """
    title: str = Field(...,
                       description="Task title",
                       min_length=1,
                       max_length=100)
    description: Optional[str] = Field(None,
                                      description="Task description")
    completed: bool = Field(default=False,
                           description="Task completion status")

    class Config:
        """Configuration for the Pydantic model."""
        schema_extra = {
            "example": {
                "title": "Complete project documentation",
                "description": "Write comprehensive docs for the CLI application",
                "completed": False
            }
        }


class TaskOutput(BaseModel):
    """
    Model for task output data.

    This model represents the data structure returned to the client
    after successful processing of task input.
    """
    id: int = Field(..., description="Unique identifier for the task")
    title: str = Field(..., description="Task title")
    description: Optional[str] = Field(None, description="Task description")
    completed: bool = Field(..., description="Task completion status")

    class Config:
        """Configuration for the Pydantic model."""
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Complete project documentation",
                "description": "Write comprehensive docs for the CLI application",
                "completed": False
            }
        }