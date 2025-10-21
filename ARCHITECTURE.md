# Application Architecture

This document outlines the architecture and design decisions of the CLI Demo application.

## Overview

The CLI Demo application consists of two main components:

1. **REST API**: A FastAPI-based web API that provides endpoints for managing users and tasks.
2. **CLI Tool**: A Typer-based command-line interface that interacts with the API.

## System Architecture

```
┌─────────────────┐      HTTP      ┌─────────────────┐
│                 │    Requests     │                 │
│    CLI Tool     │◄──────────────►│    REST API     │
│    (Typer)      │                 │    (FastAPI)    │
│                 │                 │                 │
└─────────────────┘                 └─────────────────┘
        │                                    │
        │                                    │
        ▼                                    ▼
┌─────────────────┐                 ┌─────────────────┐
│                 │                 │                 │
│  Rich Output    │                 │  Mock Database  │
│  (Terminal UI)  │                 │  (In-memory)    │
│                 │                 │                 │
└─────────────────┘                 └─────────────────┘
```

## Component Design

### REST API (FastAPI)

The REST API is built with FastAPI, a modern, fast web framework for building APIs with Python. It features automatic validation, serialization, and documentation.

#### Key Components:

1. **Models** (`app/models.py`):
   - Pydantic models for data validation and serialization
   - Defines the structure and constraints for user and task data

2. **Database** (`app/database.py`):
   - Mock in-memory database for storing users and tasks
   - Provides CRUD operations for users and tasks

3. **API Endpoints** (`app/main.py`):
   - FastAPI application entry point
   - Defines API endpoints for users and tasks
   - Handles HTTP requests and responses

#### API Endpoints:

- **Users**:
  - `GET /users/`: List all users
  - `POST /users/`: Create a new user
  - `GET /users/{user_id}`: Get a specific user

- **Tasks**:
  - `GET /tasks/`: List all tasks
  - `POST /tasks/`: Create a new task
  - `GET /tasks/{task_id}`: Get a specific task
  - `PUT /tasks/{task_id}`: Update a task

### CLI Tool (Typer)

The CLI tool is built with Typer, a library for building CLI applications with Python. It provides a clean and intuitive interface for interacting with the API.

#### Key Components:

1. **CLI Commands** (`app/cli.py`):
   - Typer application entry point
   - Defines commands for users and tasks
   - Handles command-line arguments and options

2. **API Client Functions** (`app/cli.py`):
   - Functions for making HTTP requests to the API
   - Handles serialization and deserialization of data

3. **Output Formatting** (`app/cli.py`):
   - Uses Rich library for formatting terminal output
   - Supports table and JSON output formats

#### CLI Commands:

- **Users**:
  - `user-create`: Create a new user
  - `user-list`: List all users
  - `user-show`: Show a specific user

- **Tasks**:
  - `task-create`: Create a new task
  - `task-list`: List all tasks
  - `task-show`: Show a specific task
  - `task-update`: Update a task
  - `task-complete`: Mark a task as completed

## Data Flow

### Creating a User:

1. User runs `python cli.py user-create` with appropriate arguments
2. CLI tool validates input and creates a `UserInput` object
3. CLI tool sends a POST request to `/users/` endpoint with the user data
4. API validates the input using the `UserInput` model
5. API creates a new user in the mock database
6. API returns the created user as a `UserOutput` object
7. CLI tool formats and displays the user data

### Listing Tasks:

1. User runs `python cli.py task-list`
2. CLI tool sends a GET request to `/tasks/` endpoint
3. API retrieves all tasks from the mock database
4. API returns the tasks as a list of `TaskOutput` objects
5. CLI tool formats and displays the task data

## Design Decisions

### Using FastAPI for the API

FastAPI was chosen for the API for several reasons:

- **Automatic Validation**: FastAPI uses Pydantic models for validation
- **Type Annotations**: Leverages Python type hints for better code quality
- **Performance**: Built on Starlette and Uvicorn for high performance
- **Documentation**: Automatic generation of OpenAPI documentation

### Using Typer for the CLI Tool

Typer was chosen for the CLI tool for several reasons:

- **Type Annotations**: Leverages Python type hints for better code quality
- **Automatic Help**: Generates help messages from type annotations and docstrings
- **Intuitive API**: Similar API to FastAPI, making it easy to learn
- **Interactive Prompts**: Supports interactive prompts for required arguments

### Using Rich for Output Formatting

Rich was chosen for output formatting for several reasons:

- **Beautiful Tables**: Rich provides beautiful, customizable tables
- **Colors and Styles**: Supports ANSI colors and styles for better UX
- **Markdown Support**: Renders Markdown for documentation display

### Using a Mock Database

A mock in-memory database was chosen for simplicity. In a real-world application, this would be replaced with a proper database like PostgreSQL or MongoDB.

## Future Improvements

1. **Authentication**: Add user authentication and authorization
2. **Real Database**: Replace mock database with a real database
3. **Pagination**: Add pagination for listing endpoints
4. **Testing**: Add unit and integration tests
5. **Configuration**: Add configuration management
6. **Logging**: Add proper logging
7. **Error Handling**: Improve error handling
8. **Caching**: Add caching for improved performance

## Conclusion

The CLI Demo application demonstrates how to build a modern API with FastAPI and a corresponding CLI tool with Typer. It shows how to use Pydantic models for validation, Rich for output formatting, and how to structure a Python application for clarity and maintainability.