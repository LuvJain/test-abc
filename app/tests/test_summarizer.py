"""
Tests for the document summarization functionality
"""
import unittest
from app.utils.pdf_utils import DocumentSummarizer

class TestDocumentSummarizer(unittest.TestCase):
    """Test cases for document summarization"""

    def test_summarization_length(self):
        """Test that summary is less than 10 sentences"""
        # Sample text with multiple sentences
        sample_text = """
        This is the first sentence of a sample document. This is the second sentence with some additional information.
        The third sentence contains details about a specific topic. In the fourth sentence, we explore more nuances.
        The fifth sentence provides some examples. The sixth sentence adds more context to understand the topic better.
        We can add a seventh sentence for more depth. The eighth sentence elaborates on previous points.
        A ninth sentence continues the explanation. The tenth sentence wraps up the main idea.
        An eleventh sentence adds a conclusion. The twelfth sentence provides a final thought.
        """

        # Create summarizer
        summarizer = DocumentSummarizer(sample_text)

        # Generate summary
        summary, keywords = summarizer.summarize_document(max_sentences=9)

        # Split summary into sentences
        summary_sentences = summary.split(".")
        # Remove empty strings that might come from split
        summary_sentences = [s.strip() for s in summary_sentences if s.strip()]

        # Check that summary has less than 10 sentences
        self.assertLessEqual(len(summary_sentences), 9,
            f"Summary should have at most 9 sentences, but has {len(summary_sentences)}")

    def test_keyword_extraction(self):
        """Test that keyword extraction works properly"""
        # Sample text with some keywords
        sample_text = """
        Machine learning is a field of study that gives computers the ability to learn
        without being explicitly programmed. Machine learning algorithms build a model based
        on sample data, known as training data, in order to make predictions or decisions
        without being explicitly programmed to do so. Machine learning algorithms are used in
        a wide variety of applications, such as email filtering and computer vision, where it is
        difficult or unfeasible to develop conventional algorithms to perform the needed tasks.
        """

        # Create summarizer
        summarizer = DocumentSummarizer(sample_text)

        # Get keywords
        keywords = summarizer.get_top_keywords(5)

        # Check that we got the expected number of keywords
        self.assertEqual(len(keywords), 5, f"Expected 5 keywords, but got {len(keywords)}")

        # Check that relevant keywords were extracted
        expected_keywords = ['machine', 'learning', 'algorithms', 'programmed', 'data']
        for keyword in expected_keywords:
            self.assertIn(keyword, keywords, f"Expected keyword '{keyword}' not found")

if __name__ == "__main__":
    unittest.main()