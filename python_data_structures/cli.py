#!/usr/bin/env python3
"""
CLI Interface for Python Data Structures Learning Application

This module provides a command-line interface for the Python Data Structures
Learning Application, allowing users to access different data structure tutorials
and examples directly from the command line.

Usage:
    python cli.py                      # Launch interactive menu
    python cli.py -h/--help            # Show help
    python cli.py lists                # Learn about lists
    python cli.py dictionaries         # Learn about dictionaries
    python cli.py tuples               # Learn about tuples
    python cli.py sets                 # Learn about sets
    python cli.py <structure> about    # Overview of the data structure
    python cli.py <structure> ops      # Operations for the data structure
    python cli.py <structure> patterns # Common patterns for the data structure
    python cli.py <structure> demo     # Interactive demo for the data structure
"""

import sys
import argparse
from data_structures import lists, dictionaries, tuples_and_sets
import main


def create_parser():
    """Create and configure the argument parser for CLI commands."""
    parser = argparse.ArgumentParser(
        description='Python Data Structures Learning Application',
        epilog='Run without arguments for interactive mode.'
    )

    # Add subparsers for different data structures
    subparsers = parser.add_subparsers(dest='structure', help='Data structure to learn about')

    # Lists subcommand
    lists_parser = subparsers.add_parser('lists', help='Learn about Python lists')
    lists_parser.add_argument('action', nargs='?', choices=['about', 'ops', 'patterns', 'demo'],
                          help='Action to perform with lists', default='about')

    # Dictionaries subcommand
    dict_parser = subparsers.add_parser('dictionaries', help='Learn about Python dictionaries')
    dict_parser.add_argument('action', nargs='?', choices=['about', 'ops', 'patterns', 'demo'],
                          help='Action to perform with dictionaries', default='about')

    # Tuples subcommand
    tuples_parser = subparsers.add_parser('tuples', help='Learn about Python tuples')
    tuples_parser.add_argument('action', nargs='?', choices=['about', 'ops', 'patterns', 'demo'],
                           help='Action to perform with tuples', default='about')

    # Sets subcommand
    sets_parser = subparsers.add_parser('sets', help='Learn about Python sets')
    sets_parser.add_argument('action', nargs='?', choices=['about', 'ops', 'patterns', 'demo'],
                          help='Action to perform with sets', default='about')

    # About application command
    parser.add_argument('--about', action='store_true', help='About this application')

    return parser


def handle_lists(action):
    """Handle list-related commands."""
    main.clear_screen()
    if action == 'about':
        main.about_lists()
    elif action == 'ops':
        main.list_operations()
    elif action == 'patterns':
        main.list_patterns()
    elif action == 'demo':
        main.clear_screen()
        lists.interactive_list_demo()
        input("\nPress Enter to continue...")


def handle_dictionaries(action):
    """Handle dictionary-related commands."""
    main.clear_screen()
    if action == 'about':
        main.about_dictionaries()
    elif action == 'ops':
        main.dict_operations()
    elif action == 'patterns':
        main.dict_patterns()
    elif action == 'demo':
        main.clear_screen()
        dictionaries.interactive_dict_demo()
        input("\nPress Enter to continue...")


def handle_tuples(action):
    """Handle tuple-related commands."""
    main.clear_screen()
    if action == 'about':
        main.about_tuples()
    elif action == 'ops':
        main.tuple_operations()
    elif action == 'patterns':
        main.tuple_patterns()
    elif action == 'demo':
        main.clear_screen()
        tuples_and_sets.interactive_tuple_demo()
        input("\nPress Enter to continue...")


def handle_sets(action):
    """Handle set-related commands."""
    main.clear_screen()
    if action == 'about':
        main.about_sets()
    elif action == 'ops':
        main.set_operations()
    elif action == 'patterns':
        main.set_patterns()
    elif action == 'demo':
        main.clear_screen()
        tuples_and_sets.interactive_set_demo()
        input("\nPress Enter to continue...")


def main_cli():
    """Main CLI entry point function."""
    parser = create_parser()
    args = parser.parse_args()

    # If no arguments or help flag, go to interactive mode or show help
    if len(sys.argv) == 1:
        # No arguments provided, run the interactive main program
        main.main()
        return

    # Handle about application
    if args.about:
        main.about_application()
        return

    # Handle data structure commands
    if args.structure:
        if args.structure == 'lists':
            handle_lists(args.action)
        elif args.structure == 'dictionaries':
            handle_dictionaries(args.action)
        elif args.structure == 'tuples':
            handle_tuples(args.action)
        elif args.structure == 'sets':
            handle_sets(args.action)
    else:
        # No valid command provided, show help
        parser.print_help()


if __name__ == "__main__":
    try:
        main_cli()
    except KeyboardInterrupt:
        main.clear_screen()
        print("\nProgram terminated by user. Goodbye!")
        sys.exit(0)