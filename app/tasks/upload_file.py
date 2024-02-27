import os
import requests
from core.factory import factoryApp
from schema.upload_file import UploadFileEvent
from schema.webhook import WebhookExecute, WebhookRegisterParams

from repositories.webhook import WebhookRepository

factory = factoryApp()
celery = factory.celery
webhook_repo = WebhookRepository(factory.session)


class UploadFileTask(object):
    def __init__(self) -> None:
        pass

    @celery.task(bind=True)
    def publish_upload_file(self, data: dict):
        input: UploadFileEvent = UploadFileEvent(**data)
        file_path = os.path.join(factory.upload_file, input.filename)
        with open(file_path, "wb") as file:
            file.write(input.file_content)

        return {
            "webhook_id":input.webhook_ID
        }

    @celery.task(bind=True)
    def webhook(self, data: dict):
        input: WebhookExecute = WebhookExecute(**data)
        webhook_register = webhook_repo.find_one_webhook_register(
            WebhookRegisterParams(id=input.webhook_id)
        )
        response = requests.post(webhook_register.url)
        return response.json()
