from dotenv import load_dotenv
import os
from mem0 import Memory
from openai import OpenAI
from dotenv import load_dotenv
import json

import logging
logging.basicConfig(level=logging.DEBUG)
load_dotenv()


GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
NEO4J_URI=os.getenv("NEO4J_URI")
NEO4J_PASS=os.getenv("NEO4J_PASS")

config = {
    "version": "v1.1",
    "history_db_path": "./history.db",
    
    "embedder": {
    "provider": "gemini",
    "config": {
        "api_key": GEMINI_API_KEY,
        "model": "text-embedding-004"
    }
},
   
    "llm": {
        "provider": "openai",
        "config": {
            "api_key": GEMINI_API_KEY,
            "model": "gemini-2.5-flash",
            "openai_base_url": "https://generativelanguage.googleapis.com/v1beta/openai/"
        }
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": "neo4j+s://99ea59e6.databases.neo4j.io",
            "username": "neo4j",
            "password": "407x7bcx5WuynoQ5yATYh4u8FOe4CfAQh6SB7-BghoU"
        }
    },
    "vector_store": {
    "provider": "qdrant",
    "config": {
        "host": "localhost",
        "port": 6333,
        "collection_name": "mem0_gemini_test_v3",
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
    f"ID:{mem.get('user_id')} \n Memory:{mem.get('memory')}"
    for mem in search_memory.get("results")
    ]
    
    SYSTEM_PROMPT= f"""
        Here is the context about the user:{json.dumps(memories)}
    """
    
    print (f"\n\n FOUND MEMORIES......\n\n{SYSTEM_PROMPT}\n")
    
    
    

    response=client.chat.completions.create(
        model="gemini-2.5-flash",
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