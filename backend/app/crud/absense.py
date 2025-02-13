from sqlalchemy.orm import Session

from app.models import Absense
from app.schemas.absense import AbsenseCreate, AbsenseResponse

def create(db: Session, absense_in: AbsenseCreate) -> AbsenseResponse:
    """Absense を新規作成して DB に登録する"""
    absense = Absense(
        user_id=absense_in.user_id,
        name=absense_in.name,
        start_time=absense_in.start_time,
        end_time=absense_in.end_time,
        default_start_time=absense_in.default_start_time,
        default_end_time=absense_in.default_end_time
    )
    db.add(absense)
    db.commit()
    db.refresh(absense)  # 挿入後に最新の状態を取得する
    return absense

def get_by_id(db: Session, absense_id: int) -> Absense:
    """指定した ID の Absense を取得する"""
    return db.query(Absense).filter(Absense.id == absense_id).first()

def get_by_name(db: Session, user_id:int , name: str) -> Absense:
    """指定した name の Absense を取得する"""
    return db.query(Absense).filter(Absense.user_id == user_id , Absense.name == name,).first()
