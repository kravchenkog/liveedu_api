from random import randint

class TestCheckMePositive:

    def test_WHEN_token_is_added_AND_me_EXPECTED_status_code_is_200_TC___(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert resp['status_code'] == 200








