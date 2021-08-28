from pydantic import BaseModel, Field


class InfoModel(BaseModel):
    id: int = Field(alias="uuid")
    user_id: int
    name: str
    url: str
    description: str = Field(alias="desc")
    callback: str
    logo: str
    secret: int
    active: int
    enabled: int
