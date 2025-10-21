# CLI Demo Application

A demonstration project showcasing how to build a FastAPI application with a corresponding CLI tool. This project serves as a learning resource for understanding how to create powerful command-line interfaces that interact with web APIs.

## Features

- **REST API**: Built with FastAPI, providing endpoints for managing users and tasks
- **CLI Tool**: A Typer-based command-line interface that interacts with the API
- **Data Validation**: Using Pydantic models for consistent data validation
- **Rich Output**: Formatted terminal output using the Rich library
- **Documentation**: Comprehensive docstrings and API documentation
- **Data Structures Guide**: Detailed explanations of Python data structures and their CLI application

## Project Structure

```
.
├── app/                    # Main application directory
│   ├── main.py             # FastAPI application entry point
│   ├── models.py           # Pydantic models for data validation
│   ├── cli.py              # CLI implementation using Typer
│   └── database.py         # Mock database functionality
├── cli.py                  # CLI tool entry point
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── CLI_USAGE.md            # CLI usage documentation
├── ARCHITECTURE.md         # Application architecture documentation
└── DATA_STRUCTURES.md      # Python data structures guide
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/LuvJain/test-abc.git
   cd test-abc
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

You can access the automatically generated API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Using the CLI Tool

The CLI tool can be used to interact with the API. Here are some examples:

#### Display help information

```bash
python cli.py --help
```

#### About the CLI tool

```bash
python cli.py about
```

#### Create a new user

```bash
python cli.py user-create --username john_doe --email john@example.com --role user --full-name "John Doe" --age 30
```

You can also use the interactive prompt:

```bash
python cli.py user-create
```

#### List all users

```bash
python cli.py user-list
```

#### Show a specific user

```bash
python cli.py user-show 1
```

#### Create a new task

```bash
python cli.py task-create --title "Complete documentation" --description "Write comprehensive docs for the CLI app"
```

#### List all tasks

```bash
python cli.py task-list
```

#### Show a specific task

```bash
python cli.py task-show 1
```

#### Update a task

```bash
python cli.py task-update 1 --title "Updated title" --completed true
```

#### Mark a task as completed

```bash
python cli.py task-complete 1
```

### Output Formats

All commands support different output formats:

- `--format table` (default): Displays data in a formatted table
- `--format json`: Outputs raw JSON data

Example:
```bash
python cli.py user-list --format json
```

## API Endpoints

### Users

- `GET /users/`: List all users
- `POST /users/`: Create a new user
- `GET /users/{user_id}`: Get a specific user

### Tasks

- `GET /tasks/`: List all tasks (query param: `completed`)
- `POST /tasks/`: Create a new task
- `GET /tasks/{task_id}`: Get a specific task
- `PUT /tasks/{task_id}`: Update a task

## Data Models

### User

- `username`: String (3-50 characters)
- `email`: String (valid email format)
- `role`: Enum (admin, user, guest)
- `full_name`: String (optional)
- `age`: Integer (optional, 1-119)

### Task

- `title`: String (1-100 characters)
- `description`: String (optional)
- `completed`: Boolean

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and settings management
- [Typer](https://typer.tiangolo.com/) - Library for building CLI applications
- [Rich](https://rich.readthedocs.io/) - Terminal formatting and styling
- [httpx](https://www.python-httpx.org/) - HTTP client for Python

## Development

### Python Data Structures Guide

This project includes a comprehensive guide on Python data structures and their application in CLI tools. The guide covers:

- **Basic Data Structures**: Lists, tuples, dictionaries, and sets
- **Advanced Data Structures**: Collections module, arrays, and custom data classes
- **CLI Application**: Examples of using data structures for command-line arguments, configuration, and data processing
- **Best Practices**: Guidelines for choosing the right data structure and performance considerations

To learn more about Python data structures and how to use them effectively in your CLI applications, see the [Data Structures Guide](DATA_STRUCTURES.md).

### Adding New Commands

To add a new command to the CLI tool:

1. Define a new function in `app/cli.py`
2. Decorate it with `@app.command()`
3. Implement the command functionality

Example:
```python
@app.command("new-command")
def new_command(
    param: str = typer.Option(..., help="Parameter description"),
):
    """Command description."""
    # Command implementation
```

### Adding New API Endpoints

To add a new endpoint to the API:

1. Define a new function in `app/main.py`
2. Decorate it with the appropriate FastAPI decorator (e.g., `@app.get()`, `@app.post()`)
3. Implement the endpoint functionality

Example:
```python
@app.get("/new-endpoint/", tags=["Category"])
async def new_endpoint():
    """Endpoint description."""
    # Endpoint implementation
```

## License

This project is licensed under the MIT License.