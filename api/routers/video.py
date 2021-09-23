from fastapi import APIRouter, File, BackgroundTasks, Form, UploadFile
from starlette.responses import StreamingResponse

from api.handlers.single_video import saveVideo
from api.schemas.video import VideoGetResponse

router = APIRouter(prefix="/video",
                   tags=["video"])


@router.get("/")
async def getListVideos(limit: int = 100,
                        skip: int = 0):
    return skip, limit


@router.get("/{id}")
async def getVideo(id: int):
    return f"video with id: {id}"


@router.get("/description/{id}")
async def getVideoDescr(id: int):
    return f"video description with id : {id}"


@router.patch
async def patchVideoDescr(id: int):
    return f"video description with id : {id} is patched"


@router.post("/")
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


