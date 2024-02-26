from core.factory import factoryApp
from schema.event_type import EventTypeParams

from repositories.event_type import EventTypeRepository


def ListEventType(appctx: factoryApp, data: EventTypeParams):

    repository = EventTypeRepository(appctx.session)

    items = repository.list_event(data)

    return items
