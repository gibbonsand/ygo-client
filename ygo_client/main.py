import logging
import os

from onedrive_api.onedrive_api_client import OneDriveAPIClient
import ygo_client.constants as c
from ygo_client.templates.help_messages import HELP_MESSAGES
from ygo_client.download_onedrive_file import download_onedrive_file
from ygo_client.setup_utils import init_args, init_logger, ensure_folders
from excel_client.excel_client import ExcelClient


def main():
    # Initialize logger
    init_logger(log_level=c.LOG_LEVEL,
                log_to_stream=True,
                log_to_file=True,
                logfile_path=c.LOGFILE_PATH)

    # Create setup directories if needed
    ensure_folders(["OUTPUT_FOLDER", "LOG_FOLDER"])

    # Get input arguments
    args = init_args(c.ARG_NAMES)
    logging.debug(f"Arguments: {vars(args)}")

    for arg_name in c.ARG_NAMES:
        if getattr(args, arg_name):
            logging.info(f"Running entrypoint {arg_name}.")
            globals()[f"{arg_name}"]()
    
    if not any(getattr(args, arg_name) for arg_name in c.ARG_NAMES):
        logging.error(
            "No arguments specified. Use --help to see available options."
        )