import datetime
from typing import Optional


class VideoItem:
    title: str = Optional[str]
    description: str = Optional[str]
    is_private: bool = Optional[bool]


class VideoGetResponse(VideoItem):
    create_at: datetime.datetime


class VideoPlayGetResponse(VideoItem):
    pass


class VideoUpdateResponse(VideoItem):
    pass


class VideoUpdateRequest(VideoItem):
    pass


class VideoEvent:
    event: str
    status_code: int
