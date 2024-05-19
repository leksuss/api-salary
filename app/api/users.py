from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import auth
from app.services import users as user_db_services
from app.schemas import users as user_schemas
from app.db.db_connection import get_db as db_connection
from app.db.models import User


router = APIRouter()

@router.post('/signup', response_model=user_schemas.UserSchema)
def create_user(payload: user_schemas.UserCreateSchema = Body(), db: Session = Depends(db_connection)):
    payload.password = auth.get_password_hash(payload.password)
    return user_db_services.create_user(db, user=payload)


@router.post('/login', response_model=user_schemas.UserResponse)
def login(payload: user_schemas.UserLoginSchema = Body(), db: Session = Depends(db_connection)):
    try:
        user: User = user_db_services.get_user_by_email(
            db=db, user_email=payload.email
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid user credentials'
        )

    if not auth.verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid user credentials'
        )

    return auth.generate_token(user)
