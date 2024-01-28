from pydantic import BaseModel
from typing import List, Optional,Dict

class WebhookRegisterRequest(BaseModel):
    event_type_id: str
    user_id: int
    url: str
    event_type_id: str
    custom_headers: Optional[Dict[str, str]]
    custom_payload: Optional[Dict[str, str]]