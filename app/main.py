"""
FastAPI application entry point.

This module defines the FastAPI application and its endpoints.
"""

from fastapi import FastAPI, HTTPException, Query, Path
from typing import List, Optional

from app.models import UserInput, UserOutput, TaskInput, TaskOutput
import app.database as db

# Create the FastAPI application
app = FastAPI(
    title="CLI Demo API",
    description="""
    A demo API that shows how to create a FastAPI application with a CLI interface.
    This API provides endpoints for managing users and tasks.

    The corresponding CLI tool allows interacting with these endpoints directly
    from the command line, demonstrating how to build intuitive command-line
    interfaces for web APIs.
    """,
    version="0.1.0",
)


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint that provides basic API information.
    """
    return {
        "message": "Welcome to the CLI Demo API!",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
    }


@app.post("/users/", response_model=UserOutput, tags=["Users"])
async def create_user(user_input: UserInput):
    """
    Create a new user.

    Args:
        user_input: User data to create

    Returns:
        UserOutput: The created user with an assigned ID
    """
    return db.create_user(user_input)


@app.get("/users/", response_model=List[UserOutput], tags=["Users"])
async def get_users():
    """
    Get all users.

    Returns:
        List[UserOutput]: List of all users
    """
    return db.get_all_users()


@app.get("/users/{user_id}", response_model=UserOutput, tags=["Users"])
async def get_user(user_id: int = Path(..., description="The ID of the user to retrieve")):
    """
    Get a user by ID.

    Args:
        user_id: The ID of the user to retrieve

    Returns:
        UserOutput: The user if found

    Raises:
        HTTPException: If the user is not found
    """
    user = db.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    return user


@app.post("/tasks/", response_model=TaskOutput, tags=["Tasks"])
async def create_task(task_input: TaskInput):
    """
    Create a new task.

    Args:
        task_input: Task data to create

    Returns:
        TaskOutput: The created task with an assigned ID
    """
    return db.create_task(task_input)


@app.get("/tasks/", response_model=List[TaskOutput], tags=["Tasks"])
async def get_tasks(completed: Optional[bool] = Query(None, description="Filter tasks by completion status")):
    """
    Get all tasks, optionally filtered by completion status.

    Args:
        completed: If provided, filter tasks by this completion status

    Returns:
        List[TaskOutput]: List of tasks matching the criteria
    """
    tasks = db.get_all_tasks()
    if completed is not None:
        tasks = [task for task in tasks if task.completed == completed]
    return tasks


@app.get("/tasks/{task_id}", response_model=TaskOutput, tags=["Tasks"])
async def get_task(task_id: int = Path(..., description="The ID of the task to retrieve")):
    """
    Get a task by ID.

    Args:
        task_id: The ID of the task to retrieve

    Returns:
        TaskOutput: The task if found

    Raises:
        HTTPException: If the task is not found
    """
    task = db.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
    return task


@app.put("/tasks/{task_id}", response_model=TaskOutput, tags=["Tasks"])
async def update_task(
    task_input: TaskInput,
    task_id: int = Path(..., description="The ID of the task to update")
):
    """
    Update a task by ID.

    Args:
        task_id: The ID of the task to update
        task_input: The new task data

    Returns:
        TaskOutput: The updated task

    Raises:
        HTTPException: If the task is not found
    """
    task = db.update_task(task_id, task_input)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
    return task


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)