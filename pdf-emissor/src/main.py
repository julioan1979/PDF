"""
Main module - Entry point for the PDF Emissor application.
"""

from pdf_emissor import PDFEmissor
from airtable_client import AirtableClient
from supabase_client import SupabaseClient


def main():
    """Main function to run the PDF Emissor application."""
    print("PDF Emissor - Emissão de recibos Escuteiros")

    # Initialize clients
    airtable = AirtableClient()
    supabase = SupabaseClient()
    pdf_emissor = PDFEmissor()

    print("Clients initialized successfully")
    print("Application ready to generate receipts")


if __name__ == "__main__":
    main()
