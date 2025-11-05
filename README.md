# GraphQL Server with Flask and Graphene

A basic GraphQL server implemented using Flask and Graphene to understand core GraphQL concepts in Python.

## Features

- GraphQL endpoint at `/graphql`
- GraphiQL interactive interface for testing queries
- Simple schema with Author and Book types
- Support for basic query operations
- Relationship between types (Author has many Books)

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the server

Start the server with:

```bash
python main.py
```

The server will run at http://localhost:5000 with the GraphiQL interface available at http://localhost:5000/graphql

## Testing

Run the tests with:

```bash
pytest test_schema.py -v
```

## Sample Queries

See the `sample_queries.md` file for example GraphQL queries you can use to test the API.

## Project Structure

- `app/`: Main application package
  - `models/`: Data models and sample data
  - `schema/`: GraphQL schema and resolvers
- `main.py`: Application entry point
- `test_schema.py`: Unit tests for the GraphQL schema
- `sample_queries.md`: Example GraphQL queries
