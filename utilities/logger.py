import logging
import os


def get_logger():

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("IMDbFramework")

    if not logger.hasHandlers():

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler("logs/test.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger