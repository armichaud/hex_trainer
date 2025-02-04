# Dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y\
    # Remove package lists to minimize image size
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Ensures logs from server are printed to the stdout immediately
ENV PYTHONUNBUFFERED=1
