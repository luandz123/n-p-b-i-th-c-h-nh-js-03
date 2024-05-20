from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

@app.get("/add/{a}/{b}") 
def add(a: int, b: int): # tao ham tong 2 so
    return {"result": a + b}

@app.get("/subtract/{a}/{b}")
def subtract(a: int, b: int):
    return {"result": a - b}

@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero"}
    return {"result": a / b}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả các nguồn gốc, bạn có thể chỉ định cụ thể
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả các phương thức HTTP
    allow_headers=["*"],  # Cho phép tất cả các headers
)
