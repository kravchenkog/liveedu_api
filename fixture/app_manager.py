from fixture.environment import Environment
from fixture.route_helper import Route
from fixture.api_user_helper import APIHelper
from fixture.property_user_factory import UserParseFactory
from fixture.string_generator_helper import StringGeneratoHelper
from fixture.property_user_factory import UserData
from fixture.property_user_factory import RealUserData
from fixture.data.activity_data import ActivityCosts




class AppManager:

    def __init__(self):
        self.env = Environment(3)
        self.route = Route()
        self.api_helper = APIHelper()
        self.user_parse = UserParseFactory()
        self.user_data = UserData()
        self.string_generator = StringGeneratoHelper()
        self.real_user_data = RealUserData()
        self.act_price = ActivityCosts()



