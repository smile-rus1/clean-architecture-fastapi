import pytest

from src.infrastructure.mapper.build_mapper import build_mapper


@pytest.fixture
def mapper():
    return build_mapper()
