from pydantic import BaseModel


class PaidByModel(BaseModel):
    name: str
    logo: str
