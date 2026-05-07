from mem0 import Memory
import os
from dotenv import load_dotenv
import json
load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
from openai import OpenAI

config={
    "version":"v1.1",
    "embedder":{
        "provider":"gemini",
        "config":{
            "api_key": GEMINI_API_KEY,
            "model": "gemini-embedding-2"
        }
    },
    "llm": {
        "provider":"gemini",
        "config":{
            "api_key": GEMINI_API_KEY,
            "model": "gemini-3.1-flash-lite-preview"
    }
    },
    
    "vector_store":{
        "provider":"qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "collection_name":"mem0_gemini_test",
            "embedding_model_dims": 768
        }
    }
}

mem_client=Memory.from_config(config)

client=OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


while True:
    user_query=input(">")
    
    # Searchs for relevant memory  based on user_query
    #Search memory gives a DICT
    search_memory=mem_client.search(query=user_query, filters={
        "user_id": "Lisa"
    })
    
    #Convert to simpler data type //string
    memories=[
        f"ID:{mem.get("user_id")} \n Memory:{mem.get("memory")}" for mem in search_memory.get("results")
    ]
    
    SYSTEM_PROMPT= f"""
        Here is the context about the user:{json.dumps(memories)}
    """
    
    print (f"\n\n FOUND MEMORIES......\n\n{SYSTEM_PROMPT}\n")
    
    
    

    response=client.chat.completions.create(
        model="gemini-3.1-flash-lite-preview",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":user_query}
        ]
    )

    ai_response=response.choices[0].message.content
    print("\n\n Response:\n\n")
    print(ai_response)

    #Add conversation to the memory layer
    #Automatically extract facts, episodic and semantics
    #It needs to be scoped to a user id as well

    mem_client.add(
        user_id="Lisa",
        messages=[
            {"role":"user","content":user_query}, #What user said
            {"role":"assistant","content":ai_response} # What AI responded
        ]
    )
    print ("\n\n ........Added to Memory")