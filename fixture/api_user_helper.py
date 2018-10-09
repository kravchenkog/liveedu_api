import random
import requests
import json


class APIHelper:

    def general_get(self, app, route):
        url = str(app.env.base_url) + str(route)

        response = requests.request("GET", url, headers=app.env.headers, params=app.env.params, cookies = app.env.cookies)
        try:
            responce_j = json.loads(response.text)
            if type(responce_j) == list:
                responce_j = {'data': responce_j}

            responce_j['status_code'] = response.status_code

            return responce_j

        except:
            print(str(response))

    def general_post(self, app, route, data):
        url = str(app.env.base_url) + str(route)
        if data is None:
            data = {}
        if len(app.env.headers) > 1:
            data = json.dumps(data)

        responce = requests.request("POST", url, data=data, headers=app.env.headers, cookies = app.env.cookies)
        try:
            responce_j = json.loads(responce.text)
            responce_j['status_code'] = responce.status_code

            return responce_j
        except:
            print("_____________________________ERROR_JSON_LOADS_______________________________")
            print(responce.text)

    def get_all_slug_topics(self, app, route):
        topics = self.general_get(app, route)
        slugs = []
        for topic in topics['results']:

           slugs.append(topic['slug'])

        return slugs

    def get_random_slug_topic(self, app):
        list_of_slugs = self.get_all_slug_topics(app, route=app.route.topics)
        random_slug = list_of_slugs[random.randint(0, len(list_of_slugs) - 1)]
        return random_slug

    def get_num_slug_topic(self, app, num):
        list_of_slugs = self.get_all_slug_topics(app, route=app.route.topics)
        my_list = []
        if num > len(list_of_slugs):
            num = len(list_of_slugs)
        for a in range(num):
            el = random.choice(list_of_slugs)
            my_list.append(el)
            list_of_slugs.remove(el)

        return my_list

    def get_random_list_of_slugs(self, app):
        list_of_all = self.get_all_slug_topics(app, route=app.route.topics)
        no_el = random.randint(0, len(list_of_all) - 1)
        list_slugs = []
        for el in range(no_el):
            x = random.choice(list_of_all)
            list_slugs.append(x)
            list_of_all.remove(x)
        return list_slugs

    def get_registered_user(self, app):
        app.user_data.password1, app.user_data.password2 = app.string_generator.get_random_two_passwords()
        app.user_data.email = app.string_generator.get_random_email()
        app.user_data.username = app.string_generator.get_random_username()
        app.user_data.userrole = 'streamer'
        app.user_data.slug = app.api_helper.get_random_list_of_slugs(app)
        data = {'email': app.user_data.email,
                'password1': app.user_data.password1,
                'password2': app.user_data.password2,
                'username': app.user_data.username,
                'user_role': app.user_data.userrole,
                'want_learn': app.user_data.slug,
                'skype': '123',
                'hangouts': 'sdfsdf'}
        response_reg = app.api_helper.general_post(app=app, route=app.route.register, data=data)
        return app.user_data

    def get_registered_and_logged_user(self, app):
        self.get_registered_user(app)
        self.email_confirmation(app)
        self.login_perform_and_parse_fields(app)
        app.env.headers['Authorization'] = 'JWT ' + app.real_user_data.token
        return app.user_data


    def email_confirmation(self, app):
        data_confirm = {'email': app.user_data.email, 'key': '992927E5B1C8A237875C70A302A34E22'}
        return self.general_post(app=app, route=app.route.email_confirmation, data=data_confirm)

    def login_perform(self, app):
        response_login = self.general_post(
            app=app,
            route=app.route.login,
            data={
                'username': app.user_data.username,
                'password': app.user_data.password1
                  })
        return response_login

    def login_perform_and_parse_fields(self, app):
        resp_log = self.login_perform(app=app)
        resp_log['user']['token'] = resp_log['token']
        app.user_parse.parse_user_properties(resp_dict=resp_log['user'], app=app)
        return app

    def purchase_package(self, app, plan, no_topics):
        topics = self.get_num_slug_topic(app=app, num=no_topics)
        data = {'plan': plan,
                'service': 'stripe',
                'token': 'tok_visa',
                'topics': topics}
        return self.general_post(app=app, route=app.route.subscription, data=data)

    def get_list_of_plans(self, app):
        return self.general_get(app=app, route=app.route.plans)

    def get_plan(self, app, plan):
        all_plans = self.get_list_of_plans(app)
        my_plan = [x for x in all_plans['data'] if x['id'] == plan][0]
        return my_plan

    def register_user_and_purchaqse_subs(self, app, plan_name):
        my_plan = self.get_plan(app, plan_name)
        app.user_data = self.get_registered_and_logged_user(app)

        puerchasing = app.api_helper.purchase_package(
            app, plan=my_plan['id'], no_topics=my_plan['topic_qty'])
        return my_plan