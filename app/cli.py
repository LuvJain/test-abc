"""
Command-line interface for the application.

This module implements a CLI tool that interacts with the API.
It demonstrates how to build intuitive command-line interfaces
for web APIs using Typer, Rich, and Pydantic.
"""

import typer
from typing import Optional, List
from enum import Enum
import json
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from rich.panel import Panel
from rich.markdown import Markdown
import httpx
import asyncio

from app.models import UserInput, UserOutput, TaskInput, TaskOutput, UserRole

# Create Typer app
app = typer.Typer(
    name="cli-demo",
    help="A CLI tool for interacting with the CLI Demo API.",
    add_completion=False,
)

# Create console for rich output
console = Console()

# Base URL for API
API_BASE_URL = "http://localhost:8000"


class OutputFormat(str, Enum):
    """Output format options for CLI commands."""
    TABLE = "table"
    JSON = "json"


async def get_users():
    """Get all users from the API."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/users/")
        return response.json()


async def get_user(user_id: int):
    """Get a user by ID from the API."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/users/{user_id}")
        if response.status_code == 404:
            return None
        return response.json()


async def create_user(user_input: UserInput):
    """Create a new user using the API."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{API_BASE_URL}/users/",
            json=user_input.dict(),
        )
        return response.json()


async def get_tasks(completed: Optional[bool] = None):
    """Get all tasks from the API, optionally filtered by completion status."""
    params = {}
    if completed is not None:
        params["completed"] = str(completed).lower()

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/tasks/", params=params)
        return response.json()


async def get_task(task_id: int):
    """Get a task by ID from the API."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/tasks/{task_id}")
        if response.status_code == 404:
            return None
        return response.json()


