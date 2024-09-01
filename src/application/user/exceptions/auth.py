from dataclasses import dataclass

from src.application.common.exceptions.applications import ApplicationException


class AuthException(ApplicationException):
    ...


@dataclass
class InvalidEmail(AuthException):
    email: str

    def message(self):
        return f"User with email {self.email} not registered"


class InvalidPassword(AuthException):
    def message(self):
        return f"Wrong password"