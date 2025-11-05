# Python Data Structures Learning Application

A simple interactive application to learn Python data structure essentials. This application provides a comprehensive exploration of Python's core data structures with examples, explanations, and interactive demos.

## Features

- **Interactive Learning**: Menu-driven interface for exploring each data structure
- **Comprehensive Coverage**: Detailed examples of lists, dictionaries, tuples, and sets
- **Practical Examples**: Common patterns and use cases for each data structure
- **Hands-on Practice**: Interactive demonstrations let you try operations in real-time

## Data Structures Covered

### Lists
- Ordered, mutable collections
- Creation, access, modification, and operations
- Common patterns and performance tips
- Interactive demo for trying list operations

### Dictionaries
- Key-value mappings
- Creation, access, modification, and operations
- Advanced features like defaultdict and Counter
- Common use cases and patterns

### Tuples
- Immutable sequences
- Creation, operations, and limitations
- Named tuples and applications
- Common use cases in Python programming

### Sets
- Unordered collections of unique elements
- Set operations (union, intersection, difference)
- Modifying sets and frozen sets
- Practical applications and examples

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Navigate to the project directory:
```bash
cd python_data_structures
```

3. No external dependencies are required. The application uses only standard Python libraries.

### Running the Application

#### Interactive Menu Interface
```bash
python main.py
```

#### Command Line Interface
```bash
# Show help and available commands
python cli.py --help

# Learn about a specific data structure
python cli.py lists
python cli.py dictionaries
python cli.py tuples
python cli.py sets

# Access specific aspects of a data structure
python cli.py lists about     # Basic concepts
python cli.py lists ops       # Operations and methods
python cli.py lists patterns  # Common patterns and use cases
python cli.py lists demo      # Interactive demo

# Show application information
python cli.py --about
```

## Usage

### Interactive Menu Interface

The application presents a menu-driven interface:

1. Choose a data structure to explore (Lists, Dictionaries, Tuples, Sets)
2. Within each data structure section, you can:
   - Learn about basic concepts and characteristics
   - Explore operations and methods
   - See common patterns and use cases
   - Try operations with an interactive demo

Use keyboard input to navigate menus and follow on-screen instructions.

### Command Line Interface

The CLI allows direct access to specific content:

1. Specify the data structure you want to learn about
2. Optionally specify an action (about, ops, patterns, demo)
3. Get immediate access to the requested information or demo

## Contributing

Contributions are welcome! Feel free to submit pull requests for:
- Additional examples
- Enhanced explanations
- New data structure implementations
- UI improvements

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Python Software Foundation for the excellent documentation
- Contributors to the Python standard library