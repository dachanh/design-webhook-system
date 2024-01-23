from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ErrorLog(Base):
    __tablename__ = 'error_log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    webhook_execution_id = Column(Integer, ForeignKey('webhook_executions.id'), nullable=False)
    error_message = Column(String, nullable=False)
    retry_count = Column(Integer, default=0)
    next_retry_time = Column(DateTime)
