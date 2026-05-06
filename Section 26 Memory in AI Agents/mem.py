from mem0 import Memory
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

config={
    "version":"v1.1",
    "embedder":{
        "provider":"openai",
        "config":{
            "api_key": GEMINI_API_KEY,
            "model": "gemini-embedding-2"
        }
    },
    "llm": {
        "provider":"openai",
        "config":{
            "api_key": GEMINI_API_KEY,
            "model": "gemini-2.5-flash"
    },
    "vector_store":{
        "provider":"qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }
}


mem_client=Memory.from_config(config)