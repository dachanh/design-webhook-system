import os
from core.factory import factoryApp
from schema.upload_file import UploadFileEvent
factory_app = factoryApp()

event = factory_app.celery


@event.task
def publish_upload_file(data: dict):
    req :UploadFileEvent = UploadFileEvent(**data)
    file_path = os.path.join(factory_app.upload_file,req.filename)

    with open(file_path,"'wb") as file:
        file.write(req.file_content)
    
    return "ok"


