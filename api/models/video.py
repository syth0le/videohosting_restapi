import datetime

from sqlalchemy import Column, Integer, String, TEXT, Boolean, DATETIME


class VideoModel:
    __table_name__ = 'videos'

    id: int = Column(Integer, primary_key=True)
    video_path: str = Column(String(1000), unique=True)
    title: str = Column(String(100), default="No Name")
    description: str = Column(TEXT, default="No Description")
    create_at: datetime.datetime = Column(DATETIME, default=datetime.datetime.now)
    is_private: bool = Column(Boolean, default=False)

    def __repr__(self):
        return f"<VideoModel>: {self.id}-{self.title}"
