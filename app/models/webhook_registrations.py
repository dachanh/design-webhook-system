import uuid
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class WebhookRegistrationModel(Base):
    __tablename__ = 'webhook_registrations'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer, nullable=False)
    url = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    class Config:
        populate_by_name = True
        from_attributes = True
