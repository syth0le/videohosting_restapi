import databases
import sqlalchemy as sqlalchemy
from fastapi import FastAPI

from api.routers.video import router

app = FastAPI()

AUTH_DATABASE_URL = f"postgresql://alterstrada:alterstrada@localhost:5432/alterstrada"

metadata = sqlalchemy.MetaData()
database = databases.Database(AUTH_DATABASE_URL)
engine = sqlalchemy.create_engine(AUTH_DATABASE_URL)

metadata.create_all(engine)
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

# class MainMata(ormar.ModelMeta):
#     metadata = metadata
#     database = database


app.include_router(router)
