#!/usr/bin/env python3
"""
Command handlers for the CLI interface.

This module contains the functions that handle the different CLI commands
and connect them to the appropriate data structure modules.
"""

import argparse
import sys

# Import the data structure modules from the parent package
from .. import main
from ..data_structures import lists, dictionaries, tuples_and_sets


def handle_list_command(args: argparse.Namespace) -> None:
    """
    Handle the 'list' command and its options.

    Args:
        args: Command line arguments
    """
    # If no options specified, show general info
    if not any([args.info, args.operations, args.patterns, args.interactive, args.example]):
        main.about_lists()
        return

    # Handle specific options
    if args.info:
        main.about_lists()
    if args.operations:
        main.list_operations()
    if args.patterns:
        main.list_patterns()
    if args.interactive:
        # Clear screen before interactive demo
        main.clear_screen()
        lists.interactive_list_demo()
        print("\nPress Enter to continue...")
        input()

    if args.example:
        main.clear_screen()
        main.print_header(f"LIST {args.example.upper()} EXAMPLES")

        if args.example == 'create':
            examples = lists.create_list_examples()
            for name, example in examples.items():
                print(f"• {name}: {example}")
        elif args.example == 'access':
            sample_list = [10, 20, 30, 40, 50, 60, 70]
            print(f"Sample list: {sample_list}")
            examples = lists.list_access_examples(sample_list)
            for name, example in examples.items():
                print(f"• {name}: {example}")
        elif args.example == 'modify':
            examples = lists.list_modification_examples()
            for name, example in examples.items():
                print(f"• {name}: {example}")
        elif args.example == 'iterate':
            examples = lists.list_iteration_examples()
            for name, example in examples.items():
                print(f"• {name}: {example}")


def handle_dict_command(args: argparse.Namespace) -> None:
    """
    Handle the 'dict' command and its options.

    Args:
        args: Command line arguments
    """
    # If no options specified, show general info
    if not any([args.info, args.operations, args.patterns, args.interactive, args.example]):
        main.about_dictionaries()
        return

    # Handle specific options
    if args.info:
        main.about_dictionaries()
    if args.operations:
        main.dict_operations()
    if args.patterns:
        main.dict_patterns()
    if args.interactive:
        # Clear screen before interactive demo
        main.clear_screen()
        dictionaries.interactive_dict_demo()
        print("\nPress Enter to continue...")
        input()

    if args.example:
        main.clear_screen()
        main.print_header(f"DICTIONARY {args.example.upper()} EXAMPLES")

        if args.example == 'create':
            examples = dictionaries.create_dict_examples()
            for name, example in examples.items():
                print(f"• {name}: {example}")
        elif args.example == 'access':
            examples = dictionaries.dict_access_examples()
            for name, example in examples.items():
                print(f"• {name}: {example}")
        elif args.example == 'modify':
            examples = dictionaries.dict_modification_examples()
            for name, example in examples.items():
                print(f"• {name}: {example}")
        elif args.example == 'advanced':
            examples = dictionaries.dict_advanced_examples()
            for name, example in examples.items():
                print(f"• {name}: {example}")


def handle_tuple_command(args: argparse.Namespace) -> None:
    """
    Handle the 'tuple' command and its options.

    Args:
        args: Command line arguments
    """
    # If no options specified, show general info
    if not any([args.info, args.operations, args.patterns, args.interactive]):
        main.about_tuples()
        return

    # Handle specific options
    if args.info:
        main.about_tuples()
    if args.operations:
        main.tuple_operations()
    if args.patterns:
        main.tuple_patterns()
    if args.interactive:
        # Clear screen before interactive demo
        main.clear_screen()
        tuples_and_sets.interactive_tuple_demo()
        print("\nPress Enter to continue...")
        input()


def handle_set_command(args: argparse.Namespace) -> None:
    """
    Handle the 'set' command and its options.

    Args:
        args: Command line arguments
    """
    # If no options specified, show general info
    if not any([args.info, args.operations, args.patterns, args.interactive]):
        main.about_sets()
        return

    # Handle specific options
    if args.info:
        main.about_sets()
    if args.operations:
        main.set_operations()
    if args.patterns:
        main.set_patterns()
    if args.interactive:
        # Clear screen before interactive demo
        main.clear_screen()
        tuples_and_sets.interactive_set_demo()
        print("\nPress Enter to continue...")
        input()


def handle_info_command(args: argparse.Namespace) -> None:
    """
    Handle the 'info' command.

    Args:
        args: Command line arguments
    """
    main.about_application()


def dispatch_command(args: argparse.Namespace) -> None:
    """
    Dispatch to the appropriate command handler based on the args.

    Args:
        args: Command line arguments
    """
    # Map commands to their handler functions
    handlers = {
        'list': handle_list_command,
        'dict': handle_dict_command,
        'tuple': handle_tuple_command,
        'set': handle_set_command,
        'info': handle_info_command
    }

    # Call the appropriate handler
    if args.command in handlers:
        try:
            handlers[args.command](args)
        except KeyboardInterrupt:
            main.clear_screen()
            print("\nOperation interrupted by user. Exiting...")
            sys.exit(0)
    else:
        print(f"Unknown command: {args.command}")
        sys.exit(1)