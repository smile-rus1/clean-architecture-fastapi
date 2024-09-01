from datetime import datetime

import pytest

from src.application.user.dto.user import UserDTO, UserDTOs
from src.domain.user.entities.user import User
from src.domain.user.value_objects.user import (
    UserID,
    Email,
    FirstName,
    LastName
)
from src.infrastructure.database.models import UserDB


@pytest.fixture
def user_entity():
    return User(
            id=UserID(1),
            first_name=FirstName("Test"),
            last_name=LastName("User"),
            email=Email("test@mail.ru"),
            password="password",
            updated_at=None,
            created_at=None
        )


@pytest.fixture
def user_db_model():
    model = UserDB(
        id=1,
        first_name="Test",
        last_name="User",
        email="test@mail.ru",
        password="password",
        created_at=None,
        updated_at=None
    )
    model.__dict__.pop("_sa_instance_state")

    return model


@pytest.fixture
def user_dto():
    return UserDTO(
        id=1,
        first_name="Test",
        last_name="User",
        email="test@mail.ru",
        created_at=None,
        updated_at=None
    )


def test_entity_to_dto(mapper, user_entity, user_dto):
    result = mapper.load(UserDTO, user_entity)
    assert result == user_dto


def test_entity_to_model(mapper, user_entity, user_db_model):
    result = mapper.load(UserDB, user_entity)
    result.__dict__.pop("_sa_instance_state")

    assert result.__dict__ == user_db_model.__dict__
    assert type(result) == type(user_db_model)


def test_model_db_to_entity(mapper, user_db_model, user_entity):
    result = mapper.load(User, user_db_model)
    assert result == user_entity


def test_model_db_to_dto(mapper, user_db_model, user_dto):
    result = mapper.load(UserDTO, user_db_model)
    assert result == user_dto


def test_models_to_dtos(mapper, user_db_model, user_dto):
    expected_args = UserDTOs(users=[user_dto, user_dto, user_dto])
    result = mapper.load(UserDTOs, [user_db_model, user_db_model, user_db_model])

    assert result == expected_args
