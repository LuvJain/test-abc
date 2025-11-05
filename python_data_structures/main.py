#!/usr/bin/env python3
"""
Python Data Structures Learning Application

A simple application to learn Python data structure essentials.

This application provides an interactive way to explore Python's
core data structures: lists, dictionaries, tuples, and sets.

Usage:
    python main.py          # Interactive menu interface
    python cli.py --help    # CLI interface with command-line options

The application will present a menu-driven interface for exploring
different data structures and their operations when run interactively.
For command-line options, use the cli.py module.
"""

import sys
import time
from data_structures import lists, dictionaries, tuples_and_sets


def clear_screen():
    """Clear the terminal screen."""
    print("\033c", end="")  # ANSI escape sequence to clear screen


def print_header(title, width=60):
    """Print a formatted header."""
    print("\n" + "=" * width)
    print(f"{title:^{width}}")
    print("=" * width + "\n")


def print_menu():
    """Print the main menu."""
    clear_screen()
    print_header("PYTHON DATA STRUCTURES LEARNING APPLICATION")
    print("Welcome to the Python Data Structures Learning Application!")
    print("This application will help you learn about Python's core data structures.\n")

    print("Please select a data structure to explore:\n")
    print("1. Lists")
    print("2. Dictionaries")
    print("3. Tuples")
    print("4. Sets")
    print("5. About this application")
    print("6. Exit")

    return input("\nEnter your choice (1-6): ")


def print_data_structure_menu(data_structure_name):
    """Print the menu for a specific data structure."""
    clear_screen()
    print_header(f"PYTHON {data_structure_name.upper()}")
    print(f"Learn about Python {data_structure_name}:\n")

    print(f"1. What are {data_structure_name}?")
    print(f"2. {data_structure_name} operations and methods")
    print(f"3. Common {data_structure_name} patterns and use cases")
    print(f"4. Interactive {data_structure_name} demo")
    print("5. Back to main menu")

    return input("\nEnter your choice (1-5): ")


def about_lists():
    """Display information about Python lists."""
    clear_screen()
    print_header("ABOUT PYTHON LISTS")

    print("Lists are one of Python's most versatile and commonly used data structures.")
    print("They are ordered, mutable collections that can store elements of different types.\n")

    print("Key characteristics of Python lists:")
    print("• Ordered: Elements maintain their order and are accessed by index")
    print("• Mutable: Can be modified after creation (add, remove, change elements)")
    print("• Dynamic: Can grow or shrink in size")
    print("• Heterogeneous: Can contain elements of different types")
    print("• Nestable: Can contain other lists as elements\n")

    print("Common list creation methods:")
    for name, example in lists.create_list_examples().items():
        print(f"• {name}: {example}")

    input("\nPress Enter to continue...")


def list_operations():
    """Display information about list operations and methods."""
    clear_screen()
    print_header("LIST OPERATIONS AND METHODS")

    print("Python lists support many powerful operations and methods:\n")

    print("Accessing elements:")
    sample_list = [10, 20, 30, 40, 50, 60, 70]
    print(f"Sample list: {sample_list}")
    for name, example in lists.list_access_examples(sample_list).items():
        print(f"• {name}: {example}")

    print("\nModifying lists:")
    for name, example in lists.list_modification_examples().items():
        print(f"• {name}: {example}")

    print("\nCommon list operations:")
    for name, example in lists.list_operations_examples().items():
        print(f"• {name}: {example}")

    print("\nPerformance tips:")
    for tip, description in lists.list_performance_tips().items():
        print(f"• {tip}: {description}")

    input("\nPress Enter to continue...")


def list_patterns():
    """Display information about common list patterns and use cases."""
    clear_screen()
    print_header("COMMON LIST PATTERNS AND USE CASES")

    print("Lists are used in many programming patterns and scenarios:\n")

    examples = lists.common_list_patterns()
    for pattern, example in examples.items():
        print(f"• {pattern}:")
        print(f"  {example}")
        print()

    input("Press Enter to continue...")


