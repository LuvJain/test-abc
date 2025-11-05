# Python Data Structures Learning Application

A simple application to learn about Python's core data structures.

## Overview

This application provides both interactive and command-line interfaces to help you learn about Python's core data structures:

- Lists
- Dictionaries
- Tuples
- Sets

## Interactive Mode

To run the application in interactive mode:

```
python python_data_structures/main.py
```

This will launch a menu-driven interface where you can explore different data structures.

## Command-Line Interface

The application also provides a command-line interface for accessing the data structure information directly:

```
./pyds <command> [options]
```

Make sure to give execute permissions to the script first:

```
chmod +x pyds
```

### Available Commands

- `list`: Learn about Python lists
- `dict`: Learn about Python dictionaries
- `tuple`: Learn about Python tuples
- `set`: Learn about Python sets
- `info`: Show information about the application

### Command Examples

Get information about lists:
```
./pyds list --info
```

Show list operations:
```
./pyds list --operations
```

Run an interactive list demo:
```
./pyds list --interactive
```

Show specific list examples:
```
./pyds list --example create
./pyds list --example access
./pyds list --example modify
./pyds list --example iterate
```

For more information about a specific command:
```
./pyds <command> --help
```

## Learning Path

1. Start by exploring basic information about each data structure
2. Learn about the operations and methods available
3. Study common patterns and use cases
4. Try out the interactive demos to practice

Happy learning!
