from pydantic import BaseModel

from fastapi import FastAPI,Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware


from app.database import engine

from app.models import Base
from app.crud import user, task, absense

from app.routers import user as user_router
from app.routers import absense as absense_router
from app.routers import task as task_router


app = FastAPI(
    title="MentiaLink API",
    description="API for MentiaLink",
    version="0.1",
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",  "http://192.168.150.209:3000"],  # フロントエンドのオリジン
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(absense_router.router)
app.include_router(task_router.router)

@app.get("/")
def root():
    return {"message": "Hello World"}