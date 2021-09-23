from pathlib import Path
from typing import Generator, IO

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from starlette.background import BackgroundTasks
from uuid import uuid4

from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from api.db.video import VideoDB
from api.models.video import VideoModel
from api.schemas.video import VideoUpdateRequest, VideoUpdateResponse
from api.utils.utils_videos import writeVideo, ranged
from config import Config


class SingleVideoRepository:

    @staticmethod
    async def saveVideo(db: Session,
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

        # DB SAVER DO

        await VideoDB.createVideo(db=db, title=title, video_path=set_name, description=description,
                                  is_private=is_private)

        # return title, description, is_private

        return f"Video is saved {title} {is_private}"

    @staticmethod
    async def readVideo(id: str, request: Request, db: Session) -> tuple:
        id = int(id)
        from_db = await VideoDB.getVideoById(db=db, id=id)
        print(from_db.video_path)
        dir_file = f"{Config.getSavePath()}/{from_db.video_path}"
        path = Path(dir_file)
        file = path.open('rb')
        print(path.name)
        file_size = path.stat().st_size

        content_length = file_size
        status_code = 200
        headers = {}
        content_range = request.headers.get('range')

        if content_range is not None:
            content_range = content_range.strip().lower()
            content_ranges = content_range.split('=')[-1]
            range_start, range_end, *_ = map(str.strip, (content_ranges + '-').split('-'))
            range_start = max(0, int(range_start)) if range_start else 0
            range_end = min(file_size - 1, int(range_end)) if range_end else file_size - 1
            content_length = (range_end - range_start) + 1
            file = ranged(file, start=range_start, end=range_end + 1)
            status_code = 206
            headers['Content-Range'] = f'bytes {range_start}-{range_end}/{file_size}'

        return file, status_code, content_length, headers

    @staticmethod
    async def delete_video(db: Session, id: int):
        return await VideoDB.deleteVideoById(db=db, id=id)

    @staticmethod
    async def get_template(templates: Jinja2Templates, request: Request, id: int) -> HTMLResponse:
        return templates.TemplateResponse("index.html", {"request": request, "path": id})
