from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from src.application.user.dto.auth import AuthUserDTO
from src.application.user.usecases.auth import AuthService
from src.presentation.api.auth import AuthorizationBasic
from src.presentation.api.providers.abstract.services import auth_service_provider

auth = AuthorizationBasic()
security_auth = HTTPBasic()


async def optional_auth_getter(
        credentials: HTTPBasicCredentials = Depends(auth),
        auth_service: AuthService = Depends(auth_service_provider)
):
    if credentials:
        auth_dto = AuthUserDTO(
            email=credentials.username,
            password=credentials.password
        )
        return await auth_service.authenticate_user(auth_dto)


async def auth_getter(
        credentials: HTTPBasicCredentials = Depends(auth),
        auth_service: AuthService = Depends(auth_service_provider)
):
    if credentials is None:
        raise HTTPException(
            status_code=403,
            detail={"message": "Sent a registration from authorized account"}
        )

    auth_dto = AuthUserDTO(
        email=credentials.username,
        password=credentials.password
    )
    return await auth_service.authenticate_user(auth_dto)


async def without_auth_getter(credentials: HTTPBasicCredentials = Depends(auth)):
    if credentials:
        raise HTTPException(
            status_code=403,
            detail={"message": "Sent a registration from authorized account"}
        )
