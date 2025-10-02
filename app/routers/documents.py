from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, status, Body
from sqlmodel import Session, select
from typing import List
import logging
import os
import base64

from ..database import get_session
from ..models import Document, DocumentSummary, DocumentResponse, SummaryResponse
from ..utils.pdf_utils import PDFParser, DocumentSummarizer
from ..utils.sample_generator import create_sample_pdf, create_sample_documents

router = APIRouter(prefix="/documents", tags=["documents"])

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Path to sample documents directory
SAMPLE_DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sample_docs")

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

@router.post("/samples/generate", response_model=List[DocumentResponse])
async def generate_sample_documents(
    num_samples: int = Body(3, embed=True),
    db: Session = Depends(get_session)
):
    """
    Generate multiple sample documents and add them to the database

    Args:
        num_samples: Number of sample documents to generate (default: 3)

    Returns:
        List[DocumentResponse]: List of created document entities
    """
    if num_samples < 1 or num_samples > 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Number of samples must be between 1 and 10"
        )

    try:
        # Generate sample documents
        sample_paths = create_sample_documents(SAMPLE_DOCS_DIR, num_samples)

        # Process each generated document
        document_responses = []
        for sample_path in sample_paths:
            # Read the sample file
            with open(sample_path, 'rb') as f:
                pdf_content = f.read()

            # Extract text
            text_content = PDFParser.extract_text_from_pdf(pdf_content)

            # Create document record
            document = Document(
                filename=os.path.basename(sample_path),
                content=text_content
            )

            # Save to database
            db.add(document)
            db.commit()
            db.refresh(document)

            # Add to response list
            document_responses.append(DocumentResponse(
                id=document.id,
                filename=document.filename,
                created_at=document.created_at
            ))

        return document_responses

    except Exception as e:
        logger.error(f"Error generating sample documents: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating sample documents: {str(e)}"
        )

@router.post("/sample", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
async def process_sample_document(
    sample_name: str = Body(..., embed=True),
    db: Session = Depends(get_session)
):
    """
    Process a sample document from the sample_docs directory

    Args:
        sample_name: Name of the sample document (e.g., 'sample1.pdf')

    Returns:
        DocumentResponse: The created document entity
    """
    # Ensure sample documents directory exists
    os.makedirs(SAMPLE_DOCS_DIR, exist_ok=True)

    # Check if the requested sample exists
    sample_path = os.path.join(SAMPLE_DOCS_DIR, sample_name)

    if not os.path.isfile(sample_path):
        # If the sample doesn't exist, create a sample PDF
        try:
            logger.info(f"Creating sample document: {sample_name}")
            # Use our sample_generator utility to create the PDF
            create_sample_pdf(sample_path)

            # Read the newly created PDF
            with open(sample_path, 'rb') as f:
                pdf_content = f.read()

            # Extract text from the PDF
            text_content = PDFParser.extract_text_from_pdf(pdf_content)

        except Exception as e:
            logger.error(f"Error creating sample document: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error creating sample document: {str(e)}"
            )
    else:
        # If the sample exists, read it
        try:
            with open(sample_path, 'rb') as f:
                pdf_content = f.read()

            # Extract text from the PDF
            text_content = PDFParser.extract_text_from_pdf(pdf_content)

        except Exception as e:
            logger.error(f"Error reading sample document: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error reading sample document: {str(e)}"
            )

    try:
        # Create document record
        document = Document(
            filename=sample_name,
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
        logger.error(f"Error processing sample document: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing sample document: {str(e)}"
        )