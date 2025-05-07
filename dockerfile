FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a volume mount point
VOLUME /data

# Start ChromaDB server with persistent path
CMD ["chromadb", "run", "--host", "0.0.0.0", "--port", "8000", "--path", "/data"]