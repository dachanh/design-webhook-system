from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WebhookConfiguration(Base):
    __tablename__ = 'webhook_configurations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    webhook_id = Column(Integer, ForeignKey('webhook_registrations.id'), nullable=False)
    event_type_id = Column(Integer, ForeignKey('event_types.id'), nullable=False)
    custom_headers = Column(String)
    custom_payload = Column(String)
