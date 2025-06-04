# Stage 1: Builder
FROM python:3.13.3 as builder 

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --upgrade pip \
 && pip install --user -r requirements.txt 

# Stage 2: Runtime
FROM python:3.13.3

ENV PATH="/root/.local/bin:$PATH"
WORKDIR /app


COPY --from=builder /root/.local /root/.local
COPY . /app

CMD ["gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--workers", "4","--threads","2", "--bind", "0.0.0.0:8000","--timeout","120"]