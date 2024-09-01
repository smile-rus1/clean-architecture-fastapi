from fastapi import Depends, Request
from fastapi.responses import JSONResponse

from src.application.user.usecases.user import UserService
from src.presentation.api.handlers.user.user.controllers.router import user_router
from src.presentation.api.providers.abstract.services import (
    user_provider_with_auth
)


@user_router.delete(
    "/{user_id}",
)
async def delete_user(
        user_id: int,
        user_service: UserService = Depends(user_provider_with_auth)
) -> JSONResponse:
    await user_service.delete_user(user_id)
    return JSONResponse(status_code=200, content={"message": "User successfully delete"})

