from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class TransactionModel(BaseModel):
    id: UUID = Field(alias="uuid")
    app_id: int
    amount: float
    description: str
    remote_id: UUID
    status: str
    created_at: datetime
    updated_at: datetime
    signed: Optional[int]
