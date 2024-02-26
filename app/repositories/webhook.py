from sqlalchemy import select, func
from models.webhook_registrations import (
    WebhookRegistrationModel,
)
from models.webhook_configuration import (
    WebhookConfigurationModel,
)

from schema.webhook import WebhookConfigurationData, WebhookRegistrationData


class WebhookRepository:
    def __init__(self, session):
        self.session = session

    def add(self, model):
        self.session.add(model)
        self.session.commit()

    def create_registration_model(self, data):
        webhookData = WebhookRegistrationData(**data.dict())
        return WebhookRegistrationModel(**webhookData.dict())

    def create_config_model(self, data, webhook_id):
        webhookConfigData = WebhookConfigurationData(**data.dict())
        webhookConfigData.webhook_id = webhook_id
        return WebhookConfigurationModel(**webhookConfigData.dict())

    def find_webhook_config(self, webhook_id: str):
        item = (
            self.session.query(WebhookConfigurationModel)
            .filter(WebhookConfigurationModel.webhook_id == webhook_id)
            .first()
        )

        return item

    def find_webhook_register(self, user_id: int, webhook_register_id: str):
        item = (
            self.session.query(WebhookRegistrationModel)
            .filter(
                WebhookRegistrationModel.user_id == user_id,
                WebhookRegistrationModel.id == webhook_register_id,
            )
            .first()
        )

        return item