def about_dictionaries():
    """Display information about Python dictionaries."""
    clear_screen()
    print_header("ABOUT PYTHON DICTIONARIES")

    print("Dictionaries are powerful, flexible data structures in Python.")
    print("They store key-value pairs and provide efficient lookup by key.\n")

    print("Key characteristics of Python dictionaries:")
    print("• Key-Value Mapping: Each value is associated with a unique key")
    print("• Unordered (pre-Python 3.7): Keys have no defined order")
    print("• Ordered (Python 3.7+): Keys maintain insertion order")
    print("• Mutable: Can be modified after creation")
    print("• Dynamic: Can grow or shrink in size")
    print("• Keys must be immutable: Strings, numbers, tuples (of immutables)")
    print("• Values can be any type: Including lists, dicts, objects, etc.\n")

    print("Common dictionary creation methods:")
    for name, example in dictionaries.create_dict_examples().items():
        print(f"• {name}: {example}")

    input("\nPress Enter to continue...")


def dict_operations():
    """Display information about dictionary operations and methods."""
    clear_screen()
    print_header("DICTIONARY OPERATIONS AND METHODS")

    print("Python dictionaries support many powerful operations and methods:\n")

    print("Accessing dictionary elements:")
    for name, example in dictionaries.dict_access_examples().items():
        print(f"• {name}: {example}")

    print("\nModifying dictionaries:")
    for name, example in dictionaries.dict_modification_examples().items():
        print(f"• {name}: {example}")

    print("\nCommon dictionary operations:")
    for name, example in dictionaries.dict_operations_examples().items():
        print(f"• {name}: {example}")

    print("\nAdvanced dictionary features:")
    for name, example in dictionaries.dict_advanced_examples().items():
        print(f"• {name}: {example}")

    input("\nPress Enter to continue...")


def dict_patterns():
    """Display information about common dictionary patterns and use cases."""
    clear_screen()
    print_header("COMMON DICTIONARY PATTERNS AND USE CASES")

    print("Dictionaries are used in many programming patterns and scenarios:\n")

    examples = dictionaries.dict_use_cases()
    for pattern, example in examples.items():
        print(f"• {pattern}:")
        print(f"  {example}")
        print()

    input("Press Enter to continue...")


def about_tuples():
    """Display information about Python tuples."""
    clear_screen()
    print_header("ABOUT PYTHON TUPLES")

    print("Tuples are immutable sequences, similar to lists but cannot be changed after creation.")
    print("They're typically used for fixed collections of related items.\n")

    print("Key characteristics of Python tuples:")
    print("• Ordered: Elements maintain their order and are accessed by index")
    print("• Immutable: Cannot be modified after creation")
    print("• Hashable: Can be used as dictionary keys or set elements")
    print("• Heterogeneous: Can contain elements of different types")
    print("• Nestable: Can contain other tuples as elements")
    print("• Often used for: Multiple return values, function arguments, immutable records\n")

    print("Tuple examples:")
    for name, example in tuples_and_sets.tuple_examples().items():
        print(f"• {name}: {example}")

    input("\nPress Enter to continue...")


def tuple_operations():
    """Display information about tuple operations."""
    clear_screen()
    print_header("TUPLE OPERATIONS")

    print("Operations that can be performed with tuples:\n")

    for name, example in tuples_and_sets.tuple_operations().items():
        print(f"• {name}: {example}")

    input("\nPress Enter to continue...")


def tuple_patterns():
    """Display information about common tuple patterns and use cases."""
    clear_screen()
    print_header("COMMON TUPLE PATTERNS AND USE CASES")

    print("Tuples are used in many programming patterns and scenarios:\n")

    examples = tuples_and_sets.tuple_use_cases()
    for pattern, example in examples.items():
        print(f"• {pattern}:")
        print(f"  {example}")
        print()

    input("Press Enter to continue...")


def about_sets():
    """Display information about Python sets."""
    clear_screen()
    print_header("ABOUT PYTHON SETS")

    print("Sets are unordered collections of unique elements.")
    print("They're particularly useful for membership testing and eliminating duplicates.\n")

    print("Key characteristics of Python sets:")
    print("• Unordered: Elements have no defined order")
    print("• Unique Elements: No duplicates allowed")
    print("• Mutable: Regular sets can be modified after creation")
    print("• Immutable Option: Frozen sets (frozenset) cannot be modified")
    print("• Elements must be immutable: Can contain strings, numbers, tuples, frozensets")
    print("• Fast membership testing: 'in' operator is O(1) time complexity")
    print("• Mathematical set operations: union, intersection, difference, etc.\n")

    print("Set examples:")
    for name, example in tuples_and_sets.set_examples().items():
        print(f"• {name}: {example}")

    input("\nPress Enter to continue...")


