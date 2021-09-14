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


