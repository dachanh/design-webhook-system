from pydantic import TypeAdapter
from typing import Generic, TypeVar, Annotated

from core.factory import factoryApp
from models.webhook_registrations import (
    WebhookRegistrationModel,
    WebhookRegistrationData,
)
from models.webhook_configuration import (
    WebhookConfigurationModel,
    WebhookConfigurationData,
)
from schema.webhook import WebhookRegisterRequest


def registerWebhookController(appctx: factoryApp, data: WebhookRegisterRequest):
    webhookData = WebhookRegistrationData(**data.dict())
    webhookModel = WebhookRegistrationModel(**webhookData.dict())
    # insert webhook register model
    appctx.session.add(webhookModel)
    appctx.session.commit()
    # data['webhook_id'] = webhookModel.id
    webhookConfigData = WebhookConfigurationData(**data.dict())
    webhookConfigData.webhook_id = webhookModel.id
    webConfigModel = WebhookConfigurationModel(**webhookConfigData.dict())
    appctx.session.add(webConfigModel)
    appctx.session.commit()

    return None
