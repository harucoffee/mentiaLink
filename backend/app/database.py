# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base 

# ※実際のユーザー名、パスワード、ホスト名、ポート番号、データベース名に置き換えてください
DATABASE_URL = "postgresql://harutosaito@localhost:5432/mentialink"

# エンジンの作成
engine = create_engine(DATABASE_URL)

# セッションの設定（必要に応じて）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_db():
    """
    この関数を実行すると、Base に定義されたすべてのモデルのテーブルが
    PostgreSQL データベース上に作成されます。
    """
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
