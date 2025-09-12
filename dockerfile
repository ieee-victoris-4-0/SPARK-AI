# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies required for OpenCV and others
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Copy project files to container
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Install tini (process manager)
RUN curl -Lo /usr/bin/tini https://github.com/krallin/tini/releases/download/v0.19.0/tini && \
    chmod +x /usr/bin/tini

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Use tini as entrypoint
ENTRYPOINT ["/usr/bin/tini", "--"]

# Run FastAPI and Streamlit together
CMD ["bash", "-c", "uvicorn Api.Deploy_fastapi:app --host 0.0.0.0 --port 8000 & streamlit run main.py --server.port=8501 --server.address=0.0.0.0"]
