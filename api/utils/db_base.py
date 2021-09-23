import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Config

Base = declarative_base()
AUTH_DATABASE_URL = Config.getPostgresUrl()

database = databases.Database(AUTH_DATABASE_URL)
engine = sqlalchemy.create_engine(AUTH_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
