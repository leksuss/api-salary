from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, ExpiredSignatureError, jwt
from passlib.context import CryptContext

from app.config import settings
from app.db.models import User
from app.services import users as user_db_services
from app.db.db_connection import get_db as db_connection


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def generate_token(user: User) -> dict:
    payload = {
        'sub': str(user.id),
        'exp': datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRES_MINUTES),
    }
    access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return {'access_token': access_token, 'token_type': 'bearer'}





def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(db_connection)):
    def get_credentials_exception(message: str) -> HTTPException:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=message,
            headers={'WWW-Authenticate': 'Bearer'},
        )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id: int = payload.get('sub')
        if user_id is None:
            raise get_credentials_exception('Could not validate credentials')
    except ExpiredSignatureError:
        raise get_credentials_exception('Token has expired')
    except JWTError:
        raise get_credentials_exception('Could not validate credentials')
    user = user_db_services.get_user_by_id(db, user_id)
    if user is None:
        raise get_credentials_exception('User not found')
    return user
