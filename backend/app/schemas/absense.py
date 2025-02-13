from .base import Base

from pydantic import BaseModel

class AbsenseBase(Base):
    user_id: int
    default_start_time : int
    default_end_time : int

class AbsenseCreate(AbsenseBase):
    name: str
    start_time: int
    end_time: int

class AbsenseResponse(AbsenseBase):
    id: int
    name: str
    start_time: int
    end_time: int

class AbsenseUpdate(AbsenseBase):
    id: int
    name: str