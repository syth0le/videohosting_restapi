from typing import Optional

from sqlalchemy.orm import Session

from api.models.video import VideoModel


class VideoDB:

    @staticmethod
    async def getVideoById(db: Session, id: int):
        return db.query(VideoModel).filter(VideoModel.id == id).first()

    @staticmethod
    async def createVideo(db: Session,
                          video_path: str,
                          title: Optional[str],
                          is_private: bool,
                          description: Optional[str]):
        video = VideoModel(
            video_path=video_path,
            title=title,
            is_private=is_private,
            description=description
        )
        db.add(video)
        db.commit()
        return f"video created: {video_path}"

    @staticmethod
    async def getListVideos(db: Session, skip: int = 0, limit: int = 10):
        """select * from video limit=limit skip=skip"""
        return db.query(VideoModel).all()

    @staticmethod
    async def getStreamingVideo(db: Session,
                                request, id: int):
        response = f"Response {request}{id}"
        return response

    @staticmethod
    async def deleteVideoById(db: Session,
                              id: int):
        video = db.query(VideoModel).filter(VideoModel.id == id).first()
        db.delete(video)
        db.commit()
        return f"Video {id} was deleted."

