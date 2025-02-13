from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

class Absense(Base):
    __tablename__ = "absenses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(50), nullable=False)
    start_time = Column(Integer, nullable=False)
    end_time = Column(Integer, nullable=False)
    default_start_time = Column(Integer, nullable=False)
    default_end_time = Column(Integer, nullable=False)

    # Userとのリレーションシップ
    user = relationship("User", back_populates="absenses")

    def __repr__(self):
        return f"<Absense(id={self.id}, user_name='{self.user_name}', timerange='{self.timerange}')>"