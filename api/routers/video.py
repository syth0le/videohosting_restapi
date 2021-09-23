from typing import List

from fastapi import APIRouter, File, BackgroundTasks, Form, UploadFile, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import StreamingResponse, HTMLResponse
from starlette.templating import Jinja2Templates

from api.db.video import VideoDB
from api.handlers.single_video import saveVideo, readVideo
from api.schemas.video import VideoGetResponse
from api.utils.db_base import get_db
from config import Config

router = APIRouter(prefix="/video",
                   tags=["video"])

templates = Jinja2Templates(directory=Config.getTemplatesPath())


@router.get("", response_model=List[VideoGetResponse])
async def getListVideos(limit: int = 100,
                        skip: int = 0,
                        db: Session = Depends(get_db)):
    return await VideoDB.getListVideos(db=db, skip=skip, limit=limit)


@router.get("/play/{id}")
async def getPlayVideo(request: Request, id: int, db: Session = Depends(get_db)) -> StreamingResponse:
    file, status, content_length, headers = await readVideo(db=db, request=request, id=id)

    response = StreamingResponse(file, media_type='video/mp4', status_code=status)

    response.headers.update({
        'Accept-Ranges': 'bytes',
        'Content-Length': str(content_length),
        **headers,
    })
    return response


@router.get("/{id}", response_class=HTMLResponse)
async def getVideoDescripton(request: Request, id: int):
    return templates.TemplateResponse("index.html", {"request": request, "path": id})


@router.patch("/{id}")
async def patchVideoDescription(id: int, db: Session = Depends(get_db)):
    return VideoDB.getVideoById(db=db, id=id)


@router.post("")
async def postVideo(
        background: BackgroundTasks,
        file: UploadFile = File(...),
        title: str = Form(...),
        description: str = Form(...),
        is_private: bool = Form(...),
        db: Session = Depends(get_db)):

    return await saveVideo(db=db,
                           background=background,
                           file=file,
                           title=title,
                           is_private=is_private,
                           description=description)



# @router.get("/private/{id}")
# async def getPrivateVideo(id: int):
#     return id
#
#
# @router.patch("/private/{id}")
# async def setPrivateVideo(id: int):
#     return id


