import logging
import os

import ygo_client.constants as c
from onedrive_api.onedrive_api_client import OneDriveAPIClient




def download_onedrive_file(file_name: str = None,
                           output_path: str = None) -> None:
    """ Download file from OneDrive """
    
    # Handle default args
    if not file_name:
        file_name = c.FILE_NAME
    if not output_path:
        output_path = c.OUTPUT_PATH

    # Initialize and authenticate One Drive client
    logging.info("Calling OneDriveAPI client to handle file download")
    client = OneDriveAPIClient()
    client.authenticate()

    # Retrieve file ID
    file_id = client.lookup_file(file_name)
    
    # Download file
    logging.info(f"Downloading file {file_id}...")
    client.download_file(
        file_id,
        output_path)