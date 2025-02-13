from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import absense as crud_absense
from app.schemas import absense as absense_schema

from app import database

router = APIRouter(
    prefix="/absenses",
    tags=["absenses"],
)

@router.post("/", response_model=absense_schema.AbsenseResponse)
def create_absense(absense_in: absense_schema.AbsenseCreate, db: Session = Depends(database.get_db)):
    db_absense = crud_absense.get_by_name(db, user_id=absense_in.user_id, name=absense_in.name)

    if db_absense:
        raise HTTPException(status_code=400, detail="Absense already registered")
    
    return crud_absense.create(db=db, absense_in=absense_in)

@router.get("/{absense_id}", response_model=absense_schema.AbsenseResponse)
def read_absense(absense_id: int, db: Session = Depends(database.get_db)):
    db_absense = crud_absense.get_by_id(db, absense_id=absense_id)

    if not db_absense:
        raise HTTPException(status_code=404, detail="Absense not found")

    return db_absense