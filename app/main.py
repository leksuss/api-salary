import uvicorn
from fastapi import FastAPI

from app.api.users import router as users_router

fastapi_app = FastAPI()

fastapi_app.include_router(users_router, prefix="/users", tags=["users"])

if __name__ == '__main__':
    uvicorn.run(fastapi_app, host='127.0.0.1', port=8080)