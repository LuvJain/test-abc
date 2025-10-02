#!/usr/bin/env python3
"""
Script to generate sample documents for testing the document parser application

Usage:
    python generate_samples.py [--num NUM] [--output DIR]

Options:
    --num NUM      Number of sample documents to generate (default: 3)
    --output DIR   Directory where sample documents will be saved (default: ../app/sample_docs)
"""

import os
import sys
import argparse
import logging
from pathlib import Path

# Add the parent directory to the path so we can import from the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the sample_generator module
try:
    from app.utils.sample_generator import create_sample_documents
except ImportError:
    print("Error: Could not import sample_generator module.")
    print("Make sure you're running this script from the scripts directory.")
    sys.exit(1)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main entry point for the script"""
    parser = argparse.ArgumentParser(description='Generate sample documents for testing')
    parser.add_argument('--num', type=int, default=3, help='Number of sample documents to generate')
    parser.add_argument('--output', type=str, default=None, help='Output directory for sample documents')

    args = parser.parse_args()

    # Determine output directory
    if args.output:
        output_dir = args.output
    else:
        # Default to app/sample_docs relative to this script
        script_dir = Path(__file__).parent.absolute()
        output_dir = os.path.join(script_dir.parent, 'app', 'sample_docs')

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate sample documents
    try:
        logger.info(f"Generating {args.num} sample documents in {output_dir}")
        sample_paths = create_sample_documents(output_dir, args.num)

        logger.info("Sample documents generated successfully:")
        for path in sample_paths:
            logger.info(f"  - {path}")

        logger.info(f"\nTotal documents generated: {len(sample_paths)}")

    except Exception as e:
        logger.error(f"Error generating sample documents: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()