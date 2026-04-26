from fastapi import FastAPI, Query
from client.rq_client import queue
from queues.worker import process_query

app=FastAPI()


@app.get("/")
def root():
    return 200

@app.post("/chat")
def chat(
    query:str=Query(..., description="chat query of user")
):
    job=queue.enqueue(process_query,query) #returns ID of the job 
    
    return {"status":"queued","job_id":job.id}