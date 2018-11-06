import pytest
fixture = None
from fixture.app_manager import AppManager
from  fixture.data.test_data import plans




@pytest.fixture(scope='function')
def app(request):

    fixture = AppManager()
    return fixture

@pytest.fixture(scope='function')
def app_streamer(request):
    global fixture
    if fixture == None:
        fixture = AppManager()
    fixture.api_helper.get_registered_and_logged_user(app=fixture)
    return fixture

@pytest.fixture(params=plans, scope='function', ids=[str(x['description']) for x in plans])
def plan(request):

    return request.param






