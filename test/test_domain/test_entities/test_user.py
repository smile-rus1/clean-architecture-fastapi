from datetime import datetime

import pytest

from src.domain.common.exceptions.validation import InvalidID, EmailValidationError
from src.domain.user.entities.user import User
from src.domain.user.value_objects.user import (
    UserID,
    Email,
    FirstName,
    LastName
)


@pytest.fixture
def user():
    return User(
        id=UserID(1),
        first_name=FirstName("Test"),
        last_name=LastName("User"),
        email=Email("test@mail.ru"),
        password="123456789",
        updated_at=datetime.now(),
        created_at=datetime.now()
    )


def test_create_user(user):
    assert user is not None


def test_update_user(user):
    expected_user = user
    expected_user.id = 5
    expected_user.email = "new_test_email@mail.ru"
    user.update(user_id=UserID(5), email=Email("new_test_email@mail.ru"))

    assert user == expected_user


def test_create_negative_id(user):
    with pytest.raises(InvalidID):
        user.update(user_id=UserID(-1))


def test_create_negative_email(user):
    with pytest.raises(EmailValidationError):
        user.update(email=Email("tessst"))

