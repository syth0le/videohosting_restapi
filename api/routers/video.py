from fastapi import APIRouter, File, BackgroundTasks, Form, UploadFile
from starlette.requests import Request
from starlette.responses import StreamingResponse, HTMLResponse
from starlette.templating import Jinja2Templates

from api.handlers.single_video import saveVideo, readVideo
from config import Config

router = APIRouter(prefix="/video",
                   tags=["video"])

templates = Jinja2Templates(directory=Config.getTemplatesPath())


@router.get("")
async def getListVideos(limit: int = 100,
                        skip: int = 0):
    return skip, limit


@router.get("/play/{title}")
async def getPlayVideo(request: Request, title: str) -> StreamingResponse:
    file, status, content_length, headers = await readVideo(request=request, title=title)

    response = StreamingResponse(file, media_type='video/mp4', status_code=status)

    response.headers.update({
        'Accept-Ranges': 'bytes',
        'Content-Length': str(content_length),
        **headers,
    })
    return response


# @router.get("/play/{title}")
# async def getPlayVideo(title: str):
#     file = open("files/TEST_9a1c26e4-c3b8-44f2-b460-d399ae264172.mp4", 'rb')
#     print(file.readline())
#     return StreamingResponse(file, media_type="video/mp4")


@router.get("/{title}", response_class=HTMLResponse)
async def getVideoDescripton(request: Request, title: str):
    return templates.TemplateResponse("index.html", {"request": request, "path": title})


@router.patch("/{id}")
async def patchVideoDescr(id: int):
    return f"video description with id : {id} is patched"


@router.post("")
async def postVideo(
        background: BackgroundTasks,
        file: UploadFile = File(...),
        title: str = Form(...),
        description: str = Form(...),
        is_private: bool = Form(...)):

    return await saveVideo(background=background,
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


