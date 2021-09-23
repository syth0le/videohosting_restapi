from fastapi import UploadFile, HTTPException
from starlette.background import BackgroundTasks
from uuid import uuid4

from api.db.video import VideoDB
from api.models.video import VideoModel
from api.schemas.video import VideoUpdateRequest
from api.utils.utils_videos import writeVideo


async def saveVideo(background: BackgroundTasks,
                    file: UploadFile,
                    title: str,
                    is_private: bool,
                    description: str):
    set_name = f"{title}_{uuid4()}.mp4"
    if file.content_type == 'video/mp4':
        # back_tasks.add_task(write_video, file_name, file)
        await writeVideo(set_name=set_name, file=file)
    else:
        raise HTTPException(status_code=400, detail="It isn't mp4")

    upload = VideoUpdateRequest(title=title, file=set_name, description=description, is_private=is_private)

    return await VideoModel.object.create(**upload.dict())
