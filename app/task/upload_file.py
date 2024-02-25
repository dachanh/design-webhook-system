import os
import requests
from core.factory import factoryApp
from schema.upload_file import UploadFileEvent
from schema.webhook import WebhookExecute
factory = factoryApp()
celery = factory.celery




class UploadFileTask(object):
    def __init__(self) -> None:
        pass

    @celery.task(bind=True)
    def publish_upload_file(self,data: dict):
        input:UploadFileEvent = UploadFileEvent(**data)
        file_path = os.path.join(factory.upload_file,input.filename)
        print(type(input.file_content))
        with open(file_path,"wb") as file:
            file.write(input.file_content)
        
        return "ok"
    @celery.task(bind=True)
    def webhook(self,data: dict):
        input: WebhookExecute = WebhookExecute(**data)
        response =  requests.post(input.url)
        return response.json()