async def create_task(task_input: TaskInput):
    """Create a new task using the API."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{API_BASE_URL}/tasks/",
            json=task_input.dict(),
        )
        return response.json()


async def update_task(task_id: int, task_input: TaskInput):
    """Update a task using the API."""
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{API_BASE_URL}/tasks/{task_id}",
            json=task_input.dict(),
        )
        if response.status_code == 404:
            return None
        return response.json()


def print_user_table(users: List[dict]):
    """Print user data as a formatted table."""
    if not users:
        rprint("[yellow]No users found.[/yellow]")
        return

    table = Table(title="Users")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Username", style="green")
    table.add_column("Email", style="blue")
    table.add_column("Role", style="magenta")
    table.add_column("Full Name", style="yellow")
    table.add_column("Age", justify="right")

    for user in users:
        table.add_row(
            str(user["id"]),
            user["username"],
            user["email"],
            user["role"],
            user["full_name"] or "-",
            str(user["age"]) if user["age"] else "-",
        )

    console.print(table)


def print_task_table(tasks: List[dict]):
    """Print task data as a formatted table."""
    if not tasks:
        rprint("[yellow]No tasks found.[/yellow]")
        return

    table = Table(title="Tasks")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="green")
    table.add_column("Description", style="blue")
    table.add_column("Status", style="magenta")

    for task in tasks:
        status = "[green]Completed[/green]" if task["completed"] else "[yellow]Pending[/yellow]"
        table.add_row(
            str(task["id"]),
            task["title"],
            task["description"] or "-",
            status,
        )

    console.print(table)


@app.callback()
def main():
    """
    CLI Demo - A tool for interacting with the CLI Demo API.

    This tool demonstrates how to build intuitive command-line interfaces
    for web APIs using Typer, Rich, and Pydantic.
    """
    pass


@app.command()
def about():
    """Display information about this CLI tool."""
    md_content = """
    # CLI Demo Tool

    A command-line interface for interacting with the CLI Demo API.

    ## Features

    * Create and list users
    * Create, list, and update tasks
    * View data in table or JSON format

    ## Technologies Used

    * [FastAPI](https://fastapi.tiangolo.com/) - Web framework
    * [Typer](https://typer.tiangolo.com/) - CLI framework
    * [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
    * [Rich](https://rich.readthedocs.io/en/stable/) - Terminal formatting

    ## Getting Started

    Run `python -m app.cli --help` to see available commands.
    """
    console.print(Panel(Markdown(md_content), title="About CLI Demo"))


@app.command("user-create")
def user_create(
    username: str = typer.Option(..., prompt=True, help="Username (3-50 characters)"),
    email: str = typer.Option(..., prompt=True, help="Email address"),
    role: UserRole = typer.Option(UserRole.USER, help="User role"),
    full_name: Optional[str] = typer.Option(None, help="Full name"),
    age: Optional[int] = typer.Option(None, help="Age (1-119)"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, help="Output format"),
):
    """Create a new user."""
    try:
        # Create UserInput model
        user_input = UserInput(
            username=username,
            email=email,
            role=role,
            full_name=full_name,
            age=age,
        )

        # Call API to create user
        user = asyncio.run(create_user(user_input))

        if format == OutputFormat.JSON:
            rprint(json.dumps(user, indent=2))
        else:
            print_user_table([user])

        rprint(f"[green]User created successfully with ID: {user['id']}[/green]")

    except Exception as e:
        rprint(f"[bold red]Error creating user: {str(e)}[/bold red]")


@app.command("user-list")
def user_list(
    format: OutputFormat = typer.Option(OutputFormat.TABLE, help="Output format"),
):
    """List all users."""
    try:
        users = asyncio.run(get_users())

        if format == OutputFormat.JSON:
            rprint(json.dumps(users, indent=2))
        else:
            print_user_table(users)

        rprint(f"[green]Total users: {len(users)}[/green]")

    except Exception as e:
        rprint(f"[bold red]Error listing users: {str(e)}[/bold red]")


@app.command("user-show")
def user_show(
    user_id: int = typer.Argument(..., help="User ID"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, help="Output format"),
):
    """Show details for a specific user."""
    try:
        user = asyncio.run(get_user(user_id))

        if user is None:
            rprint(f"[bold red]User with ID {user_id} not found[/bold red]")
            raise typer.Exit(1)

        if format == OutputFormat.JSON:
            rprint(json.dumps(user, indent=2))
        else:
            print_user_table([user])

    except Exception as e:
        rprint(f"[bold red]Error showing user: {str(e)}[/bold red]")


@app.command("task-create")
def task_create(
    title: str = typer.Option(..., prompt=True, help="Task title (1-100 characters)"),
    description: Optional[str] = typer.Option(None, help="Task description"),
    completed: bool = typer.Option(False, help="Task completion status"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, help="Output format"),
):
    """Create a new task."""
    try:
        # Create TaskInput model
        task_input = TaskInput(
            title=title,
            description=description,
            completed=completed,
        )

        # Call API to create task
        task = asyncio.run(create_task(task_input))

        if format == OutputFormat.JSON:
            rprint(json.dumps(task, indent=2))
        else:
            print_task_table([task])

        rprint(f"[green]Task created successfully with ID: {task['id']}[/green]")

    except Exception as e:
        rprint(f"[bold red]Error creating task: {str(e)}[/bold red]")


@app.command("task-list")
def task_list(
    completed: Optional[bool] = typer.Option(
        None, help="Filter by completion status"
    ),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, help="Output format"),
):
    """List all tasks, optionally filtered by completion status."""
    try:
        tasks = asyncio.run(get_tasks(completed))

        if format == OutputFormat.JSON:
            rprint(json.dumps(tasks, indent=2))
        else:
            print_task_table(tasks)

        status_str = ""
        if completed is not None:
            status_str = f" ({['pending', 'completed'][completed]})"

        rprint(f"[green]Total tasks{status_str}: {len(tasks)}[/green]")

    except Exception as e:
        rprint(f"[bold red]Error listing tasks: {str(e)}[/bold red]")


@app.command("task-show")
def task_show(
    task_id: int = typer.Argument(..., help="Task ID"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, help="Output format"),
):
    """Show details for a specific task."""
    try:
        task = asyncio.run(get_task(task_id))

        if task is None:
            rprint(f"[bold red]Task with ID {task_id} not found[/bold red]")
            raise typer.Exit(1)

        if format == OutputFormat.JSON:
            rprint(json.dumps(task, indent=2))
        else:
            print_task_table([task])

    except Exception as e:
        rprint(f"[bold red]Error showing task: {str(e)}[/bold red]")


@app.command("task-update")
def task_update(
    task_id: int = typer.Argument(..., help="Task ID"),
    title: Optional[str] = typer.Option(None, help="Task title (1-100 characters)"),
    description: Optional[str] = typer.Option(None, help="Task description"),
    completed: Optional[bool] = typer.Option(None, help="Task completion status"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, help="Output format"),
):
    """Update an existing task."""
    try:
        # First get the current task data
        current_task = asyncio.run(get_task(task_id))

        if current_task is None:
            rprint(f"[bold red]Task with ID {task_id} not found[/bold red]")
            raise typer.Exit(1)

        # Update fields if provided
        updated_task_input = TaskInput(
            title=title if title is not None else current_task["title"],
            description=description if description is not None else current_task["description"],
            completed=completed if completed is not None else current_task["completed"],
        )

        # Call API to update task
        task = asyncio.run(update_task(task_id, updated_task_input))

        if format == OutputFormat.JSON:
            rprint(json.dumps(task, indent=2))
        else:
            print_task_table([task])

        rprint(f"[green]Task updated successfully[/green]")

    except Exception as e:
        rprint(f"[bold red]Error updating task: {str(e)}[/bold red]")


@app.command("task-complete")
def task_complete(
    task_id: int = typer.Argument(..., help="Task ID"),
):
    """Mark a task as completed."""
    try:
        # First get the current task data
        current_task = asyncio.run(get_task(task_id))

        if current_task is None:
            rprint(f"[bold red]Task with ID {task_id} not found[/bold red]")
            raise typer.Exit(1)

        if current_task["completed"]:
            rprint(f"[yellow]Task {task_id} is already completed[/yellow]")
            return

        # Update just the completed status
        updated_task_input = TaskInput(
            title=current_task["title"],
            description=current_task["description"],
            completed=True,
        )

        # Call API to update task
        task = asyncio.run(update_task(task_id, updated_task_input))

        print_task_table([task])
        rprint(f"[green]Task {task_id} marked as completed[/green]")

    except Exception as e:
        rprint(f"[bold red]Error completing task: {str(e)}[/bold red]")


if __name__ == "__main__":
    app()