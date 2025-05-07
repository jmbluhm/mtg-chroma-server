# main.py
import chromadb.server

if __name__ == "__main__":
    chromadb.server.run(host="0.0.0.0", port=8000, path="/data")