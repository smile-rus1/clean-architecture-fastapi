import pytest

from dataclasses import dataclass
from src.domain.common.entities.entity_merge import EntityMerge


@dataclass
class SomeEntity(EntityMerge):
    id: int
    value: str

    def update(self, status):
        self._merge(status=status)


@dataclass
class TestEntity(EntityMerge):
    id: int
    status: str
    value: int
    some_list: list | None = None
    some_dict: dict | None = None
    some_entity: SomeEntity | None = None

    def update_status(self, status):
        self._merge(status=status)

    def update_some_entity(self, entity):
        self._merge(some_entity=entity)

    def update_list(self, some_list):
        self._merge(some_list=some_list)

    def update_dict(self, some_dict):
        self._merge(some_dict=some_dict)


@pytest.fixture
def entity():
    return TestEntity(id=16, status="ok", value=1337)


@pytest.fixture
def expected_result():
    return {
        "id": 16,
        "status": "ok",
        "value": 1337,
        'some_dict': None,
        'some_list': None,
        'some_entity': None
    }


def test_merge(entity, expected_result):
    update_data = "new_status"
    expected_result["status"] = update_data
    entity.update_status(update_data)

    assert entity.__dict__ == expected_result


def test_merge_with_some_entity(entity, expected_result):
    some_entity = SomeEntity(id=1, value="value")
    expected_result["some_entity"] = some_entity
    entity.update_some_entity(some_entity)

    assert entity.__dict__ == expected_result


def test_merge_with_some_dict(entity, expected_result):
    some_dict = {"one": 1, "two": 2}
    updated_data = {"four": 4, "five": 5}
    expected_result["some_dict"] = some_dict | updated_data
    entity.some_dict = some_dict
    entity.update_dict(updated_data)

    assert entity.__dict__ == expected_result


def test_merge_with_some_list(entity, expected_result):
    some_list = [1, 2, 3, 4, 5]
    update_list = [9, 0]
    expected_result["some_list"] = some_list + update_list
    entity.some_list = some_list
    entity.update_list(update_list)

    assert entity.__dict__ == expected_result
