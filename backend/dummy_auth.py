from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",  "http://192.168.150.209:3000"],  # フロントエンドのオリジン
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    password: str = "bearer"

@app.post("/login", response_model=Token)
def login(user: User):
    dummy_token = "dummy_token"
    return Token(access_token=dummy_token)

