import logging
import os

def configure_logging():
    # Create the logs folder if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("logs/log", mode="a", encoding="utf-8")
        ]
    )
    logger = logging.getLogger(__name__)
    logger.info("Logging is configured.")