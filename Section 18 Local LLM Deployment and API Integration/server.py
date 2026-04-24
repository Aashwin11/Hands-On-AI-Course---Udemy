from fastapi import FastAPI, Body
from ollama import Client


app=FastAPI()
client=Client(
         host="http://localhost:11434"    #ollama port
              )
@app.get("/")
def read_root():
    return "Hello World"

@app.post("/chat")
def chat(
    message:str=Body(...,
                     description="message"
                     )
):
    response=client.chat(model="stablelm-zephyr:latest",messages=[
        
        {"role":"user","content":message}
    ])
    
    return {"response":response.message.content}
    



