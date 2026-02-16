from fastapi import FastAPI,Request
from MockData import products

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to the FastAPI Server"

@app.get("/products")
def get_products():
    return products

@app.get("/contact")
def contact():
    return "You can connect us any time..."

# Path Params...
@app.get("/product/{product_id}")
def get_one_products(product_id:int):

#If product if id in products then return Product..Else show Error prodtc not exist
    
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct
        
    return {
        "ERROR":"Product Not Found for this ID"
    }

#Query Params...
# @app.get("/greet")
# def greet_user(name:str , age:int):
#     return {
#         "Greet":f"Hello... {name} you are {age} years old...?"
    # }

@app.get("/greet")
def greet_user(request:Request):
    query_params = dict((request.query_params))
    print(query_params)

    return {
        "Greet":f"Hello {query_params.get("name")}... you are {query_params.get("age")} years old...?"
    }