def set_operations():
    """Display information about set operations."""
    clear_screen()
    print_header("SET OPERATIONS")

    print("Operations that can be performed with sets:\n")

    print("Basic set operations:")
    for name, example in tuples_and_sets.set_operations().items():
        print(f"• {name}: {example}")

    print("\nModifying sets:")
    for name, example in tuples_and_sets.set_modifications().items():
        print(f"• {name}: {example}")

    input("\nPress Enter to continue...")


def set_patterns():
    """Display information about common set patterns and use cases."""
    clear_screen()
    print_header("COMMON SET PATTERNS AND USE CASES")

    print("Sets are used in many programming patterns and scenarios:\n")

    examples = tuples_and_sets.set_use_cases()
    for pattern, example in examples.items():
        print(f"• {pattern}:")
        print(f"  {example}")
        print()

    input("Press Enter to continue...")


def about_application():
    """Display information about the application."""
    clear_screen()
    print_header("ABOUT THIS APPLICATION")

    print("Python Data Structures Learning Application")
    print("Version: 1.1.0\n")

    print("This application is designed to help you learn about Python's")
    print("core data structures through interactive examples and demonstrations.\n")

    print("Core data structures covered:")
    print("• Lists: Ordered, mutable sequences")
    print("• Dictionaries: Key-value mappings")
    print("• Tuples: Ordered, immutable sequences")
    print("• Sets: Unordered collections of unique elements\n")

    print("Each section provides:")
    print("• Basic concepts and characteristics")
    print("• Operations and methods")
    print("• Common patterns and use cases")
    print("• Interactive demonstrations\n")

    print("Application Interfaces:")
    print("• Interactive Menu: Run 'python main.py'")
    print("• Command Line Interface: Run 'python cli.py --help'")
    print("  Examples:")
    print("    - python cli.py lists              # Learn about lists")
    print("    - python cli.py dictionaries ops   # Dictionary operations")
    print("    - python cli.py tuples demo        # Interactive tuples demo")
    print("    - python cli.py sets patterns      # Common set patterns\n")

    print("For more in-depth learning, consider exploring the official Python")
    print("documentation at https://docs.python.org/3/tutorial/datastructures.html")

    input("\nPress Enter to continue...")


def handle_list_menu():
    """Handle the lists submenu."""
    while True:
        choice = print_data_structure_menu("Lists")

        if choice == '1':
            about_lists()
        elif choice == '2':
            list_operations()
        elif choice == '3':
            list_patterns()
        elif choice == '4':
            clear_screen()
            lists.interactive_list_demo()
            input("\nPress Enter to continue...")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)


def handle_dict_menu():
    """Handle the dictionaries submenu."""
    while True:
        choice = print_data_structure_menu("Dictionaries")

        if choice == '1':
            about_dictionaries()
        elif choice == '2':
            dict_operations()
        elif choice == '3':
            dict_patterns()
        elif choice == '4':
            clear_screen()
            dictionaries.interactive_dict_demo()
            input("\nPress Enter to continue...")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)


def handle_tuple_menu():
    """Handle the tuples submenu."""
    while True:
        choice = print_data_structure_menu("Tuples")

        if choice == '1':
            about_tuples()
        elif choice == '2':
            tuple_operations()
        elif choice == '3':
            tuple_patterns()
        elif choice == '4':
            clear_screen()
            tuples_and_sets.interactive_tuple_demo()
            input("\nPress Enter to continue...")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)


def handle_set_menu():
    """Handle the sets submenu."""
    while True:
        choice = print_data_structure_menu("Sets")

        if choice == '1':
            about_sets()
        elif choice == '2':
            set_operations()
        elif choice == '3':
            set_patterns()
        elif choice == '4':
            clear_screen()
            tuples_and_sets.interactive_set_demo()
            input("\nPress Enter to continue...")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)


def main():
    """Main function to run the application."""
    while True:
        choice = print_menu()

        if choice == '1':
            handle_list_menu()
        elif choice == '2':
            handle_dict_menu()
        elif choice == '3':
            handle_tuple_menu()
        elif choice == '4':
            handle_set_menu()
        elif choice == '5':
            about_application()
        elif choice == '6':
            clear_screen()
            print("Thank you for using the Python Data Structures Learning Application!")
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\nProgram terminated by user. Goodbye!")
        sys.exit(0)