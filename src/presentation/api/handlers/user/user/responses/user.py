from datetime import datetime

from pydantic import BaseModel, Field


class UserVM(BaseModel):
    id: int = Field(alias="id", default=None)
    first_name: str = Field(alias="first_name")
    last_name: str = Field(alias="last_name")
    email: str = Field(alias="email")
    created_at: datetime = Field(alias="created_at", default=None)
    updated_at: datetime = Field(alias="updated_at", default=None)

    class Config:
        populate_by_name = True


class UsersVM(BaseModel):
    users: list[UserVM]
