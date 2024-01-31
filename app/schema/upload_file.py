from pydantic import BaseModel


class UploadFileEvent(BaseModel):
    file_content: bytes
    filename: str
