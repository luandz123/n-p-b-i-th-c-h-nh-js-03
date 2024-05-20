from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Cấu hình CORS (cho phép tất cả các origin)
origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserLogin(BaseModel):
    username: str
    password: str

# Giả lập dữ liệu sinh viên
students = [
    {"id": 1, "name": "Nguyễn Văn A", "age": 20, "address": "...", "phone": "...", "email": "...", "class": "..."},
    # ... thêm dữ liệu
]

@app.post("/api/login")
def login(user_login: UserLogin):
    if user_login.username == "admin" and user_login.password == "admin":
        return {"success": True}
    else:
        raise HTTPException(status_code=401, detail="Tài khoản hoặc mật khẩu không chính xác")

@app.get("/api/students")
def get_students():
    return students
