from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import dotenv_values
from openai import OpenAI

#Embedding the QUERY
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",google_api_key=dotenv_values(".env")["GEMINI_API_KEY"])


#Connecting to the Vector Database
vector_db=QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="Learning_RAG"
)


#Take User Input
user_query=input("Ask Something? >")

#Relevant Chunks from Vector DB
search_result=vector_db.similarity_search(query=user_query)

Context="\n\n\n".join([f"Page Content:{search.page_content}\n Page Number:{search.metadata['page_label']}"for search in search_result])

SYSTEM_PROMPT="""
    You are a helpful AI assistant who answers query based on the available context retrieved from the PDF file along with page_contents and page Number.
    
You should only answer the user based on the following context and navigate the user to open the right page to know

Context:
{context}

"""
client=OpenAI(
    api_key=dotenv_values(".env")["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":user_query},
    ]
)

print(f"🤖:{response.choices[0].message.content}")

