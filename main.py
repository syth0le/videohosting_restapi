import databases
import sqlalchemy as sqlalchemy
from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from api.utils.db_base import Base, database
from api.routers.video import router as video_router
from config import Config

app = FastAPI()

app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(video_router)

