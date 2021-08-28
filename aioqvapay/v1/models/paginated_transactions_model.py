from typing import List, Optional

from pydantic import BaseModel, Field

from .transaction_model import TransactionModel


class PaginatedTransactionsModel(BaseModel):
    current_page: int
    last_page: int
    from_index: int = Field(alias="from")
    to_index: int = Field(alias="to")
    per_page: int
    total: int
    first_page_url: str
    last_page_url: str
    prev_page_url: Optional[str]
    next_page_url: Optional[str]
    path: str
    data: List[TransactionModel]
