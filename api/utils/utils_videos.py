from typing import Generator, IO

from fastapi import UploadFile

from config import Config


async def writeVideo(set_name: str, file: UploadFile):
    file_path = Config.getSavePath() + "/" + set_name
    with open(file_path, 'wb') as f:
        data = await file.read()
        f.write(data)


async def readVideo(title: str):
    path = Config.getSavePath() + "/" + "TEST_9a1c26e4-c3b8-44f2-b460-d399ae264172.mp4"
    with open(path, "rb") as f:
        print(f.readline())


def ranged(
        file: IO[bytes],
        start: int = 0,
        end: int = None,
        block_size: int = 8192,
) -> Generator[bytes, None, None]:
    consumed = 0

    file.seek(start)
    while True:
        data_length = min(block_size, end - start - consumed) if end else block_size
        if data_length <= 0:
            break
        data = file.read(data_length)
        if not data:
            break
        consumed += data_length
        yield data

    if hasattr(file, 'close'):
        file.close()
