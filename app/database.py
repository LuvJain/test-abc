"""
Mock database module for the application.

This module provides simple in-memory storage and retrieval functions
to simulate database operations.
"""

from typing import Dict, List, Optional
from app.models import UserInput, UserOutput, TaskInput, TaskOutput

# In-memory storage
_users: Dict[int, UserOutput] = {}
_tasks: Dict[int, TaskOutput] = {}

# Counters for generating IDs
_user_counter = 0
_task_counter = 0


def create_user(user_input: UserInput) -> UserOutput:
    """
    Create a new user in the database.

    Args:
        user_input: User data to be stored

    Returns:
        UserOutput: The created user with an assigned ID
    """
    global _user_counter
    _user_counter += 1

    user_output = UserOutput(
        id=_user_counter,
        username=user_input.username,
        email=user_input.email,
        role=user_input.role,
        full_name=user_input.full_name,
        age=user_input.age
    )

    _users[_user_counter] = user_output
    return user_output


def get_user(user_id: int) -> Optional[UserOutput]:
    """
    Get a user by ID.

    Args:
        user_id: The ID of the user to retrieve

    Returns:
        UserOutput: The user if found, None otherwise
    """
    return _users.get(user_id)


def get_all_users() -> List[UserOutput]:
    """
    Get all users.

    Returns:
        List[UserOutput]: List of all users
    """
    return list(_users.values())


def create_task(task_input: TaskInput) -> TaskOutput:
    """
    Create a new task in the database.

    Args:
        task_input: Task data to be stored

    Returns:
        TaskOutput: The created task with an assigned ID
    """
    global _task_counter
    _task_counter += 1

    task_output = TaskOutput(
        id=_task_counter,
        title=task_input.title,
        description=task_input.description,
        completed=task_input.completed
    )

    _tasks[_task_counter] = task_output
    return task_output


def get_task(task_id: int) -> Optional[TaskOutput]:
    """
    Get a task by ID.

    Args:
        task_id: The ID of the task to retrieve

    Returns:
        TaskOutput: The task if found, None otherwise
    """
    return _tasks.get(task_id)


def get_all_tasks() -> List[TaskOutput]:
    """
    Get all tasks.

    Returns:
        List[TaskOutput]: List of all tasks
    """
    return list(_tasks.values())


def update_task(task_id: int, task_input: TaskInput) -> Optional[TaskOutput]:
    """
    Update a task by ID.

    Args:
        task_id: The ID of the task to update
        task_input: The new task data

    Returns:
        TaskOutput: The updated task if found, None otherwise
    """
    if task_id not in _tasks:
        return None

    task_output = TaskOutput(
        id=task_id,
        title=task_input.title,
        description=task_input.description,
        completed=task_input.completed
    )

    _tasks[task_id] = task_output
    return task_output