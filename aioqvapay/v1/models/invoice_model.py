from pydantic import BaseModel, Field


class InvoiceModel(BaseModel):
    app_id: str
    transation_id: str = Field(alias="transation_uuid")
    amount: str
    description: str
    remote_id: str
    signed: int
    url: str
    signed_url: str
