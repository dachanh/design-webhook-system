from pydantic import BaseModel


class EventType(BaseModel):
    id: int = None
    name: str = None
