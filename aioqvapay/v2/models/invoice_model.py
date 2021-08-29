from uuid import UUID

from pydantic import BaseModel, Field


class InvoiceModel(BaseModel):
    app_id: UUID
    transation_id: UUID = Field(alias="transation_uuid")
    amount: float
    description: str
    remote_id: str
    signed: int
    url: str
    signed_url: str = Field(alias="signedUrl")
