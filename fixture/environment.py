import copy

class Environment:


    def __init__(self, env_type, params={}):

        dev = {'params': '', 'baseurl': 'https://dev.liveedu.tv',
               'headers':
                   {'Content-Type': 'application/json',
                    'Authorization': 'Basic bGl2ZWNvZGluZ3R2OmNzRUFNSFBmb2V0V1V5WTNoeHdOUFh1TQ=='}}

        stg = {'baseurl': 'http://stg.liveedu.tv'}
        prod = {'baseurl': 'http://liveedu.tv'}
        cookies = {'nginx_auth': '23942c07f8f8dc87baf2a2afa32e2af4'}
        if env_type == 1:
            self.base_url = copy.deepcopy(dev['baseurl'])
            self.headers = copy.deepcopy(dev['headers'])
            self.params = params
            self.cookies = cookies

        if env_type == 2:
            self.base_url = self.prod['baseurl']

def set_env_values(environment):
    env = Environment
    env.base_url = environment['baseurl']
    return env