from .base import Base
from pydantic import EmailStr

class UserBase(Base):
    email: EmailStr
    name: str
    is_active: bool = True

# 作成用.
class UserCreate(UserBase):
    password: str

# レスポンス用.
class UserResponse(UserBase):
    id: int