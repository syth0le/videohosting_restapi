from api.db.video import VideoDB as db


class Video:

    def __init__(self, id: str, skip: int = 0):
        self.id = id
        self.skip = skip

    async def getVideo(self):
        _video = db.getVideoById(self.id)
        return "video"

    async def getPointOfVideo(self, next):
        self.skip = next
        _points = db.getStreamingVideo(self.id)
        return "point"