from fastapi import Depends, Request

from src.application.user.dto.user import SearchParametersDTO
from src.application.user.usecases.user import UserService
from src.presentation.api.handlers.common.utils.from_getter import from_getter
from src.presentation.api.handlers.user.user.controllers.router import user_router
from src.presentation.api.handlers.user.user.requests.get_request import SearchUserParameters
from src.presentation.api.handlers.user.user.responses.user import UserVM, UsersVM
from src.presentation.api.presenter.presenter import Presenter
from src.presentation.api.providers.abstract.common import presenter_provider
from src.presentation.api.providers.abstract.services import (
    user_provider_with_optional_auth,
    user_provider_without_auth
)


@user_router.get(
    "/search",
    status_code=200,
    response_model=list[UserVM]
)
async def search_user(
        request: Request,
        search_parameters: SearchUserParameters = Depends(),
        presenter: Presenter = Depends(presenter_provider),
        user_service: UserService = Depends(user_provider_without_auth)
):
    from_getter(request=request, model=search_parameters)
    search_parameters_dto = SearchParametersDTO(
        first_name=search_parameters.first_name,
        last_name=search_parameters.last_name,
        email=search_parameters.email,
        limit=search_parameters.limit,
        offset=search_parameters.offset,
    )
    users_dto = await user_service.search_users(search_parameters_dto)
    return presenter.load(UsersVM, users_dto).users


@user_router.get(
    "/{user_id}",
    response_model=UserVM
)
async def get_user(
        user_id: int,
        presenter: Presenter = Depends(presenter_provider),
        user_service: UserService = Depends(user_provider_with_optional_auth)
):
    user_dto = await user_service.get_user(user_id)
    return presenter.load(UserVM, user_dto)
