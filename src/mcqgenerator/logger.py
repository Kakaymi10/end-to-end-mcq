import logging
import os
from datetime import datetime

# Ensure the logs directory exists
log_directory = os.path.join(os.getcwd(), "logs", "logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Define the log file path
log_file = os.path.join(log_directory, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    filemode='a',
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
