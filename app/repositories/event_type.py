from models.event_type import EventTypeModel
from schema.event_type import EventType


class EventTypeRepository:
    def __init__(self, session):
        self.session = session

    def list_event(self, input: EventType):
        query = self.session.query(EventTypeModel)

        if input.id != None:
            query = query.filter(EventTypeModel.id == input.id)

        if input.name != None:
            query = query.filter(EventType.name == input.name)

        items = query.all()

        return items

    def find_one(self, input: EventType):
        query = self.session.query(EventTypeModel)

        if input.id != None:
            query = query.filter(EventTypeModel.id == input.id)

        if input.name != None:
            query = query.filter(EventType.name == input.name)

        item = query.first()

        return item
