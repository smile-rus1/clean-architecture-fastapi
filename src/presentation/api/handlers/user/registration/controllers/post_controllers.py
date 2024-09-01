from fastapi import Depends

from src.presentation.api.providers.abstract.common import presenter_provider
from src.presentation.api.providers.abstract.services import user_provider_without_auth
from src.application.user.dto.user import CreateUserDTO
from src.application.user.usecases.user import UserService
from src.presentation.api.handlers.user.registration.controllers.router import register_router
from src.presentation.api.handlers.user.registration.requests.post_requests import UsersCreateVM
from src.presentation.api.handlers.user.registration.responses.user import UserVM
from src.presentation.api.presenter.presenter import Presenter


@register_router.post(
    "",
    status_code=201,
    response_model=UserVM
)
async def registration(
        user_data: UsersCreateVM,
        user_service: UserService = Depends(user_provider_without_auth),
        presenter: Presenter = Depends(presenter_provider)
):
    create_user_dto = CreateUserDTO(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        password=user_data.password,
        updated_at=None,
        created_at=None
    )
    user_dto = await user_service.create_user(create_user_dto)
    return presenter.load(UserVM, user_dto)
