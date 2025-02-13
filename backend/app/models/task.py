from .base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    current_status = Column(Boolean, nullable=False, default=False)
    default_status = Column(Boolean, nullable=False )

    user = relationship("User", back_populates="tasks")