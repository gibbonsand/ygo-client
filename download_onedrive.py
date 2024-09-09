from onedrive_api.onedrive_api_client import OneDriveAPIClient


def download_file(filename: str = "Book 5.xlsx") -> None:
    # Download file from OneDrive
    client = OneDriveAPIClient()
    client.authenticate()

    filename = 'Book 5.xlsx'
    file_id = client.lookup_file(filename)
    
    # Download file
    client.download_file(
        file_id,
        f"/Users/andrewgibbons/Downloads/{filename}")