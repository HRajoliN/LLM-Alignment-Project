import logging

def setup_logger():
    """
    Set up a logger for the project.
    """
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger()
