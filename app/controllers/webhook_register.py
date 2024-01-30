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
    """
    Registers a new webhook.
    Uses repository for database operations.
    """
    repository = WebhookRepository(appctx.session)

    # Create models
    webhookModel = repository.create_registration_model(data)
    webConfigModel = repository.create_config_model(data, webhookModel.id)

    # Persist models
    repository.add(webhookModel)
    repository.add(webConfigModel)

    return None