import pytest
fixture = None
from fixture.app_manager import AppManager
from  fixture.data.test_data import plans
from fixture.property_user_factory import UserData
from fixture.environment import Environment



@pytest.fixture(scope='function')
def app(request):

    fixture = AppManager()
    return fixture

@pytest.fixture(scope='module')
def app_streamer(request):
    global fixture
    if fixture == None:
        fixture = AppManager()
   # fixture.env = Environment(1)
    fixture.user_data = UserData()
    fixture.api_helper.get_registered_and_logged_user(app=fixture)
    return fixture

@pytest.fixture(params=plans, scope='function', ids=[str(x['description']) for x in plans])
def plan(request):

    return request.param






