# HuggingFace Inference API – "askSri"

This project implements a FastAPI-based container-ready backend service that allows you to send inference requests to a pre-trained NLP model hosted on HuggingFace. It supports parallel requests and is ready to scale in production environments with tools like `uvicorn`, `gunicorn`, and `NGINX`.

---

## 🚀 Purpose

This API exposes a `/askSri/generate` endpoint to process text prompts and return generated responses using a transformer model. It demonstrates how to:
- Serve HuggingFace models in a clean API format
- Support multiple requests concurrently
- Containerize and deploy inference services efficiently

---

## 🤖 Model Used

**Model**: `google/flan-t5-base`

### ✅ Why this model?
- It's a **lightweight**, instruction-tuned variant of the T5 family.
- Handles summarization, translation, Q&A, and general text generation tasks.
- Fast to load and works well on CPU-only machines.
- Great choice for demonstration or proof-of-concept APIs without needing a GPU.

---

## 📂 Project Structure

LLM project/
├── app/
│ ├── api/
│ │ ├── init.py # Exposes the router
│ │ └── endpoints.py # FastAPI endpoint for inference
│ ├── init.py # Loads the model once at startup
│ ├── main.py # Initializes the FastAPI app
│ └── model_loader.py # Handles model loading and response generation
├── logs/
│ ├── app.log # Runtime logs
│ └── logging_config.py # Logging configuration
├── requirements.txt # All required dependencies
├── README.md # Project overview (this file)


---

## 🛠️ How to Run

### 🔹 1. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux
