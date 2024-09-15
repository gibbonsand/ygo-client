from onedrive_api.onedrive_api_client import OneDriveAPIClient


def download_onedrive_file(file_name: str, output_path: str = None) -> None:
    """ Download file from OneDrive """
    
    # Handle default output path
    if not output_path:
        output_path = f"/Users/andrewgibbons/Downloads/{file_name}"
        logging.info(f"No output path provided - using default: {output_path}")

    # Initialize and authenticate One Drive client
    client = OneDriveAPIClient()
    client.authenticate()

    # Retrieve file ID
    file_id = client.lookup_file(file_name)
    
    # Download file
    client.download_file(
        file_id,
        output_path)