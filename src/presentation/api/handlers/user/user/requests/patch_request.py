from pydantic import BaseModel, Field


class UpdateUserVM(BaseModel):
    first_name: str = Field(alias='first_name', default="")
    last_name: str = Field(alias='last_name', default="")
    email: str = Field(alias='email', default="")
    password: str = Field(alias='password', default="")

    class Config:
        populate_by_name = True
