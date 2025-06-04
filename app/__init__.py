# app/__init__.py

import logging
from .model_loader import ModelLoader

# Get module-level logger
logger = logging.getLogger(__name__)

logger.info("Initializing the HuggingFace model...")

try:
    loader = ModelLoader()
    logger.info("Model loaded and ready for inference.")
except Exception as e:
    logger.exception("Model initialization failed.")
    raise