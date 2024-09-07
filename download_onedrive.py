import json
import requests

from onedrive_api.onedrive_api import OneDriveAPI
import onedrive_api.constants as c


if __name__ == '__main__':
    
    # DOwnload file from OneDrive
    client = OneDriveAPI()
    client.authenticate()

    filename = 'Book 5.xlsx'
    file_id = client.lookup_file(filename)
    response = client.download_file(
        file_id,
        f"/Users/andrewgibbons/Downloads/{filename}")