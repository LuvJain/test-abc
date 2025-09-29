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

### Basic Hello World

Run the main script:
```
python -m app.main
```

### Web Application Example

Run the app example:
```
python -m app.app
```

### Using FastAPI (if installed)

Start the web server:
```
uvicorn app.main:app --reload
```

## Running Tests

Run all tests with coverage:
```
python -m pytest
```

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
