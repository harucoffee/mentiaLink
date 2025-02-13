from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import user as crud_user
from app.schemas import user as user_schema

from app import database

import hashlib


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", response_model=user_schema.UserResponse)
def create_user(user_in: user_schema.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud_user.get_by_email(db, email=user_in.email)

    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    
    user_in.password = hashlib.sha256(user_in.password.encode()).hexdigest()

    return crud_user.create(db=db, user_in=user_in)

@router.get("/{user_id}", response_model=user_schema.UserResponse)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud_user.get_by_id(db, user_id=user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user
