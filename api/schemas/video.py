import datetime
from typing import Optional
from pydantic import BaseModel


class VideoItem(BaseModel):
    # id: int
    title: str = Optional[str]
    description: str = Optional[str]
    is_private: bool = Optional[bool]


class VideoGetResponse(VideoItem):
    # create_at: datetime.datetime
    pass


class VideoPlayGetResponse(VideoItem):
    pass


class VideoUpdateResponse(VideoItem):
    pass


class VideoUpdateRequest(VideoItem):
    pass


class VideoEvent(BaseModel):
    event: str
    status_code: int
