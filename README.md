# Python Hello World Application

A simple Python application demonstrating Python fundamentals with a Hello World example.

## Project Structure

```
./
├── app/                   # Main application package
│   ├── __init__.py       # Package initialization
│   ├── app.py            # Web application structure example
│   ├── main.py           # Entry point with Hello World functionality
│   └── models.py         # Example data models
├── tests/                # Test directory
│   ├── __init__.py       # Test package initialization
│   ├── test_app.py       # Tests for app.py
│   ├── test_main.py      # Tests for main.py
│   └── test_models.py    # Tests for models.py
├── pytest.ini           # Pytest configuration
├── requirements.txt      # Python dependencies
├── run_tests.py         # Helper script to run tests with guidance
├── app_runner.py        # Interactive runner script for the application
├── TESTING_GUIDE.md     # Comprehensive guide to testing the application
└── README.md            # This file
```

## Installation

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

You can run the application in several ways:

### Using the Interactive App Runner

The application includes an interactive runner script that guides you through running the app and exploring its features:

```
python app_runner.py
```

This script provides a user-friendly menu that allows you to:
- Run the basic Hello World app
- Run the web app example
- Run tests
- Explore the project structure

### Basic Hello World

Run the main script directly:
```
python -m app.main
```

### Web Application Example

Run the app example directly:
```
python -m app.app
```

### Using FastAPI (if installed)

Start the web server:
```
uvicorn app.main:app --reload
```

## Running Tests

You can run tests in several ways:

### Using the Test Runner Script

The application includes a test runner script that provides information about the test structure and runs the tests with proper configuration:

```
python run_tests.py
```

### Using pytest directly

Run all tests with coverage:
```
python -m pytest
```

### Run specific test files

```
python -m pytest tests/test_app.py
python -m pytest tests/test_models.py
python -m pytest tests/test_main.py
```

For a comprehensive guide on testing, including explanations of test output, coverage reporting, and writing your own tests, see the [TESTING_GUIDE.md](TESTING_GUIDE.md) file.

## Python Features Demonstrated

- Type hints and annotations
- Docstrings and documentation
- Object-oriented programming with classes
- Dataclasses for data models
- Logging for application events
- Testing with pytest
- Simple web application structure
- Package organization
- Error handling
