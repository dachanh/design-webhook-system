from app.core.factory import factoryApp
from app.models.webhook_registrations import WebhookRegistrationModel
from app.models.webhook_configuration import WebhookConfigurationModel
from app.schema.webhook import WebhookRegisterRequest


def registerWebhookController(appctx: factoryApp, data : WebhookRegisterRequest):
    webhookRegisterModel = WebhookRegistrationModel(**data.dict())
    # insert webhook register model
    appctx.session.add(webhookRegisterModel)
    appctx.session.commit()

    webConfigModel = WebhookConfigurationModel(**data.dict())
    webConfigModel.event_type_id = webhookRegisterModel.id

    appctx.session.add(webConfigModel)
    appctx.session.commit()


    return None 