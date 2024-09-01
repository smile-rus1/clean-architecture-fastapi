from pydantic import BaseModel, Field


class SearchUserParameters(BaseModel):
    first_name: str = Field(alias='first_name', default='')
    last_name: str = Field(alias='last_name', default='')
    email: str = Field(alias='email', default='')
    limit: int = Field(alias='size', default=10)
    offset: int = Field(default=0)

    class Config:
        populate_by_name = True
