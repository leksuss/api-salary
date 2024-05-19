from datetime import date

from pydantic import BaseModel


class SalaryResponse(BaseModel):
    id: int
    amount: int
    date_increase: date
