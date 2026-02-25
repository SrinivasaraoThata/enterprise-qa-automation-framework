import logging
import os

def get_logger(name=__name__):
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Print to terminal
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        
        # Format: [INFO] 2024-01-01 10:00:00 - message
        formatter = logging.Formatter(
            '[%(levelname)s] %(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger