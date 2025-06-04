from fastapi import FastAPI
from app.api import inference_router
from logs.logging_config import configure_logging
import logging

# -------- Logging Configuration --------
configure_logging()
logger = logging.getLogger(__name__)
logger.info("Starting FastAPI application...")

# -------- FastAPI App Initialization --------
app = FastAPI(
    title="HuggingFace Inference API",
    description="An API that uses google/flan-t5-base to process prompts.",
    version="1.0.0"
)

# -------- Register Inference Router --------
app.include_router(inference_router, prefix="/askSri")

# -------- Health Check Endpoint --------
@app.get("/")
def read_root():
    logger.info("Health check endpoint hit.")
    return {"message": "Inference API is running."}
