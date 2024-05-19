from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import auth
from app.services import salary as salary_db_services
from app.schemas import salary as salary_schemas

from app.db.db_connection import get_db as db_connection


router = APIRouter()


@router.get("/", response_model=salary_schemas.SalaryResponse)
def get_salary(token: str = Depends(auth.oauth2_scheme), db: Session = Depends(db_connection)):
    user = auth.get_current_user(token, db)
    return salary_db_services.get_salary_by(user)
