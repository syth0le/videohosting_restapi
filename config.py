class Config:
    __file_save_path = "files"

    @classmethod
    def getSavePath(cls):
        return cls.__file_save_path
