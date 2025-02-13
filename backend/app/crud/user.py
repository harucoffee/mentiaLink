from sqlalchemy.orm import Session

from app.models import User
from app.schemas.user import UserCreate, UserResponse

def create(db: Session, user_in: UserCreate) -> UserResponse:
    """User を新規作成して DB に登録する"""
    user = User(name=user_in.name, email=user_in.email, hashed_password=user_in.password)
    db.add(user)
    db.commit()
    db.refresh(user)  # 挿入後に最新の状態を取得する
    return user

def get_by_id(db: Session, user_id: int) -> User:
    """指定した ID の User を取得する"""
    return db.query(User).filter(User.id == user_id).first()

def get_by_email(db: Session, email: str) -> User:
    """指定した email の User を取得する"""
    return db.query(User).filter(User.email == email).first()

def update(db: Session, user_id: int, new_name: str = None, new_group_id: int = None) -> User:
    """指定した ID の User を更新する"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    if new_name is not None:
        user.name = new_name
    if new_group_id is not None:
        user.group_id = new_group_id
    db.commit()
    db.refresh(user)
    return user

def delete(db: Session, user_id: int) -> bool:
    """指定した ID の User を削除する"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True
