from sqlalchemy.orm import Session

from app.db.models import User
from app.schemas.users import UserCreateSchema


def create_user(db: Session, user: UserCreateSchema):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
