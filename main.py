from chromadb.config import Settings
from chromadb.server import Server

if __name__ == "__main__":
    server = Server(Settings(
        chroma_api_impl="chromadb.api.fastapi.FastAPI",
        chroma_server_host="0.0.0.0",
        chroma_server_http_port=8000,
        persist_directory="/data"
    ))
    server.run()