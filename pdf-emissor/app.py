"""
Application entry point for the PDF Emissor service.
"""

import os
import sys

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from pdf_emissor import PDFEmissor
from airtable_client import AirtableClient
from supabase_client import SupabaseClient


def initialize_clients():
    """Initialize and return all service clients."""
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
    clients = initialize_clients()
    print("Application ready!")
