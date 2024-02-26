import uuid
from datetime import datetime
from pydantic import UUID4, BaseModel,validator
from typing import List, Optional, Dict


class WebhookRegisterRequest(BaseModel):
    event_type_id: str
    user_id: int
    url: str
    custom_headers: Optional[Dict[str, str]]
    custom_payload: Optional[Dict[str, str]]


class WebhookData(BaseModel):
    id: uuid.UUID
    user_id: int
    url: str
    created_at: datetime
    updated_at: datetime

    class Config:
        populate_by_name = True
        from_attributes = True
    
    @validator("id", allow_reuse=True)
    def validate_uuids(cls, value):
        if value:
            print(value)
            return str(value)
        return value
    
    @validator("created_at","updated_at", allow_reuse=True)
    def validate_datetime(cls,value):
        # Attempt to parse the datetime string
        try:
            # If the value is already a datetime object, return it directly
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d %H:%M:%S")
            # Otherwise, parse the string into a datetime object
            parsed_date = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            # If parsing fails, raise a ValueError
            raise ValueError(f"Invalid datetime format for {value}. Required format: YYYY-MM-DD HH:MM:SS") from e
        return parsed_date
        
class WebhookExecute(BaseModel):
    url: str
    user_id: int
    webhook_id: str

    class Config:
        populate_by_name = True
        from_attributes = True

class WebhookConfigurationData(BaseModel):
    id: str = None
    webhook_id: str = None
    event_type_id: str
    custom_headers: dict[str, str] = None
    custom_payload: dict[str, str] = None

    class Config:
        populate_by_name = True
        from_attributes = True

class WebhookRegistrationData(BaseModel):
    id: uuid.uuid4 = None
    user_id: int
    url: str

    class Config:
        populate_by_name = True
        from_attributes = True