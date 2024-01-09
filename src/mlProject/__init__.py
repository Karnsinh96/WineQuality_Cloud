import os
import sys
import logging

# Log format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory for log files
log_dir = "logs"

# Create the full file path for the log file
log_filepath = os.path.join(log_dir, "running_log.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),      # Log to a file
        logging.StreamHandler(sys.stdout)      # Log to the console
    ]
)

# Create a logger instance with the name "mlProjectLogger"
logger = logging.getLogger("mlProjectLogger")
