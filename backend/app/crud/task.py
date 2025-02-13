from sqlalchemy.orm import Session

from app.models import Task
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate

def create(db:Session, task_in: TaskCreate) -> TaskResponse:
    """Task を新規作成して DB に登録する"""
    task = Task(
        user_id=task_in.user_id,
        title=task_in.title,
        default_status = task_in.default_status,
        current_status = task_in.current_status
    )
    db.add(task)
    db.commit()
    db.refresh(task)  # 挿入後に最新の状態を取得する
    return task

def get_by_id(db:Session, task_id:int) -> Task:
    """指定した ID の Task を取得する"""
    return db.query(Task).filter(Task.id == task_id).first()

def get_by_user_id(db:Session, user_id:int) -> Task:
    """指定した User ID の Task を取得する"""
    return db.query(Task).filter(Task.user_id == user_id).all()

def update(db:Session, task_id:int, new_title:str = None, new_current_status:bool = None) -> Task:
    """指定した ID の Task を更新する"""
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    if new_title is not None:
        task.title = new_title
    if new_current_status is not None:
        task.current_status = new_current_status
    db.commit()
    db.refresh(task)
    return task