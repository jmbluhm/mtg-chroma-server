# main.py
import uvicorn
from chromadb.server.fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)