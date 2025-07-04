import logging
from logging.handlers import RotatingFileHandler
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("AUTO_UPDATER")

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Add file handler with rotation
file_handler = RotatingFileHandler(
    'logs/log.txt',
    maxBytes=2*1024*1024,  # 2MB
    backupCount=1
)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
LOGGER.addHandler(file_handler)

LOGGER.info("Live log streaming to telegram.") 