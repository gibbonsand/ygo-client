import logging

from download_onedrive import download_file
from read_excel import read_excel
from database import create_db, query_db

FILENAME = "Book 5.xlsx"
OUTPUTPATH = "/Users/andrewgibbons/Downloads/" + FILENAME
SHEETNAME = "YGO"
HEADER = True


def init_logger():
    """
    Initializes the logger with a StreamHandler to print log messages to the console.
    Args:
        None
    Returns:
        A configured logger object.
    """
    # Create a logger object and set its level to INFO
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Create a StreamHandler to write logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter for the console handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)


if __name__ == "__main__":
    init_logger()

    # Download database file
    logging.info("Downloading file from OneDrive...")
    download_file(file_name=FILENAME,
                  output_path=OUTPUTPATH)

    logging.info("Reading in Excel file in pandas DataFrame...")
    # Read out and format df
    df = read_excel(file_name=OUTPUTPATH,
                    sheet_name=SHEETNAME,
                    header=HEADER)
    
    """ create_db(df)
    query_db() """