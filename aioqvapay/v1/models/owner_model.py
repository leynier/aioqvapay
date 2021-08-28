from pydantic import BaseModel, Field


class OwnerModel(BaseModel):
    id: str = Field(alias="uuid")
    username: str
    name: str
    lastname: str
    logo: str
