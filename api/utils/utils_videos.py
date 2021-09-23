from fastapi import UploadFile


async def writeVideo(set_name: str, file: UploadFile):
    with open(set_name, 'wb') as f:
        data = await file.read()
        f.write(data)
