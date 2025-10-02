from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, status
from sqlmodel import Session, select
from typing import List
import logging

from ..database import get_session
from ..models import Document, DocumentSummary, DocumentResponse, SummaryResponse
from ..utils.pdf_utils import PDFParser, DocumentSummarizer

router = APIRouter(prefix="/documents", tags=["documents"])

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_session)
):
    """
    Upload a document (PDF) to the system
    """
    # Check if the file is a PDF
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are supported"
        )

    try:
        # Read file content
        file_content = await file.read()

        # Extract text from PDF
        text_content = PDFParser.extract_text_from_pdf(file_content)

        # Create document record
        document = Document(
            filename=file.filename,
            content=text_content
        )

        # Save to database
        db.add(document)
        db.commit()
        db.refresh(document)

        return DocumentResponse(
            id=document.id,
            filename=document.filename,
            created_at=document.created_at
        )

    except Exception as e:
        logger.error(f"Error uploading document: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error uploading document: {str(e)}"
        )

@router.get("/{document_id}/summarize", response_model=SummaryResponse)
async def summarize_document(
    document_id: int,
    db: Session = Depends(get_session)
):
    """
    Generate a summary for a specific document
    """
    # Find the document
    document = db.exec(select(Document).where(Document.id == document_id)).first()
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )

    try:
        # Create summarizer
        summarizer = DocumentSummarizer(document.content)

        # Generate summary (less than 10 sentences as per requirements)
        summary_text, keywords = summarizer.summarize_document(max_sentences=9)

        # Save summary to database
        document_summary = DocumentSummary(
            document_id=document.id,
            summary_text=summary_text,
            keywords=",".join(keywords)
        )

        db.add(document_summary)
        db.commit()
        db.refresh(document_summary)

        return SummaryResponse.from_db_model(document_summary)

    except Exception as e:
        logger.error(f"Error summarizing document: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error summarizing document: {str(e)}"
        )

@router.get("/", response_model=List[DocumentResponse])
async def list_documents(
    db: Session = Depends(get_session)
):
    """
    List all uploaded documents
    """
    documents = db.exec(select(Document)).all()
    return [
        DocumentResponse(
            id=doc.id,
            filename=doc.filename,
            created_at=doc.created_at
        ) for doc in documents
    ]