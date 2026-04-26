from pathlib import Path
from openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from dotenv import dotenv_values

pdf_path=Path(__file__).parent/"test.pdf"

#1.Load file in the current python program
loader = PyPDFLoader(file_path=pdf_path)
docs=loader.load()

# print(docs[1])

#2.Split docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=30, chunk_overlap=7) #overlap: Take little part of previous chunk in the current chunk, it helps to understand the reap
chunks = text_splitter.split_documents(documents=docs)


#3.Create Vector Embeddings
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",google_api_key=dotenv_values(".env")["GEMINI_API_KEY"])

vector_store=QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="Learning_RAG"
)
print("Indexing of Document...... COMPLETE")