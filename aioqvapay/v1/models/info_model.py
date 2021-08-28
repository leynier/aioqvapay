from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class InfoModel(BaseModel):
    id: UUID = Field(alias="uuid")
    user_id: int
    name: str
    url: str
    description: str = Field(alias="desc")
    callback: str
    success_url: str
    cancel_url: str
    logo: str
    active: bool
    enabled: bool
    card: int
    created_at: datetime
    updated_at: datetime
