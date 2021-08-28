from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class OwnerModel(BaseModel):
    id: UUID = Field(alias="uuid")
    username: str
    name: str
    lastname: str
    logo: str
    kyc: bool
    bio: Optional[str]
