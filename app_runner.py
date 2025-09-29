#!/usr/bin/env python3
"""
Runner script for the Hello World application.
This script provides a simple way to run the application and tests for users learning Python.
"""
import os
import sys
import subprocess
import time
from datetime import datetime


class AppRunner:
    """
    A helper class to run and demonstrate the Hello World application.
    """
    
    def __init__(self):
        """Initialize the application runner."""
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
    
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title):
        """Print a formatted header."""
        self.clear_screen()
        print("\n" + "=" * 60)
        print(f"{title:^60}")
        print("=" * 60 + "\n")
    
    def pause(self):
        """Pause execution until user presses Enter."""
        input("\nPress Enter to continue...")
    
    def run_command(self, cmd, cwd=None):
        """Run a shell command and capture output."""
        try:
            cwd = cwd or self.script_dir
            result = subprocess.run(
                cmd,
                cwd=cwd,
                check=False,
                text=True,
                capture_output=True,
                shell=True
            )
            return result.stdout
        except Exception as e:
            return f"Error: {str(e)}"
    
    def show_main_menu(self):
        """Display the main menu and get user choice."""
        self.print_header("PYTHON HELLO WORLD APP")
        
        print("Learn Python with this simple Hello World application!")
        print("\nOptions:")
        print("1. Run the basic Hello World app")
        print("2. Run the simple web app example")
        print("3. Run the tests")
        print("4. Explore project structure")
        print("5. Exit")
        
        return input("\nEnter your choice (1-5): ").strip()
    
    def run_hello_world(self):
        """Run the basic Hello World application."""
        self.print_header("RUNNING HELLO WORLD APP")
        print("This will run the basic Hello World application (app/main.py).\n")
        
        print("Output:\n")
        output = self.run_command("python -m app.main")
        print(output)
        
        print("\nThis example demonstrates:")
        print("- Basic Python module structure")
        print("- String formatting with f-strings")
        print("- Function definitions and documentation")
        print("- Basic logging")
        print("- Working with timestamps")
        
        self.pause()
    
    def run_web_app_example(self):
        """Run the web app example."""
        self.print_header("RUNNING WEB APP EXAMPLE")
        print("This will run the web application example (app/app.py).\n")
        
        print("Output:\n")
        output = self.run_command("python -m app.app")
        print(output)
        
        print("\nThis example demonstrates:")
        print("- Object-oriented programming in Python")
        print("- Working with classes and methods")
        print("- Data structures like dictionaries and lists")
        print("- Simple request handling")
        print("- Working with JSON data")
        
        self.pause()
    
    def run_tests(self):
        """Run the application tests."""
        self.print_header("RUNNING TESTS")
        print("This will run the test suite using pytest.\n")
        
        print("Available tests:")
        print("- test_app.py: Tests for the web application structure")
        print("- test_main.py: Tests for the basic Hello World functionality")
        print("- test_models.py: Tests for the data models\n")
        
        choice = input("Run all tests or specific test file? (all/app/main/models): ").strip().lower()
        
        command = "python -m pytest -v"
        if choice == "app":
            command += " tests/test_app.py"
        elif choice == "main":
            command += " tests/test_main.py"
        elif choice == "models":
            command += " tests/test_models.py"
        
        print("\nRunning tests...\n")
        output = self.run_command(command)
        print(output)
        
        print("\nTests demonstrate:")
        print("- How to write unit tests in Python")
        print("- How to use pytest for testing")
        print("- How to use assertions to validate code")
        print("- How to test different parts of your application")
        
        self.pause()
    
    def explore_structure(self):
        """Explore the project structure."""
        self.print_header("PROJECT STRUCTURE")
        print("This Hello World app demonstrates a simple Python project structure.\n")
        
        print("Directory structure:")
        output = self.run_command("find . -type f -name '*.py' | sort")
        print(output)
        
        print("\nCore components:")
        print("- app/main.py: Basic Hello World implementation")
        print("- app/app.py: Simple web application example")
        print("- app/models.py: Data models for the application")
        print("- tests/: Test files for different components")
        
        self.pause()
    
    def run(self):
        """Run the main application loop."""
        while True:
            choice = self.show_main_menu()
            
            if choice == '1':
                self.run_hello_world()
            elif choice == '2':
                self.run_web_app_example()
            elif choice == '3':
                self.run_tests()
            elif choice == '4':
                self.explore_structure()
            elif choice == '5':
                self.print_header("GOODBYE!")
                print("Thanks for exploring the Python Hello World application!")
                print("Happy coding!\n")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)


if __name__ == "__main__":
    runner = AppRunner()
    runner.run()