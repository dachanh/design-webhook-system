import os
import requests
from core.factory import factoryApp
from schema.upload_file import UploadFileEvent
from schema.webhook import (
    WebhookExecute,
    WebhookRegisterParams,
    WebhookConfigurationData,
)

from repositories.webhook import WebhookRepository

from tasks.task_base_class import BaseTaskWithRetry

factory = factoryApp()
celery = factory.celery
webhook_repo = WebhookRepository(factory.session)


class UploadFileTask(object):
    def __init__(self) -> None:
        pass

    @celery.task(bind=True, base=BaseTaskWithRetry)
    def publish_upload_file(self, data: dict):
        input: UploadFileEvent = UploadFileEvent(**data)
        file_path = os.path.join(factory.upload_file, input.filename)
        with open(file_path, "wb") as file:
            file.write(input.file_content)

        return {"webhook_id": input.webhook_id}

    @celery.task(bind=True, base=BaseTaskWithRetry)
    def webhook(self, data: dict):
        input: WebhookExecute = WebhookExecute(**data)
        webhook_register = webhook_repo.find_one_webhook_register(
            WebhookRegisterParams(id=input.webhook_id)
        )

        webhook_config = webhook_repo.find_webhook_config(webhook_id=input.webhook_id)

        headers = {}
        body = {}

        if webhook_config.custom_headers is not None:
            headers = webhook_config.custom_headers
            print(headers)

        if webhook_config.custom_payload is not None:
            body = webhook_config.custom_payload

        response = requests.post(webhook_register.url, headers=headers, json=body)
        # print(response.status_code)
        if response.status_code != 200:
            raise Exception("The task is failed")

        return {}
