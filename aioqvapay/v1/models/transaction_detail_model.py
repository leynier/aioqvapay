from datetime import datetime

from pydantic import BaseModel, Field

from .app_model import AppModel
from .owner_model import OwnerModel
from .paid_by_model import PaidByModel


class TransactionDetailModel(BaseModel):
    id: str = Field(alias="uuid")
    user_id: int
    app_id: int
    amount: str
    description: str
    remote_id: int
    status: str
    paid_by_user_id: int
    signed: int
    created_at: datetime
    updated_at: datetime
    paid_by: PaidByModel
    app: AppModel
    owner: OwnerModel
