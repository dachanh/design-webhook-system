from pydantic import BaseModel, HttpUrl
from typing import List, Optional,Dict

class WebhookRegisterRequest(BaseModel):
    event_type: str
    url: str
    custom_headers: Optional[Dict[str, str]]
    custom_payload: Optional[Dict[str, str]]
