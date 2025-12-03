"""
Airtable Client module - Handles communication with Airtable API.
"""

import os


class AirtableClient:
    """Client for interacting with Airtable API."""

    def __init__(self, api_key: str = None, base_id: str = None):
        """
        Initialize the Airtable client.

        Args:
            api_key: Airtable API key. Defaults to AIRTABLE_API_KEY env variable.
            base_id: Airtable base ID. Defaults to AIRTABLE_BASE_ID env variable.
        """
        self.api_key = api_key or os.getenv("AIRTABLE_API_KEY")
        self.base_id = base_id or os.getenv("AIRTABLE_BASE_ID")

    def get_records(self, table_name: str) -> list:
        """
        Fetch records from a table.

        Args:
            table_name: Name of the Airtable table.

        Returns:
            List of records.
        """
        raise NotImplementedError("Airtable get_records not implemented yet")

    def create_record(self, table_name: str, data: dict) -> dict:
        """
        Create a new record in a table.

        Args:
            table_name: Name of the Airtable table.
            data: Record data to create.

        Returns:
            Created record.
        """
        raise NotImplementedError("Airtable create_record not implemented yet")

    def update_record(self, table_name: str, record_id: str, data: dict) -> dict:
        """
        Update an existing record.

        Args:
            table_name: Name of the Airtable table.
            record_id: ID of the record to update.
            data: Updated record data.

        Returns:
            Updated record.
        """
        raise NotImplementedError("Airtable update_record not implemented yet")
