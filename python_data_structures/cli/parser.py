#!/usr/bin/env python3
"""
Command line argument parser for Python Data Structures Learning Application.

This module defines the command line interface for the application,
providing access to data structure examples and interactive demos.
"""

import argparse
import sys
from typing import List, Optional


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser for the CLI.

    Returns:
        argparse.ArgumentParser: Configured parser object
    """
    # Create main parser
    parser = argparse.ArgumentParser(
        description="Python Data Structures Learning Application - CLI",
        epilog="Use 'pyds <command> --help' for more information about a specific command."
    )

    # Add version information
    parser.add_argument(
        '--version',
        action='version',
        version='Python Data Structures Learning App v1.0.0'
    )

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(
        title='commands',
        dest='command',
        help='Available commands'
    )

    # List command
    list_parser = subparsers.add_parser(
        'list',
        help='Learn about Python lists'
    )
    list_parser.add_argument(
        '--info',
        action='store_true',
        help='Show general information about lists'
    )
    list_parser.add_argument(
        '--operations',
        action='store_true',
        help='Show list operations and methods'
    )
    list_parser.add_argument(
        '--patterns',
        action='store_true',
        help='Show common list patterns and use cases'
    )
    list_parser.add_argument(
        '--interactive',
        action='store_true',
        help='Run the interactive list demo'
    )
    list_parser.add_argument(
        '--example',
        choices=['create', 'access', 'modify', 'iterate'],
        help='Show specific list examples'
    )

    # Dictionary command
    dict_parser = subparsers.add_parser(
        'dict',
        help='Learn about Python dictionaries'
    )
    dict_parser.add_argument(
        '--info',
        action='store_true',
        help='Show general information about dictionaries'
    )
    dict_parser.add_argument(
        '--operations',
        action='store_true',
        help='Show dictionary operations and methods'
    )
    dict_parser.add_argument(
        '--patterns',
        action='store_true',
        help='Show common dictionary patterns and use cases'
    )
    dict_parser.add_argument(
        '--interactive',
        action='store_true',
        help='Run the interactive dictionary demo'
    )
    dict_parser.add_argument(
        '--example',
        choices=['create', 'access', 'modify', 'advanced'],
        help='Show specific dictionary examples'
    )

    # Tuple command
    tuple_parser = subparsers.add_parser(
        'tuple',
        help='Learn about Python tuples'
    )
    tuple_parser.add_argument(
        '--info',
        action='store_true',
        help='Show general information about tuples'
    )
    tuple_parser.add_argument(
        '--operations',
        action='store_true',
        help='Show tuple operations'
    )
    tuple_parser.add_argument(
        '--patterns',
        action='store_true',
        help='Show common tuple patterns and use cases'
    )
    tuple_parser.add_argument(
        '--interactive',
        action='store_true',
        help='Run the interactive tuple demo'
    )

    # Set command
    set_parser = subparsers.add_parser(
        'set',
        help='Learn about Python sets'
    )
    set_parser.add_argument(
        '--info',
        action='store_true',
        help='Show general information about sets'
    )
    set_parser.add_argument(
        '--operations',
        action='store_true',
        help='Show set operations'
    )
    set_parser.add_argument(
        '--patterns',
        action='store_true',
        help='Show common set patterns and use cases'
    )
    set_parser.add_argument(
        '--interactive',
        action='store_true',
        help='Run the interactive set demo'
    )

    # Info command
    info_parser = subparsers.add_parser(
        'info',
        help='Show information about the application'
    )

    return parser


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse the command line arguments.

    Args:
        args: Command line arguments to parse. Defaults to sys.argv if None.

    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = create_parser()
    parsed_args = parser.parse_args(args)

    # If no command is provided, show help
    if not parsed_args.command:
        parser.print_help()
        sys.exit(0)

    return parsed_args