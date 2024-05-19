import uvicorn
from fastapi import FastAPI

from app.api.users import router as users_router
from app.api.salary import router as salary_router


fastapi_app = FastAPI()

fastapi_app.include_router(users_router, prefix="/users", tags=["users"])
fastapi_app.include_router(salary_router, prefix="/salary", tags=["salary"])

if __name__ == '__main__':
    uvicorn.run(fastapi_app, host='127.0.0.1', port=8080)
