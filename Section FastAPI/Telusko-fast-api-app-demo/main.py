from fastapi import FastAPI
#from library_name import class_name
from models import Product
from database import Session
import database
import database_models

app_fastapi=FastAPI()

database_models.Base.metadata.create_all(bind=database.engine)

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

def init_db():
    db=Session()
    count=db.query(database_models.Product).count
    if count==0:
        for product in products:
        
            db.add(database_models.Product(**product.model_dump()))    
        db.commit()
    
init_db()

#Get all products
@app_fastapi.get("/products")
def get_all_products():
    #DB_connection - talks to sqlalchemy. All these configs are done in seperate file
    db=Session()
    db.query()
    #write the query
    
    return products

#Get product by ID
@app_fastapi.get("/product/{id}")
def get_product_by_id(id:int):
    for _ in products:
        if _.id== id:
            return _
    return "Product not found"


#Add a record
@app_fastapi.post("/product")
def add_product(product:Product):
    products.append(product)
    return product

#Update
@app_fastapi.put("/product")
def update_product(id:int,product:Product):
    for _ in range(len(products)):
        if products[_].id== id:
            products[_]=product
            return f"product Added successfully {product}"
        
    return "No product found"


#Delete

@app_fastapi.delete("/product")
def delete_product(name: str):
    for product in products:
        if product.name == name:
            products.remove(product)
            return "Product deleted"

    return "Product not found"            




