from datetime import datetime

from fastapi import Depends

from src.application.user.dto.user import UpdateUserDTO
from src.application.user.usecases.user import UserService
from src.presentation.api.handlers.user.user.responses.user import UserVM
from src.presentation.api.handlers.user.user.controllers.router import user_router
from src.presentation.api.handlers.user.user.requests.patch_request import UpdateUserVM
from src.presentation.api.presenter.presenter import Presenter
from src.presentation.api.providers.abstract.common import presenter_provider
from src.presentation.api.providers.abstract.services import user_provider_with_auth
from src.presentation.api.providers.auth import security_auth


@user_router.patch(
    "/{user_id}",
    response_model=UserVM
)
async def update_user(
        user_id: int,
        user_data: UpdateUserVM,
        presenter: Presenter = Depends(presenter_provider),
        user_service: UserService = Depends(user_provider_with_auth),
        # auth: security_auth = Depends(security_auth)  # для openAPI
):
    update_user_dto = UpdateUserDTO(
        id=user_id,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        password=user_data.password,
        created_at=None,
        updated_at=datetime.now(),
    )
    user_dto = await user_service.update_user(update_user_dto)
    return presenter.load(UserVM, user_dto)
