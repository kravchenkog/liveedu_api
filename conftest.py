import pytest
fixture = None
from fixture.app_manager import AppManager


@pytest.fixture(scope='function')
def app(request):

    fixture = AppManager()
    return fixture

@pytest.fixture(scope='function')
def app_streamer(request):
    global fixture
    if fixture == None:
        fixture = AppManager()
    streamer = fixture.api_helper.get_registered_user(app=fixture)
    return streamer




