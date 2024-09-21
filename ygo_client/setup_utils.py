# setup_utils.py
""" Submodule for setting up utilities. required by ygo_client """

import argparse
import logging
import os
from pathlib import Path

import ygo_client.constants as c
from ygo_client.templates.help_messages import HELP_MESSAGES


def ensure_folders(folder_list: list):
    """
    Ensures that the directories specified in the environment variables exist.

    For each folder type in the folder_list, this function checks whether the corresponding
    environment variable is set. If the environment variable exists and points to a valid path, 
    the function ensures that the directory is created (if it doesn't already exist). If the 
    environment variable is not set, no action is taken for that folder type.

    Args:
        folder_list (list): A list of folder type names (strings). These correspond to environment 
                            variable names, where the values should represent the folder paths.
    
    Notes:
        - If the environment variable for a given folder type is not set, the function will not 
          create any folder for that entry and will skip to the next item in the list.
        - If the environment variable is set but points to a path that does not exist, this function
          will create the necessary directories, including any intermediate directories.

    Example:
        If 'folder_list' contains ['LOG_DIR', 'BACKUP_DIR'], and the environment variables 
        LOG_DIR and BACKUP_DIR point to valid paths, the function will ensure those directories 
        exist, creating them if necessary.
    """
    # Argument handling
    folder_list = [folder_list] if not isinstance(folder_list, list) else folder_list
    if not folder_list:
        logging.warning(
            "No folder list was provided to ensure_folders so it did nothing."
        )
        return

    for folder_type in folder_list:
        # Get the folder path from the environment variable corresponding to the folder type
        folder_path = os.environ.get(folder_type)

        # If the environment variable is set, create the folder path
        if folder_path:
            # Create the directory (and intermediate directories) if they don't exist
            Path(folder_path).mkdir(parents=True, exist_ok=True)
        else:
            logging.warning(
                "No environment variable found for %f, defaulting to Downloads \
                    directory.", folder_type
            )


def init_args(arg_names: list = c.ARG_NAMES):
    """
    Parse command-line arguments using argparse.

    This function creates an ArgumentParser object and defines the available
    command-line options. The `parse_args()` method is used to parse the input
    from the user.
    
    Returns:
        An object containing the parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="YGO collection client, database manager and utilities"
    )

    # Define each option with a long name that matches a key in HELP_MESSAGES
    for arg_name in arg_names:
        if arg_name not in c.VALUE_ARGS:
            # Use action="store_true" to indicate that this is a flag (on/off)
            parser.add_argument(f"--{arg_name}",
                                action="store_true",
                                help=HELP_MESSAGES[arg_name])
        else:
            # Value arguments take a value as defined in c.VALUE_ARGS
            parser.add_argument(f"--{arg_name}",
                                type=c.VALUE_ARGS[arg_name],
                                help=HELP_MESSAGES[arg_name])

    return parser.parse_args()


def init_logger(log_level: int = logging.INFO,
                log_to_stream: bool = True,
                log_to_file: bool = True,
                logfile_path: str = f"./{__name__}") -> None:
    """
    Initializes the logger with a StreamHandler and a FileHandler to print log
    messages to the console and to a logfile.
    Args:
        log_level (int): The level of the logger. Defaults to INFO.
        log_to_file (bool): Whether to log to file. Defaults to True.
        log_to_stream (bool): Whether to log to stream. Defaults to True.
    """
    # Create a logger object and set its level to INFO
    logger = logging.getLogger()
    logger.setLevel(log_level)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # File handler
    if log_to_file:
        file_handler = logging.FileHandler(logfile_path)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log_level)
        logger.addHandler(file_handler)

    # Stream handler
    if log_to_stream:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(log_level)
        logger.addHandler(stream_handler)
