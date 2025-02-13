from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import task as crud_task
from app.schemas import task as task_schema

from app import database

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.post("/", response_model=task_schema.TaskResponse)
def create_task(task_in: task_schema.TaskCreate, db: Session = Depends(database.get_db)):
    return crud_task.create(db=db, task_in=task_in)


@router.get("/{task_id}", response_model=task_schema.TaskResponse)
def read_task(task_id: int, db: Session = Depends(database.get_db)):
    db_task = crud_task.get_by_id(db, task_id=task_id)

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return db_task