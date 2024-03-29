from sqlalchemy import select, func
from models.webhook_registrations import (
    WebhookRegistrationModel,
)
from models.webhook_configuration import (
    WebhookConfigurationModel,
)

from schema.webhook import (
    WebhookConfigurationData,
    WebhookRegistrationData,
    WebhookRegisterParams,
)


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

    def find_webhook_config(self, webhook_id):
        item = (
            self.session.query(WebhookConfigurationModel)
            .filter(WebhookConfigurationModel.webhook_id == webhook_id)
            .one()
        )

        return item

    def find_one_webhook_register(self, input: WebhookRegisterParams):
        stmt = self.session.query(WebhookRegistrationModel)

        if input.url != None:
            stmt = stmt.filter(WebhookRegistrationModel.url == input.url)

        if input.id != None:
            stmt = stmt.filter(WebhookRegistrationModel.id == input.id)

        if input.user_id != None:
            stmt = stmt.filter(WebhookConfigurationModel.user_id == input.user_id)

        item = stmt.one()

        return item
