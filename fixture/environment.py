import copy

class Environment:


    def __init__(self, env_type, params=None):

        dev = {'params': '', 'baseurl': 'https://dev.liveedu.tv',
               'headers':
                   {'Content-Type': 'application/json',
                    'Authorization': 'Basic bGl2ZWNvZGluZ3R2OmNzRUFNSFBmb2V0V1V5WTNoeHdOUFh1TQ=='}}

        stg = {'baseurl': 'http://stg.liveedu.tv'}
        prod = {'baseurl': 'http://liveedu.tv'}

        if env_type == 1:
            self.base_url = copy.deepcopy(dev['baseurl'])
            self.headers = copy.deepcopy(dev['headers'])
            self.params = params
        if env_type == 2:
            self.base_url = self.prod['baseurl']

def set_env_values(environment):
    env = Environment
    env.base_url = environment['baseurl']
    return env