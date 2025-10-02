from sqlmodel import SQLModel, create_engine, Session
import os

# Database URL - using SQLite for simplicity
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./document_parser.db")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    """Initialize the database and create tables"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Get a database session"""
    with Session(engine) as session:
        yield session