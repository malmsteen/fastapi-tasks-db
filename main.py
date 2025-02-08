from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, Annotated

from contextlib import asynccontextmanager

from database import create_tables, drop_tables
from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)

tasks = []
