"""
Tests for the Document Parser API
"""
from fastapi.testclient import TestClient
import os
import pytest
from sqlmodel import SQLModel, create_engine, Session
from sqlmodel.pool import StaticPool

from app.main import app
from app.database import get_session
from app.models import Document

# Create a test database in memory
TEST_DATABASE_URL = "sqlite://"

@pytest.fixture
def client():
    """Create a test client with an in-memory database"""
    # Create test engine
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    # Create tables
    SQLModel.metadata.create_all(engine)

    # Override the get_session dependency
    def get_test_session():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_session] = get_test_session

    # Create test client
    with TestClient(app) as client:
        yield client

    # Clean up
    SQLModel.metadata.drop_all(engine)

def test_root_endpoint(client):
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Document Parser API is running"

def test_list_documents_empty(client):
    """Test listing documents when none exist"""
    response = client.get("/documents/")
    assert response.status_code == 200
    assert response.json() == []

def test_document_not_found(client):
    """Test summarizing a non-existent document"""
    response = client.get("/documents/999/summarize")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

# Note: Testing file uploads would require creating a mock PDF file,
# which is more complex and would be better handled in a separate test module