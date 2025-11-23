#   Custom logger setup for the RAG Pipeline application.
import logging
def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Sets up a custom logger with the specified name and level."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if not logger.hasHandlers():
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    
    return logger
app_logger = setup_logger("RAG_Pipeline_Logger")
# Example usage:
app_logger.info("Logger initialized for RAG Pipeline")

