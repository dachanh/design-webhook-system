from core.factory import factoryApp
from repositories.webhook import WebhookRepository
from schema.webhook import WebhookRegisterRequest


def registerWebhookController(appctx: factoryApp, data: WebhookRegisterRequest):
    """
    Registers a new webhook.
    Uses repository for database operations.
    """
    appctx.session.begin()
    repository = WebhookRepository(appctx.session)

    # Create models
    webhookModel = repository.create_registration_model(data)
    repository.add(webhookModel)

    webConfigModel = repository.create_config_model(data, webhookModel.id)
    # Persist models
    repository.add(webConfigModel)
    appctx.session.expunge_all()
    appctx.session.close()

    return webhookModel
