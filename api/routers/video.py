from fastapi import APIRouter

router = APIRouter(prefix="/video",
                   tags=["video"])


@router.get("/")
async def getListVideos(limit: int = 100,
                        skip: int = 0):
    return skip, limit


@router.get("/{id}")
async def getVideo(id: int):
    return f"video with id: {id}"


@router.get("/{id}")
async def getVideoDescr(id: int):
    return f"video description with id : {id}"


@router.patch
async def patchVideoDescr(id: int):
    return f"video description with id : {id} is patched"


@router.post("/")
async def postVideo():
    return "Video posted"


# @router.get("/private/{id}")
# async def getPrivateVideo(id: int):
#     return id
#
#
# @router.patch("/private/{id}")
# async def setPrivateVideo(id: int):
#     return id


