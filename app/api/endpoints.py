import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app import loader  # this is the ModelLoader instance from app/__init__.py

# Setup logger for this module
logger = logging.getLogger(__name__)

# Create a FastAPI router
router = APIRouter()

# Define the request schema
class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 100  # Optional, defaults to 100

# Define the /generate endpoint
@router.post("/generate")
def generate_text(request: PromptRequest):
    logger.info(f"Received request with prompt: {request.prompt}")

    try:
        result = loader.generate_response(
            prompt=request.prompt,
            max_length=request.max_length
        )
        logger.info("Successfully generated response.")
        return {"response": result}

    except Exception as e:
        logger.exception("Failed to generate response.")
        raise HTTPException(status_code=500, detail=str(e))