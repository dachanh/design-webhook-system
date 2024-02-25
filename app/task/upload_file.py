import os
import requests
from core.factory import factoryApp
from schema.upload_file import UploadFileEvent
from schema.webhook import WebhookExecute
factory = factoryApp()
event = factory.celery




class UploadFileTask(object):
    def __init__(self) -> None:
        pass

    @event.task(bind=True)
    def publish_upload_file(self,data: dict):
        input:UploadFileEvent = UploadFileEvent(**data)
        file_path = os.path.join(factory.upload_file,input.filename)
        
        with open(file_path,"'wb") as file:
            file.write(input.file_content)
        
        return "ok"
    @event.task
    def webhook(self,data: dict):
        input: WebhookExecute = WebhookExecute(**data)
        response =  requests.post(input.url)
        return response.json()

