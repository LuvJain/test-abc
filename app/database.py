from sqlmodel import SQLModel, Session, create_engine
import os
from typing import Generator

# Use environment variable for database URL or default to SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    """Create database tables based on SQLModel models."""
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """Session dependency."""
    with Session(engine) as session:
        yield session