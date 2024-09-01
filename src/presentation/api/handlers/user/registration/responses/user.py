from pydantic import BaseModel, Field


class UserVM(BaseModel):
    id: int = Field(alias="id")
    first_name: str = Field(alias="first_name")
    last_name: str = Field(alias="last_name")
    email: str = Field(alias="email")

    class Config:
        populate_by_name = True


class UsersVM(BaseModel):
    users: list[UserVM]
