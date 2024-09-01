from fastapi import FastAPI

from src.presentation.config.config import Config

from . import common, services, abstract, auth


def bind_common(app: FastAPI, config: Config):
    app.dependency_overrides[abstract.common.session_provider] = common.db_session(config)
    app.dependency_overrides[abstract.common.mapper_provider] = common.mapper_getter
    app.dependency_overrides[abstract.common.hasher_provider] = common.hasher_getter
    app.dependency_overrides[abstract.common.uow_provider] = common.uow_getter
    app.dependency_overrides[abstract.common.presenter_provider] = common.presenter_getter


def bind_auth(app: FastAPI):
    app.dependency_overrides[abstract.auth.auth_provider] = auth.auth_getter
    app.dependency_overrides[abstract.auth.optional_auth_provider] = auth.optional_auth_getter
    app.dependency_overrides[abstract.auth.without_auth_provider] = auth.without_auth_getter


def bind_services(app: FastAPI):
    app.dependency_overrides[
        abstract.services.user_provider_without_auth] = services.user_service_without_auth_getter
    app.dependency_overrides[
        abstract.services.auth_service_provider] = services.auth_service_getter
    app.dependency_overrides[
        abstract.services.user_provider_with_optional_auth] = services.user_service_with_optional_getter
    app.dependency_overrides[
        abstract.services.user_provider_with_auth] = services.user_service_with_auth_getter


def bind_providers(app: FastAPI, config: Config):
    bind_common(app, config)
    bind_auth(app)
    bind_services(app)
