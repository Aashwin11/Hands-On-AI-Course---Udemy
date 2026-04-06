from fastapi import FastAPI
#from library_name import class_name
from models import Product
app_fastapi=FastAPI()

@app_fastapi.get("/")
def greet():
    return ("Welcome to the Backend:8000")

greet()

products=[
          Product(id=1, name="phone",description="budget phone",price=99,quantity=10),
          Product(id=2, name="Laptop",description="Latop phone",price=1999,quantity=3),
          Product(id=3, name="Pen",description="Budget pen",price=1,quantity=30),
          Product(id=4, name="Table",description="Big Table",price=299,quantity=2),

]
@app_fastapi.get("/products")
def get_all_products():
    return products