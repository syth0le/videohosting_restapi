from fastapi import UploadFile

from config import Config


async def writeVideo(set_name: str, file: UploadFile):
    file_path = Config.getSavePath() + "/" + set_name
    with open(file_path, 'wb') as f:
        data = await file.read()
        f.write(data)
