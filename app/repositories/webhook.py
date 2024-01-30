from models.webhook_registrations import (
    WebhookRegistrationModel,
    WebhookRegistrationData,
)
from models.webhook_configuration import (
    WebhookConfigurationModel,
    WebhookConfigurationData,
)
class WebhookRepository:
    def __init__(self, session):
        self.session = session

    def add(self, model):
        try:
            self.session.add(model)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def create_registration_model(self, data):
        webhookData = WebhookRegistrationData(**data.dict())
        return WebhookRegistrationModel(**webhookData.dict())

    def create_config_model(self, data, webhook_id):
        webhookConfigData = WebhookConfigurationData(**data.dict())
        webhookConfigData.webhook_id = webhook_id
        return WebhookConfigurationModel(**webhookConfigData.dict())