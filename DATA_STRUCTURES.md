# Python Data Structures Guide

This guide provides an overview of the key data structures in Python and how they can be used effectively in your CLI applications. Understanding these data structures is essential for writing efficient, clean, and maintainable code.

## Table of Contents

1. [Basic Data Structures](#basic-data-structures)
   - [Lists](#lists)
   - [Tuples](#tuples)
   - [Dictionaries](#dictionaries)
   - [Sets](#sets)
2. [Advanced Data Structures](#advanced-data-structures)
   - [Collections Module](#collections-module)
   - [Arrays](#arrays)
   - [Custom Data Classes](#custom-data-classes)
3. [Data Structures in CLI Applications](#data-structures-in-cli-applications)
   - [Command-Line Arguments](#command-line-arguments)
   - [Configuration Management](#configuration-management)
   - [Data Serialization](#data-serialization)
4. [Practical Examples](#practical-examples)
   - [User Management](#user-management)
   - [Task Management](#task-management)
   - [Data Processing](#data-processing)
5. [Best Practices](#best-practices)
   - [Choosing the Right Data Structure](#choosing-the-right-data-structure)
   - [Performance Considerations](#performance-considerations)
   - [Type Hints](#type-hints)

## Basic Data Structures

### Lists

Lists are ordered, mutable collections that can contain elements of different types. They are one of the most versatile data structures in Python.

#### Key Features
- **Ordered**: Elements maintain their insertion order
- **Mutable**: Elements can be added, removed, or changed after creation
- **Indexable**: Elements can be accessed by their position (0-based indexing)
- **Nestable**: Lists can contain other lists (creating multi-dimensional structures)

#### Common Operations

```python
# Creating a list
users = ["john", "alice", "bob"]
mixed_list = [1, "hello", True, 3.14]

# Accessing elements
first_user = users[0]  # "john"
last_user = users[-1]  # "bob"

# Slicing
first_two = users[0:2]  # ["john", "alice"]

# Adding elements
users.append("charlie")  # ["john", "alice", "bob", "charlie"]
users.insert(1, "dave")  # ["john", "dave", "alice", "bob", "charlie"]
users.extend(["eve", "frank"])  # ["john", "dave", "alice", "bob", "charlie", "eve", "frank"]

# Removing elements
users.remove("alice")  # Removes the first occurrence of "alice"
popped_user = users.pop()  # Removes and returns the last element
popped_index = users.pop(1)  # Removes and returns the element at index 1
users.clear()  # Removes all elements

# Other operations
user_count = len(users)  # Number of elements
is_present = "john" in users  # Membership test
users.sort()  # In-place sorting
users.reverse()  # In-place reversal
sorted_users = sorted(users)  # Returns a new sorted list
```

#### When to Use Lists
- When order matters
- When you need a dynamic collection that changes size
- When you need to store duplicate elements
- When you need random access to elements by position

#### Example in CLI Context

```python
def process_users(usernames: List[str], options: List[str]) -> None:
    """
    Process a list of usernames with the given options.

    Args:
        usernames: A list of usernames to process
        options: A list of processing options
    """
    for username in usernames:
        for option in options:
            print(f"Processing {username} with option {option}")
```

### Tuples

Tuples are ordered, immutable collections that can contain elements of different types. They're similar to lists but cannot be modified after creation.

#### Key Features
- **Ordered**: Elements maintain their insertion order
- **Immutable**: Elements cannot be added, removed, or changed after creation
- **Indexable**: Elements can be accessed by their position (0-based indexing)
- **Hashable**: If all elements are hashable, tuples can be used as dictionary keys or set elements

#### Common Operations

```python
# Creating a tuple
user = ("john", "doe", 30)
empty_tuple = ()
single_item_tuple = ("john",)  # Note the comma

# Accessing elements
first_name = user[0]  # "john"
last_name = user[1]  # "doe"

# Unpacking
first, last, age = user

# Slicing
name_parts = user[0:2]  # ("john", "doe")

# Combining tuples
full_user = user + ("admin", "active")  # ("john", "doe", 30, "admin", "active")

# Other operations
item_count = len(user)  # Number of elements
is_present = "john" in user  # Membership test
occurrences = user.count("john")  # Count occurrences
find_index = user.index("doe")  # Find index of first occurrence
```

#### When to Use Tuples
- When you need an immutable sequence (data shouldn't change)
- For heterogeneous data (different types of data in a fixed structure)
- As dictionary keys (when needed)
- For function returns where you want to return multiple values
- For data that is meant to be unpacked

#### Example in CLI Context

```python
def get_user_details(user_id: int) -> Tuple[str, str, int]:
    """
    Get user details for the given user ID.

    Args:
        user_id: The ID of the user

    Returns:
        A tuple containing (username, email, age)
    """
    # In a real application, this would fetch data from a database or API
    return ("john_doe", "john@example.com", 30)

# Using the function
username, email, age = get_user_details(1)
print(f"User: {username}, Email: {email}, Age: {age}")
```

### Dictionaries

Dictionaries are mutable, unordered collections of key-value pairs. They provide an efficient way to store and retrieve data using unique keys.

#### Key Features
- **Key-Value Pairs**: Each element is a key-value pair
- **Unique Keys**: Each key can only appear once in a dictionary
- **Mutable**: Elements can be added, removed, or changed after creation
- **Unordered**: (Prior to Python 3.7) Elements don't have a specific order
- **Fast Lookups**: O(1) average case for retrieving values by key

#### Common Operations

```python
# Creating a dictionary
user = {"username": "john_doe", "email": "john@example.com", "age": 30}
empty_dict = {}
via_constructor = dict(username="john_doe", email="john@example.com")

# Accessing elements
username = user["username"]  # "john_doe"
# Using get() with a default value (avoids KeyError)
role = user.get("role", "user")  # Returns "user" if "role" key doesn't exist

# Adding or updating elements
user["role"] = "admin"  # Adds a new key-value pair
user["age"] = 31  # Updates an existing value

# Removing elements
removed_value = user.pop("age")  # Removes and returns the value
last_item = user.popitem()  # Removes and returns the last inserted key-value pair
user.clear()  # Removes all elements

# Dictionary methods
keys_list = list(user.keys())  # Get a list of all keys
values_list = list(user.values())  # Get a list of all values
items_list = list(user.items())  # Get a list of all key-value pairs as tuples

# Dictionary comprehension
squared = {x: x**2 for x in range(6)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # {"a": 1, "b": 3, "c": 4}

# Other operations
item_count = len(user)  # Number of key-value pairs
is_key_present = "username" in user  # Check if key exists
```

#### When to Use Dictionaries
- When you need fast lookups by key
- For data that naturally has key-value relationships
- When you need to store unique keys with associated values
- For configuration settings
- For caching results

#### Example in CLI Context

```python
def format_user_output(user: dict, format_type: str) -> str:
    """
    Format user data according to the specified format type.

    Args:
        user: A dictionary containing user data
        format_type: The output format (e.g., "simple", "detailed", "json")

    Returns:
        Formatted string representation of the user data
    """
    if format_type == "simple":
        return f"{user['username']} ({user['email']})"
    elif format_type == "detailed":
        details = [f"{key}: {value}" for key, value in user.items()]
        return "\n".join(details)
    elif format_type == "json":
        return json.dumps(user, indent=2)
    else:
        return str(user)

# Example usage
user_data = {
    "username": "john_doe",
    "email": "john@example.com",
    "role": "admin",
    "age": 30
}

print(format_user_output(user_data, "detailed"))
```

### Sets

Sets are unordered collections of unique elements. They're useful for membership testing, removing duplicates, and mathematical set operations.

#### Key Features
- **Unique Elements**: No duplicates allowed
- **Unordered**: Elements don't have a specific order
- **Mutable**: Elements can be added or removed after creation
- **Hashable Elements**: Elements must be hashable (immutable)
- **Fast Membership Testing**: O(1) average case for membership tests

#### Common Operations

```python
# Creating a set
users = {"john", "alice", "bob"}
empty_set = set()  # Note: {} creates an empty dict, not a set
from_iterable = set(["john", "alice", "bob", "john"])  # Removes duplicates

# Adding elements
users.add("charlie")  # Adds a single element
users.update({"dave", "eve"})  # Adds multiple elements

# Removing elements
users.remove("alice")  # Raises KeyError if element doesn't exist
users.discard("alice")  # Doesn't raise error if element doesn't exist
popped_item = users.pop()  # Removes and returns an arbitrary element
users.clear()  # Removes all elements

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
union = a | b  # {1, 2, 3, 4, 5, 6}
intersection = a & b  # {3, 4}
difference = a - b  # {1, 2}
symmetric_diff = a ^ b  # {1, 2, 5, 6}

# Other operations
item_count = len(users)  # Number of elements
is_member = "john" in users  # Membership test
is_subset = a <= b  # Test if a is a subset of b
is_superset = a >= b  # Test if a is a superset of b
is_disjoint = a.isdisjoint(b)  # Test if a and b have no elements in common
```

#### When to Use Sets
- When you need to ensure uniqueness
- For membership testing
- When you need to perform mathematical set operations
- For eliminating duplicates from a collection
- When the order of elements doesn't matter

#### Example in CLI Context

```python
def validate_and_filter_tags(input_tags: List[str], allowed_tags: Set[str]) -> Set[str]:
    """
    Validate and filter tags against a set of allowed tags.

    Args:
        input_tags: List of tags provided by the user
        allowed_tags: Set of allowed tag values

    Returns:
        Set of valid, unique tags
    """
    # Convert input to a set to remove duplicates
    unique_tags = set(input_tags)

    # Filter to only include allowed tags
    valid_tags = unique_tags & allowed_tags

    # Inform about invalid tags
    invalid_tags = unique_tags - allowed_tags
    if invalid_tags:
        print(f"Warning: Ignoring invalid tags: {', '.join(invalid_tags)}")

    return valid_tags

# Example usage
ALLOWED_TAGS = {"python", "cli", "api", "web", "database", "testing"}
user_input = ["python", "cli", "invalid-tag", "python", "unknown"]

valid_tags = validate_and_filter_tags(user_input, ALLOWED_TAGS)
print(f"Valid tags: {', '.join(valid_tags)}")
```

## Advanced Data Structures

### Collections Module

The `collections` module provides specialized data structures that extend the capabilities of Python's built-in types. These data structures are optimized for specific use cases and can make your code more efficient and readable.

#### namedtuple

Named tuples are immutable sequence types similar to regular tuples, but each element can be accessed by name (as well as by index). They're useful for creating simple, immutable data objects.

```python
from collections import namedtuple

# Define a named tuple class
User = namedtuple('User', ['username', 'email', 'role'])

# Create an instance
user = User('john_doe', 'john@example.com', 'admin')

# Access by name
print(user.username)  # 'john_doe'
print(user.email)     # 'john@example.com'

# Access by index
print(user[0])        # 'john_doe'

# Unpacking
username, email, role = user
```

Named tuples are particularly useful in CLI applications for returning structured data from functions, creating configuration objects, or defining command results.

#### defaultdict

A `defaultdict` is a subclass of `dict` that calls a factory function to provide default values for missing keys. This eliminates the need for key existence checks.

```python
from collections import defaultdict

# Create a defaultdict with list as the default factory
command_groups = defaultdict(list)

# Add commands to groups without checking if the key exists
command_groups['user'].append('user-create')
command_groups['user'].append('user-list')
command_groups['task'].append('task-create')

# Access a key that doesn't exist yet
print(command_groups['report'])  # Returns an empty list instead of KeyError
```

In CLI applications, `defaultdict` is useful for grouping related items, counting occurrences, or building hierarchical structures.

#### OrderedDict

An `OrderedDict` is a dictionary subclass that remembers the insertion order of keys. While regular dictionaries in Python 3.7+ preserve insertion order, `OrderedDict` provides additional methods like `move_to_end()` and has a different equality comparison behavior.

```python
from collections import OrderedDict

# Create an ordered dictionary
cli_commands = OrderedDict()
cli_commands['help'] = 'Display help information'
cli_commands['version'] = 'Display version information'
cli_commands['config'] = 'Configure settings'

# Iterate in insertion order
for command, description in cli_commands.items():
    print(f"{command}: {description}")
```

In CLI applications, `OrderedDict` is useful for configuration settings, command registries, or any scenario where order matters.

#### Counter

A `Counter` is a dictionary subclass for counting hashable objects. It's a convenient way to count occurrences of elements in a collection.

```python
from collections import Counter

# Count command usages
command_usage = Counter()
command_usage.update(['user-list', 'task-create', 'user-list', 'help'])

# Get most common commands
print(command_usage.most_common(2))  # [('user-list', 2), ('task-create', 1)]

# Count elements in a list
words = ['cli', 'python', 'api', 'cli', 'task', 'user', 'cli']
word_counts = Counter(words)
print(word_counts['cli'])  # 3
```

In CLI applications, `Counter` is useful for analytics, generating reports, or identifying patterns in user behavior.

#### deque

A `deque` (double-ended queue) is a list-like container with efficient appends and pops from either end. It's useful for implementing queues, stacks, or maintaining a fixed-size history.

```python
from collections import deque

# Create a deque with a maximum length
command_history = deque(maxlen=5)

# Add commands to the history
command_history.append('user-list')
command_history.append('task-create')
command_history.append('help')

# When maxlen is reached, oldest items are discarded
print(list(command_history))  # ['user-list', 'task-create', 'help']

# Efficient operations at both ends
command_history.appendleft('version')  # Add to the left
last_command = command_history.pop()   # Remove from the right
```

In CLI applications, `deque` is useful for command history, breadth-first search algorithms, or processing streams of data.

### Arrays

The `array` module provides space-efficient arrays of numeric values. Unlike lists, arrays are homogeneous and store only values of a single type.

```python
import array

# Create an array of integers
# 'i' represents signed int
scores = array.array('i', [75, 92, 87, 65, 98])

# Modify the array
scores.append(80)
scores[0] = 77

# Array operations
avg_score = sum(scores) / len(scores)
max_score = max(scores)
```

In CLI applications, arrays are useful when working with large collections of numeric data, such as processing sensor readings, performance metrics, or binary data.

### Custom Data Classes

Python 3.7+ introduced the `dataclasses` module which provides a decorator and functions for automatically adding special methods to user-defined classes.

```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class CliCommand:
    name: str
    description: str
    aliases: List[str] = field(default_factory=list)
    is_public: bool = True
    help_text: Optional[str] = None

    def get_usage(self) -> str:
        return f"{self.name}: {self.description}"

# Create a command
user_list_cmd = CliCommand(
    name="user-list",
    description="List all users",
    aliases=["ls-users", "users"],
)

print(user_list_cmd)  # CliCommand(name='user-list', description='List all users', aliases=['ls-users', 'users'], is_public=True, help_text=None)
print(user_list_cmd.get_usage())  # user-list: List all users
```

Data classes provide a concise way to define classes that mainly store data. They automatically generate special methods like `__init__`, `__repr__`, and `__eq__`, making your code cleaner and less error-prone.

In CLI applications, data classes are useful for representing commands, configuration settings, user inputs, and application state.

#### Frozen Data Classes

You can also create immutable (frozen) data classes:

```python
@dataclass(frozen=True)
class CliOption:
    name: str
    short_name: Optional[str]
    help_text: str
    required: bool = False
```

Frozen data classes are particularly useful for configuration parameters, command-line options, or any data that should not change after creation.

## Data Structures in CLI Applications

### Command-Line Arguments

Command-line arguments are a critical component of any CLI application. In this section, we'll explore how different data structures can be used to organize and process command-line arguments.

#### Using Lists for Positional Arguments

```python
import typer
from typing import List

app = typer.Typer()

@app.command()
def process_files(
    files: List[str] = typer.Argument(
        ...,
        help="List of files to process"
    )
):
    """Process multiple files provided as positional arguments."""
    for file in files:
        typer.echo(f"Processing file: {file}")

# Usage: python cli.py process-files file1.txt file2.txt file3.txt
```

#### Using Dictionaries for Parameter Configurations

```python
def create_command_config():
    """Create a configuration dictionary for commands."""
    return {
        "user-list": {
            "help": "List all users",
            "options": {
                "format": {
                    "type": str,
                    "default": "table",
                    "help": "Output format (table or json)"
                },
                "sort_by": {
                    "type": str,
                    "default": "id",
                    "help": "Field to sort by"
                }
            }
        },
        "task-list": {
            "help": "List all tasks",
            "options": {
                "completed": {
                    "type": bool,
                    "default": None,
                    "help": "Filter by completion status"
                },
                "format": {
                    "type": str,
                    "default": "table",
                    "help": "Output format (table or json)"
                }
            }
        }
    }

# Usage with a command factory
def register_commands(app, config):
    for cmd_name, cmd_config in config.items():
        options = cmd_config.get("options", {})
        # Create and register command with options...
```

### Configuration Management

Proper configuration management is essential for flexible and maintainable CLI applications. Here's how different data structures can be used for this purpose.

#### Nested Dictionaries for Hierarchical Configuration

```python
def load_config(config_file="config.json"):
    """Load configuration from a JSON file."""
    with open(config_file, "r") as f:
        return json.load(f)

# Example config structure
config = {
    "api": {
        "base_url": "http://localhost:8000",
        "timeout": 30,
        "retry": {
            "max_attempts": 3,
            "backoff_factor": 0.5
        }
    },
    "output": {
        "default_format": "table",
        "colors": {
            "success": "green",
            "error": "red",
            "warning": "yellow"
        },
        "verbosity": 1
    },
    "cache": {
        "enabled": True,
        "max_size": 100,
        "ttl": 300  # seconds
    }
}

# Access nested configuration
api_url = config["api"]["base_url"]
max_retry = config["api"]["retry"]["max_attempts"]
```

#### Using Data Classes for Strongly Typed Configuration

```python
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class RetryConfig:
    max_attempts: int = 3
    backoff_factor: float = 0.5

@dataclass
class ApiConfig:
    base_url: str
    timeout: int = 30
    retry: RetryConfig = RetryConfig()

@dataclass
class OutputConfig:
    default_format: str = "table"
    colors: Dict[str, str] = None
    verbosity: int = 1

@dataclass
class AppConfig:
    api: ApiConfig
    output: OutputConfig
    cache_enabled: bool = True
    cache_max_size: Optional[int] = 100

    @classmethod
    def from_dict(cls, config_dict):
        """Create a config object from a dictionary."""
        api_config = ApiConfig(
            base_url=config_dict["api"]["base_url"],
            timeout=config_dict["api"].get("timeout", 30),
            retry=RetryConfig(
                max_attempts=config_dict["api"]["retry"].get("max_attempts", 3),
                backoff_factor=config_dict["api"]["retry"].get("backoff_factor", 0.5)
            )
        )
        output_config = OutputConfig(
            default_format=config_dict["output"].get("default_format", "table"),
            colors=config_dict["output"].get("colors", {}),
            verbosity=config_dict["output"].get("verbosity", 1)
        )
        return cls(
            api=api_config,
            output=output_config,
            cache_enabled=config_dict.get("cache", {}).get("enabled", True),
            cache_max_size=config_dict.get("cache", {}).get("max_size", 100)
        )

# Usage
config_dict = load_config()
app_config = AppConfig.from_dict(config_dict)
print(f"API URL: {app_config.api.base_url}")
print(f"Max retry attempts: {app_config.api.retry.max_attempts}")
```

### Data Serialization

CLI applications often need to serialize data for output, storage, or API communication. Here's how to use different data structures for serialization.

#### Lists and Dictionaries for JSON Serialization

```python
import json

def format_output(data, format_type="table"):
    """Format data for output in different formats."""
    if format_type == "json":
        return json.dumps(data, indent=2)
    elif format_type == "table":
        # Convert to table representation
        return create_table(data)
    else:
        return str(data)

# Example with user data
users = [
    {"id": 1, "username": "john_doe", "email": "john@example.com", "role": "admin"},
    {"id": 2, "username": "jane_doe", "email": "jane@example.com", "role": "user"}
]

# Output as JSON
json_output = format_output(users, "json")
print(json_output)
```

## Practical Examples

Let's explore some practical examples of how data structures can be used in real-world CLI applications.

### User Management

Here's an example of extending the existing CLI application to add user management features with better data structure usage:

```python
import typer
from typing import List, Dict, Optional
from enum import Enum
import json
from dataclasses import dataclass, field
from rich.console import Console
from rich.table import Table

# Create console for rich output
console = Console()

# Data classes for structured data
@dataclass
class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

@dataclass
class User:
    username: str
    email: str
    role: UserRole = UserRole.USER
    full_name: Optional[str] = None
    age: Optional[int] = None
    id: Optional[int] = None

    def to_dict(self) -> Dict:
        """Convert user to dictionary for serialization."""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role.value,
            "full_name": self.full_name,
            "age": self.age
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Create a user object from dictionary data."""
        return cls(
            username=data["username"],
            email=data["email"],
            role=UserRole(data["role"]),
            full_name=data.get("full_name"),
            age=data.get("age"),
            id=data.get("id")
        )

# User repository using dictionary for in-memory storage
class UserRepository:
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.next_id: int = 1

    def create(self, user: User) -> User:
        """Create a new user."""
        user.id = self.next_id
        self.users[user.id] = user
        self.next_id += 1
        return user

    def get_all(self) -> List[User]:
        """Get all users."""
        return list(self.users.values())

    def get_by_id(self, user_id: int) -> Optional[User]:
        """Get a user by ID."""
        return self.users.get(user_id)

    def update(self, user_id: int, user: User) -> Optional[User]:
        """Update a user."""
        if user_id in self.users:
            user.id = user_id
            self.users[user_id] = user
            return user
        return None

    def delete(self, user_id: int) -> bool:
        """Delete a user."""
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

# Create typer app
app = typer.Typer()
user_repo = UserRepository()

# Output formatting with enums
class OutputFormat(str, Enum):
    TABLE = "table"
    JSON = "json"

@app.command("user-create")
def user_create(
    username: str = typer.Option(..., prompt=True, help="Username"),
    email: str = typer.Option(..., prompt=True, help="Email address"),
    role: UserRole = typer.Option(UserRole.USER, help="User role"),
    full_name: Optional[str] = typer.Option(None, help="Full name"),
    age: Optional[int] = typer.Option(None, help="Age"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, help="Output format"),
):
    """Create a new user with structured data."""
    # Create user object
    user = User(
        username=username,
        email=email,
        role=role,
        full_name=full_name,
        age=age
    )

    # Save user
    created_user = user_repo.create(user)

    # Format output
    if format == OutputFormat.JSON:
        typer.echo(json.dumps(created_user.to_dict(), indent=2))
    else:
        # Create a table
        table = Table(title="User Created")
        table.add_column("ID", style="cyan")
        table.add_column("Username", style="green")
        table.add_column("Email", style="blue")
        table.add_column("Role", style="magenta")
        table.add_column("Full Name", style="yellow")
        table.add_column("Age")

        user_dict = created_user.to_dict()
        table.add_row(
            str(user_dict["id"]),
            user_dict["username"],
            user_dict["email"],
            user_dict["role"],
            user_dict["full_name"] or "-",
            str(user_dict["age"]) if user_dict["age"] else "-"
        )

        console.print(table)

@app.command("user-list")
def user_list(
    format: OutputFormat = typer.Option(OutputFormat.TABLE, help="Output format"),
):
    """List all users with rich formatting."""
    users = user_repo.get_all()

    if format == OutputFormat.JSON:
        user_dicts = [user.to_dict() for user in users]
        typer.echo(json.dumps(user_dicts, indent=2))
    else:
        # Create a table
        table = Table(title="Users")
        table.add_column("ID", style="cyan")
        table.add_column("Username", style="green")
        table.add_column("Email", style="blue")
        table.add_column("Role", style="magenta")
        table.add_column("Full Name", style="yellow")
        table.add_column("Age")

        for user in users:
            user_dict = user.to_dict()
            table.add_row(
                str(user_dict["id"]),
                user_dict["username"],
                user_dict["email"],
                user_dict["role"],
                user_dict["full_name"] or "-",
                str(user_dict["age"]) if user_dict["age"] else "-"
            )

        console.print(table)

if __name__ == "__main__":
    # Pre-populate with sample data
    user_repo.create(User(username="john_doe", email="john@example.com", role=UserRole.ADMIN, full_name="John Doe", age=30))
    user_repo.create(User(username="jane_doe", email="jane@example.com", role=UserRole.USER, full_name="Jane Doe", age=28))

    app()
```

### Task Management

Here's an example of implementing task management functionality using various data structures:

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set
from datetime import datetime, date
from enum import Enum
import typer
from rich.console import Console
from rich.table import Table
import json

console = Console()
app = typer.Typer()

# Enum for task priority
class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

# Data class for tasks
@dataclass
class Task:
    title: str
    description: Optional[str] = None
    completed: bool = False
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: Optional[date] = None
    tags: Set[str] = field(default_factory=set)
    created_at: datetime = field(default_factory=datetime.now)
    id: Optional[int] = None

    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "priority": self.priority.value,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "tags": list(self.tags),
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Create a task object from dictionary data."""
        tags_set = set(data.get("tags", []))
        due_date = None
        if data.get("due_date"):
            due_date = datetime.fromisoformat(data["due_date"]).date()

        return cls(
            title=data["title"],
            description=data.get("description"),
            completed=data.get("completed", False),
            priority=TaskPriority(data.get("priority", "medium")),
            due_date=due_date,
            tags=tags_set,
            created_at=datetime.fromisoformat(data.get("created_at", datetime.now().isoformat())),
            id=data.get("id")
        )

# Task repository
class TaskRepository:
    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self.next_id: int = 1

    def create(self, task: Task) -> Task:
        """Create a new task."""
        task.id = self.next_id
        self.tasks[task.id] = task
        self.next_id += 1
        return task

    def get_all(self, completed: Optional[bool] = None) -> List[Task]:
        """Get all tasks, optionally filtered by completion status."""
        if completed is None:
            return list(self.tasks.values())
        return [task for task in self.tasks.values() if task.completed == completed]

    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by ID."""
        return self.tasks.get(task_id)

    def update(self, task_id: int, task: Task) -> Optional[Task]:
        """Update a task."""
        if task_id in self.tasks:
            task.id = task_id
            self.tasks[task_id] = task
            return task
        return None

    def delete(self, task_id: int) -> bool:
        """Delete a task."""
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def get_by_tags(self, tags: Set[str]) -> List[Task]:
        """Get tasks that have all the specified tags."""
        return [task for task in self.tasks.values() if tags.issubset(task.tags)]

    def get_by_priority(self, priority: TaskPriority) -> List[Task]:
        """Get tasks with the specified priority."""
        return [task for task in self.tasks.values() if task.priority == priority]

# Output formatting
class OutputFormat(str, Enum):
    TABLE = "table"
    JSON = "json"

# Create task repository
task_repo = TaskRepository()

@app.command("task-create")
def task_create(
    title: str = typer.Option(..., prompt=True, help="Task title"),
    description: Optional[str] = typer.Option(None, help="Task description"),
    priority: TaskPriority = typer.Option(TaskPriority.MEDIUM, help="Task priority"),
    due_date: Optional[str] = typer.Option(None, help="Due date (YYYY-MM-DD)"),
    tags: Optional[str] = typer.Option(None, help="Comma-separated tags"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, help="Output format"),
):
    """Create a new task with rich metadata."""
    # Parse due date
    parsed_due_date = None
    if due_date:
        try:
            parsed_due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            typer.echo("Invalid date format. Please use YYYY-MM-DD.")
            raise typer.Exit(1)

    # Parse tags
    tag_set = set()
    if tags:
        tag_set = {tag.strip() for tag in tags.split(",")}

    # Create task
    task = Task(
        title=title,
        description=description,
        priority=priority,
        due_date=parsed_due_date,
        tags=tag_set
    )

    # Save task
    created_task = task_repo.create(task)

    # Format output
    if format == OutputFormat.JSON:
        typer.echo(json.dumps(created_task.to_dict(), indent=2))
    else:
        # Create a table
        table = Table(title="Task Created")
        table.add_column("ID", style="cyan")
        table.add_column("Title", style="green")
        table.add_column("Description", style="blue")
        table.add_column("Priority", style="magenta")
        table.add_column("Due Date", style="yellow")
        table.add_column("Tags", style="cyan")

        task_dict = created_task.to_dict()
        table.add_row(
            str(task_dict["id"]),
            task_dict["title"],
            task_dict["description"] or "-",
            task_dict["priority"],
            task_dict["due_date"] or "-",
            ", ".join(task_dict["tags"]) or "-"
        )

        console.print(table)

@app.command("task-list")
def task_list(
    completed: Optional[bool] = typer.Option(None, help="Filter by completion status"),
    priority: Optional[TaskPriority] = typer.Option(None, help="Filter by priority"),
    tag: Optional[str] = typer.Option(None, help="Filter by tag"),
    format: OutputFormat = typer.Option(OutputFormat.TABLE, help="Output format"),
):
    """List tasks with filtering options."""
    # Get all tasks
    tasks = task_repo.get_all(completed)

    # Filter by priority
    if priority:
        tasks = [task for task in tasks if task.priority == priority]

    # Filter by tag
    if tag:
        tasks = [task for task in tasks if tag in task.tags]

    # Format output
    if format == OutputFormat.JSON:
        task_dicts = [task.to_dict() for task in tasks]
        typer.echo(json.dumps(task_dicts, indent=2))
    else:
        # Create a table
        table = Table(title="Tasks")
        table.add_column("ID", style="cyan")
        table.add_column("Title", style="green")
        table.add_column("Priority", style="magenta")
        table.add_column("Due Date", style="yellow")
        table.add_column("Tags", style="cyan")
        table.add_column("Status", style="blue")

        for task in tasks:
            task_dict = task.to_dict()
            status = "[green]Completed[/green]" if task.completed else "[yellow]Pending[/yellow]"
            table.add_row(
                str(task_dict["id"]),
                task_dict["title"],
                task_dict["priority"],
                task_dict["due_date"] or "-",
                ", ".join(task_dict["tags"]) or "-",
                status
            )

        console.print(table)

if __name__ == "__main__":
    # Pre-populate with sample data
    task_repo.create(Task(
        title="Complete documentation",
        description="Write comprehensive docs for the CLI application",
        priority=TaskPriority.HIGH,
        tags={"documentation", "python", "cli"}
    ))
    task_repo.create(Task(
        title="Implement user authentication",
        description="Add user authentication to the API",
        priority=TaskPriority.MEDIUM,
        tags={"security", "api"}
    ))

    app()
```

### Data Processing

Here's an example of using various data structures for data processing in a CLI application:

```python
from collections import Counter, defaultdict, deque
import csv
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set, Deque
import typer
from rich.console import Console
from rich.table import Table
from datetime import datetime
import statistics
import json

app = typer.Typer()
console = Console()

# Data classes for structured data
@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    service: str
    message: str

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            timestamp=datetime.fromisoformat(data["timestamp"]),
            level=data["level"],
            service=data["service"],
            message=data["message"]
        )

@dataclass
class LogAnalytics:
    total_entries: int = 0
    entries_by_level: Dict[str, int] = field(default_factory=Counter)
    entries_by_service: Dict[str, int] = field(default_factory=Counter)
    recent_logs: Deque[LogEntry] = field(default_factory=lambda: deque(maxlen=10))
    error_services: Set[str] = field(default_factory=set)

    def add_entry(self, entry: LogEntry):
        """Add a log entry to analytics."""
        self.total_entries += 1
        self.entries_by_level[entry.level] += 1
        self.entries_by_service[entry.service] += 1
        self.recent_logs.append(entry)

        if entry.level.lower() in ("error", "critical"):
            self.error_services.add(entry.service)

@app.command("analyze-logs")
def analyze_logs(
    log_file: str = typer.Argument(..., help="Path to log file (CSV format)"),
    output_format: str = typer.Option("table", help="Output format (table or json)")
):
    """Analyze log data using efficient data structures."""
    # Load and process logs
    analytics = LogAnalytics()
    log_entries = []

    try:
        with open(log_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                entry = LogEntry.from_dict(row)
                log_entries.append(entry)
                analytics.add_entry(entry)
    except Exception as e:
        typer.echo(f"Error reading log file: {str(e)}")
        raise typer.Exit(1)

    # Additional data processing using various data structures

    # Group logs by hour using defaultdict
    logs_by_hour = defaultdict(list)
    for entry in log_entries:
        hour = entry.timestamp.replace(minute=0, second=0, microsecond=0)
        logs_by_hour[hour].append(entry)

    # Calculate hourly statistics
    hourly_stats = {}
    for hour, entries in logs_by_hour.items():
        hourly_stats[hour.isoformat()] = {
            "count": len(entries),
            "error_count": sum(1 for e in entries if e.level.lower() in ("error", "critical")),
            "services": Counter(e.service for e in entries)
        }

    # Find most common error messages using Counter
    error_entries = [e for e in log_entries if e.level.lower() in ("error", "critical")]
    error_messages = Counter(e.message for e in error_entries)
    top_errors = error_messages.most_common(5)

    # Prepare results
    results = {
        "summary": {
            "total_entries": analytics.total_entries,
            "entries_by_level": dict(analytics.entries_by_level),
            "entries_by_service": dict(analytics.entries_by_service),
            "error_services": list(analytics.error_services)
        },
        "hourly_stats": hourly_stats,
        "top_errors": [{"message": msg, "count": count} for msg, count in top_errors],
        "recent_logs": [
            {
                "timestamp": entry.timestamp.isoformat(),
                "level": entry.level,
                "service": entry.service,
                "message": entry.message
            }
            for entry in analytics.recent_logs
        ]
    }

    # Output results
    if output_format.lower() == "json":
        typer.echo(json.dumps(results, indent=2))
    else:
        # Summary table
        summary_table = Table(title="Log Analysis Summary")
        summary_table.add_column("Metric", style="cyan")
        summary_table.add_column("Value", style="green")

        summary_table.add_row("Total Entries", str(analytics.total_entries))
        summary_table.add_row("Error Services", ", ".join(analytics.error_services) or "None")

        # Level breakdown table
        level_table = Table(title="Entries by Log Level")
        level_table.add_column("Level", style="magenta")
        level_table.add_column("Count", style="green")
        level_table.add_column("Percentage", style="blue")

        for level, count in sorted(analytics.entries_by_level.items()):
            percentage = (count / analytics.total_entries) * 100 if analytics.total_entries > 0 else 0
            level_table.add_row(level, str(count), f"{percentage:.1f}%")

        # Top errors table
        errors_table = Table(title="Top Error Messages")
        errors_table.add_column("Message", style="red")
        errors_table.add_column("Count", style="green")

        for msg, count in top_errors:
            errors_table.add_row(msg, str(count))

        # Recent logs table
        recent_table = Table(title="Recent Logs")
        recent_table.add_column("Timestamp", style="cyan")
        recent_table.add_column("Level", style="magenta")
        recent_table.add_column("Service", style="green")
        recent_table.add_column("Message", style="blue")

        for entry in list(analytics.recent_logs):
            recent_table.add_row(
                entry.timestamp.isoformat(),
                entry.level,
                entry.service,
                entry.message
            )

        # Print all tables
        console.print(summary_table)
        console.print(level_table)
        console.print(errors_table)
        console.print(recent_table)

if __name__ == "__main__":
    app()
```

## Best Practices

### Choosing the Right Data Structure

Selecting the appropriate data structure for your task can significantly impact the performance, readability, and maintainability of your code. Here are some guidelines:

1. **When to Use Lists**:
   - When order matters
   - When elements need to be accessed by position
   - When you need a mutable sequence
   - When you need to store duplicate elements

2. **When to Use Tuples**:
   - When you need an immutable sequence
   - For heterogeneous data (different types in a fixed structure)
   - For returning multiple values from a function
   - For dictionary keys (when needed)

3. **When to Use Dictionaries**:
   - When you need fast lookups by key
   - For mapping relationships between values
   - For configuration settings
   - For caching results
   - For counting occurrences

4. **When to Use Sets**:
   - When uniqueness matters
   - For membership testing
   - For removing duplicates
   - For mathematical set operations

5. **When to Use Collections Module**:
   - `namedtuple`: When you need tuples with named fields
   - `defaultdict`: When you need dictionaries with default values
   - `OrderedDict`: When you need dictionaries with guaranteed ordering and special methods
   - `Counter`: When you need to count occurrences
   - `deque`: When you need a double-ended queue

6. **When to Use Data Classes**:
   - When you need classes that mainly store data
   - For structured configuration
   - For complex data models
   - For improved code readability and maintainability

### Performance Considerations

Different data structures have different performance characteristics. Here's a quick reference:

| Operation | List | Tuple | Dict | Set | Deque |
|-----------|------|-------|------|-----|-------|
| Access by index | O(1) | O(1) | - | - | O(1) |
| Access by key | - | - | O(1) | - | - |
| Search | O(n) | O(n) | O(1) | O(1) | O(n) |
| Append | O(1) | - | - | - | O(1) |
| Insert at beginning | O(n) | - | - | - | O(1) |
| Insert in middle | O(n) | - | - | - | O(n) |
| Delete at end | O(1) | - | - | - | O(1) |
| Delete at beginning | O(n) | - | - | - | O(1) |
| Delete in middle | O(n) | - | - | - | O(n) |

Remember:
- Use `list` when you need a mutable sequence
- Use `dict` when you need fast lookups by key
- Use `set` when you need unique elements and fast membership testing
- Use `deque` when you need efficient operations at both ends

### Type Hints

Type hints improve code readability and maintainability, especially when working with complex data structures. Here are some examples:

```python
from typing import List, Dict, Tuple, Set, Optional, Union

# Simple type hints
def process_usernames(usernames: List[str]) -> None:
    """Process a list of usernames."""
    for username in usernames:
        print(f"Processing {username}")

# Complex type hints
def get_user_data(user_id: int) -> Dict[str, Union[str, int, List[str]]]:
    """Get user data as a dictionary."""
    return {
        "id": user_id,
        "username": "john_doe",
        "email": "john@example.com",
        "age": 30,
        "tags": ["admin", "active"]
    }

# Type hints with generics
def group_by_role(users: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    """Group users by their role."""
    result: Dict[str, List[Dict[str, str]]] = {}
    for user in users:
        role = user.get("role", "user")
        if role not in result:
            result[role] = []
        result[role].append(user)
    return result

# Type hints with Optional
def find_user(users: List[Dict[str, str]], username: str) -> Optional[Dict[str, str]]:
    """Find a user by username or return None if not found."""
    for user in users:
        if user.get("username") == username:
            return user
    return None
```

Using type hints with data structures helps catch errors early, improves IDE autocomplete, and makes your code more self-documenting.