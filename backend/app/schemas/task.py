from .base import Base

from pydantic import BaseModel

class TaskBase(Base):
    user_id: int

class TaskCreate(TaskBase):
    title: str
    default_status: bool
    current_status: bool = False

class TaskResponse(TaskBase):
    id: int
    title: str
    current_status: bool

class TaskUpdate(TaskBase):
    id: int
    current_status: bool