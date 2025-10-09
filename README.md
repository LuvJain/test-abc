# Notes Application

A simple notes application with FastAPI backend and CLI interface.

## Features

- Create, read, update, and delete notes
- RESTful API with FastAPI
- CLI interface for easy management

## Installation

1. Clone the repository:

```bash
git clone https://github.com/LuvJain/test-abc.git
cd test-abc
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

The API will be available at `http://localhost:8000`.

## API Documentation

Once the server is running, you can access the API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## CLI Usage

The CLI interface provides an easy way to manage your notes from the command line.

### Prerequisites

Make sure the API server is running before using the CLI.

### Commands

#### Create a new note

```bash
python cli.py create --title "Note Title" --content "Note content goes here"
```

#### List all notes

```bash
python cli.py list
```

You can also use pagination:

```bash
python cli.py list --skip 10 --limit 5
```

#### Get a specific note

```bash
python cli.py get NOTE_ID
```

Replace `NOTE_ID` with the actual ID of the note.

#### Update a note

```bash
python cli.py update NOTE_ID --title "New Title" --content "Updated content"
```

You can update either title, content, or both.

#### Delete a note

```bash
python cli.py delete NOTE_ID
```

Add the `--force` or `-f` flag to delete without confirmation:

```bash
python cli.py delete NOTE_ID --force
```

## API Endpoints

- `GET /notes/`: List all notes
- `POST /notes/`: Create a new note
- `GET /notes/{note_id}`: Get a specific note
- `PATCH /notes/{note_id}`: Update a note
- `DELETE /notes/{note_id}`: Delete a note

## Development

### Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Click (for CLI)
