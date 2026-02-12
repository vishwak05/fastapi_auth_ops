from fastapi import FastAPI
from contextlib import asynccontextmanager

from auth.database import create_db_and_tables
from auth.auth_routes import router as auth_router
from routes.user import router as users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI authentication and authorization example"}