import argparse
import logging
import os

from onedrive_file_management.download_onedrive import download_file
from onedrive_file_management.read_excel import read_excel
import templates.help_messages as t


FILE_NAME = os.getenv('FILENAME', 'Book 5.xlsx')
SHEET_NAME = os.getenv('YGO', 'YGO')
HEADER = os.getenv('HEADER', True)
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER', '~/Downloads/')
OUTPUT_PATH = OUTPUT_FOLDER + FILE_NAME
LOGFILE_PATH = os.getenv('LOGFILE_PATH', '~/Downloads/')
LOG_LEVEL = os.getenv('LOG_LEVEL', logging.INFO)

ARG_NAMES = t.HELP_MESSAGES.keys()


def get_args():
    """
    Parse command-line arguments using argparse.

    This function creates an ArgumentParser object and defines the available
    command-line options. The `parse_args()` method is used to parse the input
    from the user.
    
    Returns:
        An object containing the parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="YGO collection client, database manager and utilities")

    # Define each option with a long name that matches a key in HELP_MESSAGES
    for arg_name in ARG_NAMES:
        # Use action="store_true" to indicate that this is a flag (on/off)
        parser.add_argument(f"--{arg_name}",
                            action="store_true",
                            help=t.HELP_MESSAGES[arg_name])
    
    return parser.parse_args()


def init_logger(log_to_file: bool = True, log_to_stream: bool = True) -> None:
    """
    Initializes the logger with a StreamHandler and a FileHandler to print log
    messages to the console and to a logfile.
    Args:
        log_to_file (bool): Whether to log to file. Defaults to True.
        log_to_stream (bool): Whether to log to stream. Defaults to True.
    """
    # Create a logger object and set its level to INFO
    logger = logging.getLogger()
    logger.setLevel(LOG_LEVEL)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # File handler
    if log_to_file:
        file_handler = logging.FileHandler(LOGFILE_PATH)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(LOG_LEVEL)
        logger.addHandler(file_handler)
    
    # Stream handler
    if log_to_stream:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(LOG_LEVEL)
        logger.addHandler(stream_handler)


#if __name__ == "__main__":
def main():
    init_logger(log_to_stream=True, log_to_file=True)

    # Get input arguments
    args = get_args()
    logging.debug(f"Arguments: {vars(args)}")

    for arg_name in ARG_NAMES:
        if getattr(args, arg_name):
            logging.info(f"Running entrypoint {arg_name}.")
            globals()[f"{arg_name}"]()
    
    if not any(getattr(args, arg_name) for arg_name in ARG_NAMES):
        logging.error(
            "No arguments specified. Use --help to see available options."
        )
        raise Exception(
            "No arguments specified. Use --help to see available options."
        )

    """     # Download database file
    logging.info("Downloading file from OneDrive...")
    download_file(file_name=FILENAME,
                  output_path=OUTPUT_PATH)

    logging.info("Reading in Excel file in pandas DataFrame...")
    # Read out and format df
    df = read_excel(file_name=OUTPUT_PATH,
                    sheet_name=SHEETNAME,
                    header=HEADER) """
    
    print(df)