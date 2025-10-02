from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

class Document(SQLModel, table=True):
    """Model for storing document information"""
    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str
    content: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class DocumentSummary(SQLModel, table=True):
    """Model for storing document summaries"""
    id: Optional[int] = Field(default=None, primary_key=True)
    document_id: int = Field(foreign_key="document.id")
    summary_text: str
    keywords: str  # Stored as comma-separated values
    created_at: datetime = Field(default_factory=datetime.now)

# Pydantic models for API
class DocumentCreate(BaseModel):
    filename: str

class DocumentResponse(BaseModel):
    id: int
    filename: str
    created_at: datetime

class SummaryResponse(BaseModel):
    id: int
    document_id: int
    summary_text: str
    keywords: List[str]
    created_at: datetime

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "document_id": 1,
                "summary_text": "This is a summary of the document that contains less than 10 sentences.",
                "keywords": ["keyword1", "keyword2", "keyword3"],
                "created_at": "2023-01-01T12:00:00"
            }
        }

    @classmethod
    def from_db_model(cls, db_model: DocumentSummary):
        """Convert database model to response model"""
        return cls(
            id=db_model.id,
            document_id=db_model.document_id,
            summary_text=db_model.summary_text,
            keywords=db_model.keywords.split(","),
            created_at=db_model.created_at
        )