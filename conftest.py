import pytest
fixture = None
from fixture.app_manager import AppManager


@pytest.fixture(scope='function')
def app(request):

    fixture = AppManager()
    return fixture



