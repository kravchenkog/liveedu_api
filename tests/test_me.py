from random import randint
from random import choice
#
# class TestCheckMePositive:

    # def test_WHEN_token_is_added_AND_me_EXPECTED_status_code_is_200_TC___(self, app):
    #     app.user_data = app.api_helper.get_registered_and_logged_user(app)
    #     resp = app.api_helper.general_get(app=app, route=app.route.me)
    #     assert resp['status_code'] == 200
    #
    # def test_WHEN_put_not_all_fields_EXPECTED_status_code_is_400TC_(self, app):
    #     app.user_data = app.api_helper.get_registered_and_logged_user(app)
    #     topics = app.api_helper.get_random_slug_topic(app)
    #     data = {
    #         'topics': [topics]
    #     }
    #     resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
    #     assert resp['status_code'] == 400
    #
    # def test_WHEN_put_newtopic_EXPECTED_status_code_is_200TC_(self, app):
    #     app.user_data = app.api_helper.get_registered_and_logged_user(app)
    #     topics = app.api_helper.get_random_slug_topic(app)
    #     data = {
    #     "email": app.user_data.email,
    #     "topics": [topics],
    #     "categories": [],
    #     "birthday_day": None,
    #     "birthday_month": None,
    #     "birthday_year": None,
    #     "avatar": None,
    #     "timezone": "UTC"
    #     }
    #     resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
    #     assert resp['status_code'] == 200
    #
    # def test_WHEN_put_newSeveraltopics_EXPECTED_list_of_topics_is_properTC_(self, app):
    #     app.user_data = app.api_helper.get_registered_and_logged_user(app)
    #     topics_list = app.api_helper.get_num_slug_topic(app, 3)
    #     data = {
    #     "email": app.user_data.email,
    #     "topics": topics_list,
    #     "categories": [],
    #     "birthday_day": None,
    #     "birthday_month": None,
    #     "birthday_year": None,
    #     "avatar": None,
    #     "timezone": "UTC"
    #     }
    #     resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
    #     assert set(topics_list) == set(resp['topics']) and len(topics_list) == len(resp['topics'])
    #
    # def test_WHEN_put_newtopic_AND_category_EXPECTED_list_of_cat_is_properTC_(self, app):
    #     app.user_data = app.api_helper.get_registered_and_logged_user(app)
    #     topics_list = app.api_helper.get_num_slug_topic(app, 1)
    #     app.route.topics = app.route.topics + topics_list[0] + '/categories'
    #     cat_resp = app.api_helper.general_get(app, route=app.route.topics)
    #     cat_list_slug = choice([x['slug'] for x in cat_resp['results']])
    #     data = {
    #     "email": app.user_data.email,
    #     "topics": topics_list,
    #     "categories": [cat_list_slug],
    #     "birthday_day": None,
    #     "birthday_month": None,
    #     "birthday_year": None,
    #     "avatar": None,
    #     "timezone": "UTC"
    #     }
    #     resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
    #     assert cat_list_slug == resp['categories'][0]
    #
    # def test_WHEN_put_timezone_EXPECTED_value_is_savedTC_(self, app):
    #     app.user_data = app.api_helper.get_registered_and_logged_user(app)
    #     timezone = "Africa/Freetown"
    #     data = {
    #     "email": app.user_data.email,
    #     "topics": [],
    #     "categories": [],
    #     "birthday_day": None,
    #     "birthday_month": None,
    #     "birthday_year": None,
    #     "avatar": None,
    #     "timezone": timezone
    #     }
    #     resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
    #     assert resp["timezone"] == timezone
    #
    # def test_WHEN_put_birthday_day_EXPECTED_value_is_savedTC_(self, app):
    #     app.user_data = app.api_helper.get_registered_and_logged_user(app)
    #     birthday_day = 30
    #     timezone = "PDT"
    #     data = {
    #     "email": app.user_data.email,
    #     "topics": [],
    #     "categories": [],
    #     "birthday_day": birthday_day,
    #     "birthday_month": None,
    #     "birthday_year": None,
    #     "avatar": None,
    #     "timezone": "UTC"
    #     }
    #     resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
    #     assert resp["birthday_day"] == birthday_day
    #
    # def test_WHEN_put_birthday_month_EXPECTED_value_is_savedTC_(self, app):
    #     app.user_data = app.api_helper.get_registered_and_logged_user(app)
    #     birthday_month = 12
    #     data = {
    #     "email": app.user_data.email,
    #     "topics": [],
    #     "categories": [],
    #     "birthday_day": None,
    #     "birthday_month": birthday_month,
    #     "birthday_year": None,
    #     "avatar": None,
    #     "timezone": "UTC"
    #     }
    #     resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
    #     assert resp["birthday_month"] == birthday_month
    #
    # def test_WHEN_put_birthday_year_EXPECTED_value_is_savedTC_(self, app):
    #     app.user_data = app.api_helper.get_registered_and_logged_user(app)
    #     birthday_year = 1984
    #     data = {
    #     "email": app.user_data.email,
    #     "topics": [],
    #     "categories": [],
    #     "birthday_day": None,
    #     "birthday_month": None,
    #     "birthday_year": birthday_year,
    #     "avatar": None,
    #     "timezone": "UTC"
    #     }
    #     resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
    #     assert resp["birthday_year"] == birthday_year

class TestCheckMeDelete:
    # def test_WHEN_delete_EXPECTED_login_is_notTC_(self, app):
    #     app.user_data = app.api_helper.get_registered_and_logged_user(app)
    #     app.api_helper.general_delete(app=app, route=app.route.me, data=None)
    #     resp = app.api_helper.login_perform(app)
    #     assert resp['status_code'] == 400

    def test_WHEN_delete_EXPECTED_signup_is_notTC_(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        app.api_helper.general_delete(app=app, route=app.route.me, data=None)
        resp = app.api_helper.get_registered_user(app, app.user_data)
        assert resp['status_code'] == 400

# class TestCheckMeDelete:
#     def test_WHEN_me_balanses_EXPECTED_response_code_is_200TC_(self, app):
#         app.user_data = app.api_helper.get_registered_and_logged_user(app)
#         resp = app.api_helper.general_get(app, app.route.me_balanses)
#         assert resp['status_code'] == 200









