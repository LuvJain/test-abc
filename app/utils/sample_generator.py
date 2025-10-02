"""
Sample document generator utility
This module provides functions to create sample PDF documents for testing the document parsing functionality
"""

import os
import logging
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_sample_pdf(output_path, content=None):
    """
    Create a sample PDF document with provided or default content

    Args:
        output_path (str): Path where the PDF file will be saved
        content (dict, optional): Dictionary containing content for the PDF
                                 Default content will be used if not provided

    Returns:
        str: Path to the created PDF file
    """
    # Default content if none provided
    if content is None:
        content = {
            "title": "Sample Document for Document Parser",
            "paragraphs": [
                "This is a sample document created for testing purposes.",
                "It contains sample text that can be used to test the document parsing functionality.",
                "The document parser should be able to extract text from this document.",
            ],
            "key_points": [
                "Document parsing capabilities",
                "Text extraction from PDFs",
                "Summarization algorithms",
                "Keyword extraction techniques",
                "Natural language processing"
            ]
        }

    try:
        # Create a PDF file
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)

        # Add title
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, 750, content.get("title", "Sample Document"))

        # Add paragraphs
        c.setFont("Helvetica", 12)
        y_position = 700
        for paragraph in content.get("paragraphs", []):
            c.drawString(100, y_position, paragraph)
            y_position -= 50

        # Add key points
        if "key_points" in content and content["key_points"]:
            c.drawString(100, y_position, "Key points in this document include:")
            y_position -= 30

            c.setFont("Helvetica", 10)
            for i, point in enumerate(content["key_points"], 1):
                c.drawString(120, y_position, f"{i}. {point}")
                y_position -= 30

        c.save()

        # Get PDF content
        pdf_content = buffer.getvalue()
        buffer.close()

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Write PDF to file
        with open(output_path, 'wb') as f:
            f.write(pdf_content)

        logger.info(f"Sample PDF created successfully at: {output_path}")
        return output_path

    except Exception as e:
        logger.error(f"Error creating sample PDF: {e}")
        raise

def create_sample_documents(output_dir, num_samples=3):
    """
    Create multiple sample PDF documents with different content

    Args:
        output_dir (str): Directory where the PDF files will be saved
        num_samples (int, optional): Number of sample documents to create. Default is 3.

    Returns:
        list: List of paths to the created PDF files
    """
    sample_paths = []

    # Sample 1: Basic sample
    basic_content = {
        "title": "Basic Sample Document",
        "paragraphs": [
            "This is a basic sample document for testing the document parser.",
            "It contains simple text content that can be extracted and analyzed.",
            "The parser should identify the main topics and provide a concise summary."
        ],
        "key_points": [
            "Document parsing",
            "Text extraction",
            "Topic identification",
            "Summary generation",
            "Keyword extraction"
        ]
    }

    # Sample 2: Technical document
    technical_content = {
        "title": "Technical Document Sample",
        "paragraphs": [
            "This technical document describes the architecture of a document parsing system.",
            "The system uses natural language processing techniques to analyze text content.",
            "Key components include tokenization, sentence segmentation, and keyword extraction.",
            "The summarization algorithm ranks sentences by importance using TF-IDF scoring."
        ],
        "key_points": [
            "System architecture",
            "NLP techniques",
            "Tokenization methods",
            "TF-IDF scoring",
            "Sentence ranking algorithms",
            "Performance optimization"
        ]
    }

    # Sample 3: Business document
    business_content = {
        "title": "Business Report Sample",
        "paragraphs": [
            "This quarterly business report highlights key performance indicators.",
            "Revenue increased by 15% compared to the previous quarter.",
            "Customer acquisition costs decreased by 8% due to improved marketing strategies.",
            "The new product line exceeded sales projections by 20%.",
            "Expansion into new markets is planned for the next quarter."
        ],
        "key_points": [
            "Revenue growth",
            "Cost reduction",
            "Marketing efficiency",
            "Product performance",
            "Market expansion",
            "Strategic planning"
        ]
    }

    # Create samples based on the requested number
    content_samples = [basic_content, technical_content, business_content]
    for i in range(min(num_samples, len(content_samples))):
        sample_path = os.path.join(output_dir, f"sample{i+1}.pdf")
        path = create_sample_pdf(sample_path, content_samples[i])
        sample_paths.append(path)

    # If more samples are requested than we have predefined content for
    for i in range(len(content_samples), num_samples):
        sample_path = os.path.join(output_dir, f"sample{i+1}.pdf")
        path = create_sample_pdf(sample_path)  # Use default content
        sample_paths.append(path)

    return sample_paths