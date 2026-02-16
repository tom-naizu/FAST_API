from fastapi import FastAPI,Request
from Data import products
from dtos import ProductDTO

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

##body, headers- request headers, query params

## Different types of HTTP Methods

@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)

    return{"Status":"Product Created Successfully...","Data":products}


@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO,product_id:int):

    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            
            return{"Status":"Product Update Successfuly...","products":product_data}

    return {
        "ERROR":"Product Not Found for this ID"
    }

@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
        
        for index,oneProduct in enumerate(products):
            if oneProduct.get("id") == product_id:
                deleted_product = products.pop(index)
                return{"Status":"Product Deleted Successfuly...","product":deleted_product}

        return {
        "ERROR":"Product Not Found for this ID"
    }

## How to do validate data. -DTOS

## How to call different HTTP Methods. -Any TOOL?
