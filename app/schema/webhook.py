from pydantic import UUID4, BaseModel
from typing import List, Optional, Dict


class WebhookRegisterRequest(BaseModel):
    event_type_id: str
    user_id: int
    url: str
    custom_headers: Optional[Dict[str, str]]
    custom_payload: Optional[Dict[str, str]]


class WebhookExecute(BaseModel):
    url: str
    user_id: int
    webhook_id: str
