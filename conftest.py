import pytest


@pytest.fixture(scope="session")
def global_stat():
    return 10
