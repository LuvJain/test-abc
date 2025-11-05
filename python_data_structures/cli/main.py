#!/usr/bin/env python3
"""
Main entry point for the CLI interface.

This module provides the main function that starts the CLI application.
"""

import sys
from .parser import parse_args
from .handlers import dispatch_command


def main() -> None:
    """
    Main entry point for the CLI application.

    Parses command line arguments and dispatches to the appropriate handler.
    """
    try:
        args = parse_args()
        dispatch_command(args)
    except KeyboardInterrupt:
        print("\nProgram terminated by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()