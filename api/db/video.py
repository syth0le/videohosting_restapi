class VideoDB:

    @staticmethod
    async def getVideoById(id):
        """select * from video as v where v.id=id"""
        return f'returned video {id}'

    @staticmethod
    async def getListVideos(skip: int = 0, limit: int = 10):
        """select * from video limit=limit skip=skip"""
        return f'returned videos {skip} {limit}'

    @staticmethod
    async def getStreamingVideo(request, id: int):
        response = f"Response {request}{id}"
        return response
