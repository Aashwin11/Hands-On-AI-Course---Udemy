from openai import OpenAI
from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")
client=OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


#Embedding the QUERY
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",google_api_key=gemini_api_key)
print("📞Embedding model confirmed...\n")


#Connecting to the Vector Database
print("📞Connecting to the Vector Database...\n")
vector_db=QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="Learning_RAG"
)


def process_query(user_query:str):  #We will receive query here, process here and retrieve it
    print("🔎Searching Chunks...\n")
    search_result=vector_db.similarity_search(query=user_query)
    Context="\n\n\n".join([f"Page Content:{search.page_content}\n Page Number:{search.metadata['page_label']}"for search in search_result])
    
    SYSTEM_PROMPT="""
    You are a helpful AI assistant who answers query based on the available context retrieved from the PDF file along with page_contents and page Number.
    
You should only answer the user based on the following context and navigate the user to open the right page to know

Context:
{Context}

"""
    response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":user_query},
    ]
)
    print("QEURYING COMPLETE")
    return(f"🤖:{response.choices[0].message.content}")
