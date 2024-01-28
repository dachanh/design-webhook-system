from pydantic import TypeAdapter
from typing import Generic, TypeVar, Annotated

from core.factory import factoryApp
from models.webhook_registrations import WebhookRegistrationModel,WebhookRegistrationData
from models.webhook_configuration import WebhookConfigurationModel,WebhookConfigurationData
from schema.webhook import WebhookRegisterRequest


def registerWebhookController(appctx: factoryApp, data : WebhookRegisterRequest):
    print(data)
    webhookData = WebhookRegistrationData(**data)
    print(webhookData.dict())
    webhookModel = WebhookRegistrationModel(**webhookData.dict())
    # insert webhook register model
    appctx.session.add(webhookModel)
    appctx.session.commit()
    print(webhookModel.id)
    webhookConfigData = WebhookConfigurationData(**data)
    webhookConfigData.webhook_id =  webhookModel.id
    webConfigModel = WebhookConfigurationModel(**webhookConfigData.dict())
    # print(type(webConfigModel.id))
    # webConfigModel.event_type_id = webhookRegisterModel.id

    appctx.session.add(webConfigModel)
    appctx.session.commit()


    return None 