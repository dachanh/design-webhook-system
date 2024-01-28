from typing_extensions import TypedDict
from pydantic import UUID4
from typing import List, Optional,Dict

class WebhookRegisterRequest(TypedDict):
    event_type_id: UUID4
    user_id: int
    url: str
    custom_headers: Optional[Dict[str, str]]
    custom_payload: Optional[Dict[str, str]]