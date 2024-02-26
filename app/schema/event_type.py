from uuid import UUID
from pydantic import BaseModel,validator


class EventTypeParams(BaseModel):
    id: str = None
    name: str = None


class EventType(BaseModel):
    id: UUID 
    name: str 
    description: str

    class Config:
        populate_by_name = True
        from_attributes = True

    @validator("id")
    def validate_uuids(cls, value):
        if value:
            return str(value)
        return value