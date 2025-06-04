# *HuggingFace Inference API with Flan-T5-Large*

## *Project Overview*

This project demonstrates how to deploy a containerized API using *Flan-T5-Large, a pre-trained model from Hugging Face, to process natural language inference requests. The app is built using **FastAPI* for the API framework, *Gunicorn* and *Uvicorn* as the ASGI server, and *NGINX* as the reverse proxy to handle parallel requests efficiently. The entire system is containerized using *Docker* and orchestrated using *Docker Compose*.

### *Key Features*
- Loads and serves the *Flan-T5-Large* model for NLP tasks like summarization, question answering, etc.
- Supports *parallel requests* to handle multiple users simultaneously.
- Deployed in *Docker containers* for easy deployment and scalability.
- Uses *NGINX* for load balancing and reverse proxy functionality.
- Logs system activities for monitoring and debugging.

## *Why Flan-T5-Large?*

The *Flan-T5-Large* model is chosen for its *instruction-tuned capabilities* and *moderate size* (~770 million parameters). It provides a *great balance between performance and memory usage*, which is essential for deployment on a local machine with limited resources. It supports various NLP tasks like:
- *Question answering*
- *Text summarization*
- *Translation*
  
Given the hardware constraints of my system and the large model size of alternatives (like Falcon-RW-1B), *Flan-T5-Large* was selected to avoid memory and processing limitations while still demonstrating impressive performance.

## *Challenges and Solutions*
- *Large Model Limitations*: Initially tried using large models like Falcon-RW-1B, but the system could not produce any result due to high resource consumption.  
- *Cloud Deployment Issues: Explored cloud options like **AWS* and *RunPod.io, but encountered delays in **GPU quota approvals*. These options also required payments.
- *Solution: Settled on **Flan-T5-Large, which offered a **lighter* model with acceptable performance, allowing efficient inference within available resources.

## *Project Structure*
LLM project/
│
├── app/
│ ├── init.py # Initializes model loader singleton and app context
│ ├── model_loader.py # Loads and caches the HuggingFace model & tokenizer
│ ├── main.py # FastAPI app entrypoint, Gunicorn/Uvicorn setup, logging init
│ ├── askSri/ # API route folder (renamed from 'api' for clarity)
│ │ ├── init.py # API router setup
│ │ └── endpoints.py # Defines API endpoints like /askSri/generate
│
├── logs/ # Folder for logging configuration and log files
│ └── logging_config.py # Logging setup (formats, handlers, levels)
│
├── venv/ # Python virtual environment (ignored in Git)
│
├── nginx.conf # NGINX reverse proxy configuration file
├── Dockerfile # Multi-stage Dockerfile to build and run app container
├── docker-compose.yml # Docker Compose to orchestrate app + nginx containers
├── requirements.txt # Python dependencies list
├── README.md # Project documentation, overview, and instructions
└── .gitignore # To ignore files/folders like venv, pycache, logs, etc.


## *How It Works*

1. *Docker Containers*:
   - *App Container*: Contains the FastAPI app with the model and inference logic.
   - *NGINX Container*: Handles incoming HTTP requests, routes them to the app container, and manages load balancing.

2. *Model Loading*:
   - The *Flan-T5-Large* model is loaded once into memory when the app starts.
   - The model remains in memory, improving response time for subsequent requests.
   
3. *Concurrency*:
   - *Gunicorn* with *Uvicorn workers* runs the FastAPI app, allowing multiple workers to process parallel requests efficiently.
   - *NGINX* serves as a reverse proxy, handling incoming traffic and forwarding it to the app container on port 8000.

4. *Logging*:
   - A *logging system* is integrated to monitor activity and capture any errors or issues, providing visibility into the system’s health.

---

## *Getting Started*

### *Prerequisites*

- *Docker* installed on your machine.
- *Docker Compose* installed.
- *Python 3.7+* if you want to run the code locally outside of Docker.
- *Postman* (optional)

## *Docker Details*

### *Dockerfile*
- *Multi-stage build*:
  - The *first stage* installs Python dependencies.
  - The *second stage* copies the app code and runs it using *Gunicorn/Uvicorn workers* to serve the FastAPI app.

### *docker-compose.yml*
- *Defines two services*:
  - *app: The FastAPI application with **Gunicorn* and *Uvicorn workers* to handle concurrent requests efficiently.
  - *nginx: The reverse proxy that listens on port **80* and forwards requests to the app service.

---

## *Future Improvements*

- *GPU Support: Future versions could implement **GPU support* for faster inference, either locally or on cloud services (e.g., RunPod or AWS).
- *Auto-scaling: Implement **auto-scaling* using *Kubernetes* or *AWS ECS* to handle higher traffic loads automatically.
- *Security: Add **authentication, **rate limiting, and **SSL termination* for production-grade security and encryption.
- *Model Expansion*: Support additional HuggingFace models and endpoints for more diverse NLP tasks, offering flexible scaling to other use cases.

---

## *Conclusion*

This project showcases a *containerized FastAPI app* serving *Flan-T5-Large* via *Gunicorn + Uvicorn workers, with **NGINX* handling reverse proxy duties for scalability and efficient request handling. The setup is *production-ready* and can be easily scaled by adjusting *Docker* configurations or deploying in *cloud environments*.

---
