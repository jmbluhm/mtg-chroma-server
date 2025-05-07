# main.py
from chromadb.server.fastapi import run

if __name__ == "__main__":
    run(host="0.0.0.0", port=8000, path="/data")