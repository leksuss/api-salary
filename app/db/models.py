from datetime import datetime, timedelta, timezone
import bcrypt
import jwt
from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

from app.config import settings


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, nullable=False, autoincrement=True, index=True)
    full_name: Mapped[String] = mapped_column(String(200), nullable=False)
    email: Mapped[String] = mapped_column(String(200), unique=True, nullable=False)
    password: Mapped[String] = mapped_column(String(200), nullable=False)


    def __repr__(self):
        return f'User(id={self.id}, email={self.email})'
