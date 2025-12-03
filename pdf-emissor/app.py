"""
Flask application entry point for the PDF Emissor web service.
"""

import os
import sys

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from src.pdf_emissor import PDFEmissor
from src.airtable_client import AirtableClient
from src.supabase_client import SupabaseClient


def create_app():
    """Create and configure the application."""
    # Initialize clients
    airtable_client = AirtableClient()
    supabase_client = SupabaseClient()
    pdf_emissor = PDFEmissor()

    print("PDF Emissor application initialized")
    print("Airtable Client:", airtable_client)
    print("Supabase Client:", supabase_client)
    print("PDF Emissor:", pdf_emissor)

    return {
        "airtable": airtable_client,
        "supabase": supabase_client,
        "pdf_emissor": pdf_emissor
    }


if __name__ == "__main__":
    app = create_app()
    print("Application ready!")
