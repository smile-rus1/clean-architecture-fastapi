import json

from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

from src.application.user.exceptions.auth import AuthException
from src.domain.common.exceptions.validation import BaseModelException
from src.infrastructure.database.repo.common.exceptions.base import BaseRepoException


async def common_validation_exception_handler(_, exc: BaseModelException | BaseRepoException):
    return JSONResponse(status_code=400, content={"message": exc.message()})


async def auth_exception_handler(_, exc: AuthException):
    return JSONResponse(status_code=401, content={"message": exc.message()})


async def validation_exception_handler(_, err: ValidationError | RequestValidationError):
    return JSONResponse(status_code=400, content=json.loads(err.json()))


async def request_validation_exception_handler(_, err: RequestValidationError):
    return JSONResponse(status_code=400, content=err.errors())
