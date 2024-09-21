""" Main entrypoint for the ygo_client tool. """

import logging

import ygo_client.constants as c
from ygo_client.setup_utils import init_args, init_logger, ensure_folders

# Import possible entrypoint functions
from ygo_client.download_onedrive_file import download_onedrive_file
from ygo_client.query_excel_file import query_excel_file

def main():
    """ Main entrypoint for ygo_client """
    # Initialize logger
    init_logger(log_level=c.LOG_LEVEL,
                log_to_stream=True,
                log_to_file=True,
                logfile_path=c.LOGFILE_PATH)

    # Create setup directories if needed
    ensure_folders(["OUTPUT_FOLDER", "LOG_FOLDER"])

    # Get input arguments
    args = init_args(c.ARG_NAMES)
    logging.debug("Arguments: %s", vars(args))

    for arg_name in c.ARG_NAMES:
        arg_value = getattr(args, arg_name)

        # Case for boolean arguments (store_true)
        if arg_value is True:
            logging.info("Running entrypoint %s.", arg_name)
            globals()[f"{arg_name}"]()

        # Case for non-boolean arguments (that take an argument)
        elif arg_value and arg_value is not None:
            logging.info("Running entrypoint %s with value %s.", arg_name, arg_value)
            globals()[f"{arg_name}"](arg_value)

    if not any(getattr(args, arg_name) for arg_name in c.ARG_NAMES):
        logging.error(
            "No arguments specified. Use --help to see available options."
        )
