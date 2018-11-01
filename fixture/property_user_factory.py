class UserData:
    def __init__(self, email=None, password=None, username=None, password1=None, password2=None,
                 userrole=None, slug=None, response_reg = None):
        self.email = email
        self.password = password
        self.username = username
        self.password1 = password1
        self.password2 = password2
        self.userrole = userrole
        self.slug = slug
        self.response_reg = response_reg
#test
class RealUserData:
    def __init__(self, email=None, username=None, user_role=None, slug=None, url=None,
                 avatar = None, is_premium = None, count_followers=None, site_url=None,
                 registration_date=None, projects=None, active_project=None, profile=None,
                 plan=None, token = None):
        self.email = email
        self.username = username
        self.user_role = user_role
        self.slug = slug
        self.url = url
        self.avatar = avatar
        self.is_premium = is_premium
        self.count_followers = count_followers
        self.site_url = site_url
        self.registration_date = registration_date
        self.projects = projects
        self.active_project = active_project
        self.profile = profile
        self.plan = plan
        self.token = token
#

class UserParseFactory:


    def parse_user_properties(self, resp_dict=None, app=None):

        all_fields = ['email', 'username', 'user_role', 'slug', 'url',
                      'avatar', 'is_premium', 'count_followers', 'site_url',
                      'registration_date', 'projects', 'active_project',
                      'profile', 'plan', 'token']
        for field in all_fields:
            if field in resp_dict.keys():
                setattr(app.real_user_data, field, resp_dict[field])

        return app

    def test(self):
        pass