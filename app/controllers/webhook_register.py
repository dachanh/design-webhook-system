from pydantic import TypeAdapter
from typing import Generic, TypeVar, Annotated

from core.factory import factoryApp
from models.webhook_registrations import WebhookRegistrationModel,WebhookRegistrationData
from models.webhook_configuration import WebhookConfigurationModel,WebhookConfigurationData
from schema.webhook import WebhookRegisterRequest


def registerWebhookController(appctx: factoryApp, data : WebhookRegisterRequest):
    print(data)
    webhookData = WebhookRegistrationData(**data.dict())
    print(webhookData.dict())
    webhookModel = WebhookRegistrationModel(**webhookData.dict())
    # insert webhook register model
    appctx.session.add(webhookModel)
    appctx.session.commit()
    print("webhook_id",webhookModel.id)
    print("type webhook_id",type(webhookModel.id))
    # data['webhook_id'] = webhookModel.id
    webhookConfigData = WebhookConfigurationData(**data.dict())
    webhookConfigData.webhook_id =  webhookModel.id
    print("*"*10000)
    print(webhookConfigData)
    webConfigModel = WebhookConfigurationModel(**webhookConfigData.dict())
    # print(type(webConfigModel.id))
    # webConfigModel.event_type_id = webhookRegisterModel.id

    appctx.session.add(webConfigModel)
    appctx.session.commit()


    return None 