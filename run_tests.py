#!/usr/bin/env python3
"""
Test runner script for the Hello World application.
This script demonstrates how to run the pytest tests for this application.
"""
import os
import sys
import subprocess


def run_tests():
    """
    Run the pytest tests for the Hello World application.
    
    Returns:
        int: The exit code of the pytest command.
    """
    print("\n=== Running Hello World App Tests ===\n")
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set up the pytest command
    pytest_cmd = [
        "python", "-m", "pytest", "-v",
        "--cov=app",
        "--cov-report=term-missing"
    ]
    
    # Run the pytest command
    try:
        result = subprocess.run(
            pytest_cmd,
            cwd=script_dir,
            check=False,
            text=True,
            capture_output=True
        )
        
        # Print the output
        print(result.stdout)
        
        if result.stderr:
            print("\nErrors:")
            print(result.stderr)
        
        # Print summary
        if result.returncode == 0:
            print("\n✅ All tests passed successfully!")
        else:
            print(f"\n❌ Some tests failed (exit code: {result.returncode})")
        
        return result.returncode
        
    except Exception as e:
        print(f"Error running tests: {e}")
        return 1


def print_test_structure():
    """
    Print information about the test structure of the project.
    """
    print("\n=== Test Structure Information ===\n")
    print("The Hello World application uses pytest for testing.")
    print("Test files are organized in the 'tests/' directory:")
    print("  - tests/test_app.py: Tests for the SimpleApp class")
    print("  - tests/test_models.py: Tests for data models like Greeting")
    print("  - tests/test_main.py: Tests for the main entry point functions\n")
    print("Configuration is in pytest.ini, including test paths and coverage settings.")


def main():
    """
    Main entry point for the test runner script.
    """
    print("\n=== Hello World App Test Runner ===")
    print("This script helps you run tests for the Hello World Python application")
    
    print_test_structure()
    
    # Prompt to run tests
    choice = input("\nDo you want to run the tests now? (y/n): ").strip().lower()
    
    if choice == 'y':
        exit_code = run_tests()
        sys.exit(exit_code)
    else:
        print("\nTests not run. You can run tests manually with: python -m pytest")
        sys.exit(0)


if __name__ == "__main__":
    main()