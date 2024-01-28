import uuid
from pydantic import BaseModel ,Json as pydantic_json
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID,JSON

Base = declarative_base()

class WebhookConfigurationModel(Base):
    __tablename__ = 'webhook_configurations'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    webhook_id = Column(UUID, ForeignKey('webhook_registrations.id'), nullable=False)
    event_type_id = Column(Integer, ForeignKey('event_types.id'), nullable=False)
    custom_headers = Column(JSON)
    custom_payload = Column(JSON)

    class Config:
        populate_by_name = True
        from_attributes = True


class WebhookConfigurationData(BaseModel):
    id : uuid.uuid4 = None
    webhook_id: uuid.uuid4  = None
    event_type_id: uuid.uuid4
    custom_headers: pydantic_json
    custom_payload: pydantic_json