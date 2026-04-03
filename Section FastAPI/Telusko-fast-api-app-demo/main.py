from fastapi import FastAPI
#from library_name import class_name

app_fastapi=FastAPI()

@app_fastapi.get("/")
def greet():
    return ("Welcome to the Backend:8000")

greet()