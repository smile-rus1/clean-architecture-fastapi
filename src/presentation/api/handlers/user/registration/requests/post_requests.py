from pydantic import BaseModel, Field


class UsersCreateVM(BaseModel):
    first_name: str = Field(alias="first_name")
    last_name: str = Field(alias="last_name")
    email: str = Field(alias="email")
    password: str = Field(alias="password")

    class Config:
        populate_by_name = True
