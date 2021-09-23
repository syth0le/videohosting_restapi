class Config:
    __file_save_path = "files"
    __postgres = f"postgresql://alterstrada:alterstrada@localhost:5432/alterstrada"
    __templates_path = "templates"

    @classmethod
    def getSavePath(cls):
        return cls.__file_save_path

    @classmethod
    def getTemplatesPath(cls):
        return cls.__templates_path

    @classmethod
    def getPostgresUrl(cls):
        return cls.__postgres
