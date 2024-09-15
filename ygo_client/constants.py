import logging
import os

from ygo_client.templates.help_messages import HELP_MESSAGES


# Logging config
LOG_FOLDER = os.getenv('LOG_FOLDER', f"{os.path.expanduser('~')}/Downloads/")
LOGFILE_PATH = LOG_FOLDER + f"{__name__}"
LOG_LEVEL = os.getenv('LOG_LEVEL', logging.INFO)

# argparse config
ARG_NAMES = HELP_MESSAGES.keys()

# File name and properties
FILE_NAME = os.getenv('FILE_NAME', 'Book 5.xlsx')
SHEET_NAME = os.getenv('SHEET_NAME', 'YGO')
HEADER = os.getenv('HEADER', True)

# Output folder config
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER', f"{os.path.expanduser('~')}/Downloads/")
OUTPUT_PATH = OUTPUT_FOLDER + FILE_NAME