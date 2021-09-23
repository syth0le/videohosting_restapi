from fastapi import APIRouter, File, BackgroundTasks, Form, UploadFile, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import StreamingResponse, HTMLResponse
from starlette.templating import Jinja2Templates

from api.db.video import VideoDB
from api.handlers.single_video import SingleVideoRepository as svr
from api.handlers.list_of_videos import ListVideoRepository as lvr
from api.utils.db_base import get_db
from config import Config

router = APIRouter(prefix="/video",
                   tags=["video"])

templates = Jinja2Templates(directory=Config.getTemplatesPath())


@router.get("")
async def getListVideos(limit: int = 100,
                        skip: int = 0,
                        db: Session = Depends(get_db)):
    return await lvr.getListVideo(db=db, skip=skip, limit=limit)


@router.get("/play/{id}")
async def getPlayVideo(request: Request, id: int, db: Session = Depends(get_db)) -> StreamingResponse:
    file, status, content_length, headers = await svr.readVideo(db=db, request=request, id=id)

    response = StreamingResponse(file, media_type='video/mp4', status_code=status)

    response.headers.update({
        'Accept-Ranges': 'bytes',
        'Content-Length': str(content_length),
        **headers,
    })
    return response


@router.get("/{id}", response_class=HTMLResponse)
async def getVideoDescripton(request: Request, id: int):
    return await svr.get_template(templates=templates, request=request, id=id)


@router.post("")
async def postVideo(
        background: BackgroundTasks,
        file: UploadFile = File(...),
        title: str = Form(...),
        description: str = Form(...),
        is_private: bool = Form(...),
        db: Session = Depends(get_db)):
    return await svr.saveVideo(db=db,
                               background=background,
                               file=file,
                               title=title,
                               is_private=is_private,
                               description=description)


@router.delete("/{id}")
async def deleteVideoDescription(id: int, db: Session = Depends(get_db)):
    return await svr.delete_video(db=db, id=id)


# @router.patch("/{id}")
# async def patchVideoDescription(id: int, db: Session = Depends(get_db)):
#     return VideoDB.getVideoById(db=db, id=id)


# @router.get("/private/{id}")
# async def getPrivateVideo(id: int):
#     return id
#
#
# @router.patch("/private/{id}")
# async def setPrivateVideo(id: int):
#     return id
