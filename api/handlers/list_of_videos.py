from sqlalchemy.orm import Session

from api.db.video import VideoDB


class ListVideoRepository:

    @staticmethod
    async def getListVideo(db: Session, skip: int, limit: int):
        return await VideoDB.getListVideos(db=db, skip=skip, limit=limit)
