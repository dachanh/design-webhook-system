import os
from core.factory import factoryApp
from schema.upload_file import UploadFileEvent

factory = factoryApp()
event = factory.celery




class UploadFileWebhook(object):
    def __init__(self) -> None:
        pass

    @event.task
    def publish_upload_file(self,data: dict):
        input:UploadFileEvent = UploadFileEvent(**data)
        file_path = os.path.join(factory.upload_file,input.filename)

        with open(file_path,"'wb") as file:
            file.write(input.file_content)
        
        return "ok"
    
    def webhook(self,data: dict):
        input =  