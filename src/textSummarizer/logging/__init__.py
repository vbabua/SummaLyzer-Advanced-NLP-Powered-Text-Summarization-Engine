# Import necessary libraries
import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger():
    
    # Define the format string for the logs as containing log level, module name, and the log message
    logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

    try:
        # Define a directory for the logs
        log_dir = Path("logs")
        
        # Create the log directory if it doesn't exist
        log_dir.mkdir(exist_ok=True)
        
        # Define the filepath where the logs will be stored
        log_filepath = log_dir / "running_logs.log"

        # Setup a rotating file handler which rotates logs after they reach a certain size
        # Create a new log file after the current one reaches 5MB, and will keep backups of the last 3 log files
        file_handler = RotatingFileHandler(log_filepath, maxBytes=5*1024*1024, backupCount=3)

        # Define the handlers for the logger
        handlers = [
            # Write logs to a file
            file_handler, 
            # Output logs to a console
            logging.StreamHandler(sys.stdout)]
        
        # Configure the basic settings for the logging module
        logging.basicConfig(level=logging.INFO, format=logging_str, handlers=handlers)

        # Create and return a logger with the name "textSummarizerLogger"
        logger = logging.getLogger("textSummarizerLogger")

        return logger

    except Exception as e:
        # If there's any error during logger setup, print the error
        print(f"Error setting up logger: {e}")
        
        # Return a default logger in case of setup errors
        return logging.getLogger()

# Call the setup_logger function to initialize the logger
logger = setup_logger()
