import os
import PyPDF2
import io
from typing import Tuple, List, Dict
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Download necessary NLTK resources
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
except Exception as e:
    logger.warning(f"Failed to download NLTK resources: {e}")
    logger.info("Continuing without NLTK downloads - this may affect performance")

class PDFParser:
    """Utility class for parsing PDF documents"""

    @staticmethod
    def extract_text_from_pdf(pdf_file) -> str:
        """
        Extract text content from a PDF file

        Args:
            pdf_file: A file-like object or bytes containing the PDF

        Returns:
            str: The extracted text content
        """
        try:
            if isinstance(pdf_file, bytes):
                pdf_file = io.BytesIO(pdf_file)

            # Create PDF reader object
            reader = PyPDF2.PdfReader(pdf_file)

            # Extract text from each page
            text = ""
            for page in reader.pages:
                text += page.extract_text()

            return text
        except Exception as e:
            logger.error(f"Error extracting text from PDF: {e}")
            raise ValueError(f"Could not extract text from PDF: {str(e)}")

class DocumentSummarizer:
    """Utility class for summarizing document text"""

    def __init__(self, text: str):
        """
        Initialize with document text

        Args:
            text (str): The document text to summarize
        """
        self.text = text
        self.sentences = []
        self.clean_text()

    def clean_text(self):
        """Clean and prepare the text for processing"""
        # Remove extra whitespace
        self.text = re.sub(r'\s+', ' ', self.text).strip()

        # Split into sentences
        self.sentences = sent_tokenize(self.text)

    def get_top_keywords(self, num_keywords: int = 10) -> List[str]:
        """
        Extract the top keywords from the document

        Args:
            num_keywords (int): Number of keywords to extract

        Returns:
            List[str]: List of top keywords
        """
        # Tokenize the text into words
        words = word_tokenize(self.text.lower())

        # Get stopwords
        stop_words = set(stopwords.words('english'))

        # Filter out stopwords and non-alphabetic tokens
        filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

        # Count word frequencies
        word_freq = Counter(filtered_words)

        # Get the most common words
        top_keywords = [keyword for keyword, _ in word_freq.most_common(num_keywords)]

        return top_keywords

    def generate_summary(self, max_sentences: int = 5) -> str:
        """
        Generate a summary of the document

        Args:
            max_sentences (int): Maximum number of sentences in the summary

        Returns:
            str: The generated summary
        """
        if not self.sentences:
            return "Could not generate summary: No sentences found in the document."

        # If we have fewer sentences than the max, use all of them
        if len(self.sentences) <= max_sentences:
            return " ".join(self.sentences)

        # Simple extractive summarization - take first few sentences
        # This is a basic approach; more sophisticated methods could be implemented
        summary = " ".join(self.sentences[:max_sentences])

        return summary

    def summarize_document(self, max_sentences: int = 9) -> Tuple[str, List[str]]:
        """
        Generate a complete document summary with keywords

        Args:
            max_sentences (int): Maximum number of sentences in the summary

        Returns:
            Tuple[str, List[str]]: A tuple containing the summary text and a list of keywords
        """
        summary = self.generate_summary(max_sentences)
        keywords = self.get_top_keywords(10)

        return summary, keywords