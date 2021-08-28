from datetime import datetime

from pydantic import BaseModel, Field


class TransactionModel(BaseModel):
    id: str = Field(alias="uuid")
    user_id: int
    app_id: int
    amount: str
    description: str
    remote_id: str
    status: str
    paid_by_user_id: int
    created_at: datetime
    updated_at: datetime
    signed: int
