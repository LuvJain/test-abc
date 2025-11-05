#!/usr/bin/env python3
"""
CLI Testing Script for Python Data Structures Learning Application

This script tests the CLI interface implementation for the application
by checking if all the necessary components are in place and validating
the argument parsing logic.
"""

import os
import sys
import importlib.util
from unittest import mock


def check_file_exists(filename):
    """Check if a file exists in the current directory."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    exists = os.path.isfile(filepath)
    print(f"Checking for {filename}:", "✅ Found" if exists else "❌ Not found")
    return exists


def check_module_imports(module_name):
    """Check if a module can be imported without errors."""
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            print(f"Checking import of {module_name}: ❌ Module not found")
            return False

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print(f"Checking import of {module_name}: ✅ Successfully imported")
        return True
    except Exception as e:
        print(f"Checking import of {module_name}: ❌ Error: {e}")
        return False


def test_cli_argument_parsing():
    """Test the CLI argument parsing functionality."""
    print("\nTesting CLI argument parsing...")

    # Import cli module
    try:
        import cli

        # Test the argument parser creation
        parser = cli.create_parser()
        if parser:
            print("✅ Successfully created argument parser")

            # Test parsing with different arguments using mock
            test_cases = [
                (["lists"], {"structure": "lists", "action": "about"}),
                (["dictionaries", "ops"], {"structure": "dictionaries", "action": "ops"}),
                (["tuples", "patterns"], {"structure": "tuples", "action": "patterns"}),
                (["sets", "demo"], {"structure": "sets", "action": "demo"}),
                (["--about"], {"about": True, "structure": None})
            ]

            all_passed = True
            for args, expected in test_cases:
                with mock.patch('sys.argv', ['cli.py'] + args):
                    try:
                        parsed_args = parser.parse_args(args)
                        # Check if all expected keys are in the parsed args
                        matches = all(
                            getattr(parsed_args, key, None) == value
                            for key, value in expected.items()
                            if key != "structure" or value is not None
                        )
                        if matches:
                            print(f"✅ Successfully parsed args: {args}")
                        else:
                            print(f"❌ Failed to correctly parse args: {args}")
                            print(f"  Expected: {expected}")
                            print(f"  Got: {parsed_args}")
                            all_passed = False
                    except Exception as e:
                        print(f"❌ Error parsing args {args}: {e}")
                        all_passed = False

            if all_passed:
                print("✅ All argument parsing tests passed")
            else:
                print("❌ Some argument parsing tests failed")
        else:
            print("❌ Failed to create argument parser")

    except Exception as e:
        print(f"❌ Error testing CLI argument parsing: {e}")


def run_tests():
    """Run all tests."""
    print("==== Testing Python Data Structures CLI Implementation ====\n")

    # Check for required files
    files_exist = all([
        check_file_exists("cli.py"),
        check_file_exists("main.py")
    ])

    if not files_exist:
        print("\n❌ Required files are missing. Tests cannot continue.")
        return False

    # Check for required module imports
    imports_ok = all([
        check_module_imports("data_structures.lists"),
        check_module_imports("data_structures.dictionaries"),
        check_module_imports("data_structures.tuples_and_sets")
    ])

    if not imports_ok:
        print("\n❌ Required modules cannot be imported. Tests cannot continue.")
        return False

    # Test CLI argument parsing
    test_cli_argument_parsing()

    print("\n==== Testing Complete ====")
    return True


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)