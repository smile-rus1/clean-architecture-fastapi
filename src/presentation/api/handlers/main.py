from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

from src.application.user.exceptions.user import BaseUserExceptions
from src.presentation.api.handlers.user.common import user_exception_handler
from src.presentation.api.handlers.user.user.controllers import user_router
from src.presentation.api.handlers.user.registration.controllers import register_router

from src.domain.common.exceptions.validation import BaseModelException
from src.application.user.exceptions.auth import AuthException
from src.infrastructure.database.repo.common.exceptions.base import BaseRepoException

from src.presentation.api.handlers.common import (
    auth_exception_handler,
    common_validation_exception_handler,
    validation_exception_handler,
    request_validation_exception_handler
)


def bind_exceptions_handlers(app: FastAPI):
    app.add_exception_handler(AuthException, auth_exception_handler)
    app.add_exception_handler(ValidationError, validation_exception_handler)
    app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
    app.add_exception_handler(BaseRepoException, common_validation_exception_handler)
    app.add_exception_handler(BaseModelException, common_validation_exception_handler)
    app.add_exception_handler(BaseUserExceptions, user_exception_handler)


def bind_routers(app: FastAPI):
    app.include_router(register_router)
    app.include_router(user_router)
