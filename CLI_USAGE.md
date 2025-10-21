# CLI Tool Usage Guide

This document provides detailed information on using the CLI tool for interacting with the API.

## Overview

The CLI tool is a command-line interface built with Typer that allows you to interact with the REST API. It provides commands for managing users and tasks, with options for formatting the output.

For a detailed guide on Python data structures and their application in CLI tools, see the [Data Structures Guide](DATA_STRUCTURES.md).

## Installation

Make sure you have installed the project dependencies:

```bash
pip install -r requirements.txt
```

## Basic Usage

The CLI tool can be run using Python:

```bash
python cli.py [COMMAND] [OPTIONS]
```

To see a list of available commands:

```bash
python cli.py --help
```

## Available Commands

### General Commands

#### `about`

Display information about the CLI tool.

```bash
python cli.py about
```

### User Management

#### `user-create`

Create a new user.

```bash
python cli.py user-create --username john_doe --email john@example.com --role user --full-name "John Doe" --age 30
```

Options:
- `--username TEXT`: Username (3-50 characters) [required]
- `--email TEXT`: Email address [required]
- `--role [admin|user|guest]`: User role [default: user]
- `--full-name TEXT`: Full name
- `--age INTEGER`: Age (1-119)
- `--format [table|json]`: Output format [default: table]

You can also use the interactive prompt:

```bash
python cli.py user-create
```

The tool will prompt you for the required fields.

#### `user-list`

List all users.

```bash
python cli.py user-list
```

Options:
- `--format [table|json]`: Output format [default: table]

#### `user-show`

Show details for a specific user.

```bash
python cli.py user-show 1
```

Arguments:
- `USER_ID`: User ID [required]

Options:
- `--format [table|json]`: Output format [default: table]

### Task Management

#### `task-create`

Create a new task.

```bash
python cli.py task-create --title "Complete documentation" --description "Write comprehensive docs for the CLI app"
```

Options:
- `--title TEXT`: Task title (1-100 characters) [required]
- `--description TEXT`: Task description
- `--completed / --no-completed`: Task completion status [default: False]
- `--format [table|json]`: Output format [default: table]

You can also use the interactive prompt:

```bash
python cli.py task-create
```

#### `task-list`

List all tasks, optionally filtered by completion status.

```bash
python cli.py task-list
```

Options:
- `--completed / --no-completed`: Filter by completion status
- `--format [table|json]`: Output format [default: table]

Examples:
```bash
# List all tasks
python cli.py task-list

# List only completed tasks
python cli.py task-list --completed

# List only pending tasks
python cli.py task-list --no-completed
```

#### `task-show`

Show details for a specific task.

```bash
python cli.py task-show 1
```

Arguments:
- `TASK_ID`: Task ID [required]

Options:
- `--format [table|json]`: Output format [default: table]

#### `task-update`

Update an existing task.

```bash
python cli.py task-update 1 --title "Updated title" --completed
```

Arguments:
- `TASK_ID`: Task ID [required]

Options:
- `--title TEXT`: New task title (1-100 characters)
- `--description TEXT`: New task description
- `--completed / --no-completed`: New task completion status
- `--format [table|json]`: Output format [default: table]

#### `task-complete`

Mark a task as completed.

```bash
python cli.py task-complete 1
```

Arguments:
- `TASK_ID`: Task ID [required]

## Output Formats

All commands support different output formats:

- `--format table` (default): Displays data in a rich formatted table
- `--format json`: Outputs raw JSON data

Example:
```bash
python cli.py user-list --format json
```

## Error Handling

The CLI tool provides clear error messages for common issues:

- If the API server is not running, you'll see an error indicating the connection failed.
- If a user or task is not found, you'll see an error message specifying the ID that wasn't found.
- If input validation fails, you'll see detailed error messages about the validation issues.

## Examples

### Creating and listing users

```bash
# Create a new user
python cli.py user-create --username alice --email alice@example.com

# List all users
python cli.py user-list
```

### Managing tasks

```bash
# Create a new task
python cli.py task-create --title "Learn Python" --description "Complete Python tutorial"

# List all tasks
python cli.py task-list

# Mark a task as completed
python cli.py task-complete 1

# List only completed tasks
python cli.py task-list --completed
```

### Using JSON output

```bash
# Get user details in JSON format
python cli.py user-show 1 --format json

# List all tasks in JSON format
python cli.py task-list --format json
```

## Working with the API Server

The CLI tool assumes the API server is running at http://localhost:8000. Make sure to start the API server before using the CLI:

```bash
uvicorn app.main:app --reload
```

## Troubleshooting

### Connection Errors

If you see connection errors when using the CLI tool, make sure the API server is running:

```bash
uvicorn app.main:app --reload
```

### Input Validation Errors

If your input doesn't meet the validation requirements (e.g., username too short, invalid email), the CLI will show detailed error messages. Adjust your input according to the error messages.

### Command Not Found

If a command is not recognized, check the available commands using:

```bash
python cli.py --help
```

## Advanced Usage

### Combining Commands with Shell Tools

You can use the CLI tool with other shell tools. For example, to save the JSON output of a command to a file:

```bash
python cli.py user-list --format json > users.json
```

Or to filter and process the output using `jq`:

```bash
python cli.py task-list --format json | jq '.[] | select(.completed == true)'
```

### Understanding Data Structures in the CLI

The CLI tool uses various Python data structures to efficiently manage and process data:

- **Lists and Tuples**: For handling collections of items and returning multiple values
- **Dictionaries**: For structured configuration and parameter handling
- **Sets**: For managing unique values and efficient lookups
- **Custom Data Classes**: For creating structured, type-safe data models
- **Collections Module**: For specialized containers like OrderedDict and defaultdict

To learn more about how these data structures are used in CLI applications and how to leverage them in your own code, refer to the [Data Structures Guide](DATA_STRUCTURES.md). This guide includes practical examples specifically tailored for CLI applications.

## Next Steps

- Learn how to add new commands by examining the code in `app/cli.py`
- Explore the API documentation at http://localhost:8000/docs
- Study the [Data Structures Guide](DATA_STRUCTURES.md) to better understand how to build efficient CLI applications