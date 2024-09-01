from dataclasses import dataclass

from src.application.common.exceptions.applications import ApplicationException


class BaseUserExceptions(ApplicationException):
    ...


@dataclass
class UserAlreadyExist(BaseUserExceptions):
    email: str

    def message(self):
        return f"User with email {self.email} already exist"


@dataclass
class UserNotFoundByEmail(BaseUserExceptions):
    email: str

    def message(self):
        return f"User with email {self.email} not found"


@dataclass
class UserIDException(BaseUserExceptions):
    user_id: int


@dataclass
class UserNotFoundByID(UserIDException):
    def message(self):
        return f"User with user_id {self.user_id} not found"


@dataclass
class UserAccessError(UserIDException):
    def message(self):
        return f"Access denied to user account with user_id {self.user_id}!"
