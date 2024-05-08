import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine

from config import settings

app = FastAPI()
db = create_engine(settings.DATABASE_URL)

@app.on_event("startup")
def startup_database():
    return db.connect()

@app.on_event("shutdown")
def shutdown_database():
    return db.dispose()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)