from datetime import datetime

from pydantic import BaseModel, Field


class AppModel(BaseModel):
    id: str = Field(alias="uuid")
    user_id: int
    name: str
    url: str
    description: str = Field(alias="desc")
    callback: str
    success_url: str
    cancel_url: str
    logo: str
    active: int
    enabled: int
    created_at: datetime
    updated_at: datetime
