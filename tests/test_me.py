
class TestCheckEmail:
    def test_twst(self, app):
        app.user_data = app.api_helper.get_registered_user(app)
        app.api_helper.email_confirmation(app)
        app.api_helper.login_perform_and_parse_fields(app)
        app.env.headers['Authorization'] = 'Bearer '+app.real_user_data.token
        app.api_helper.general_get(app=app, route=app.route.me)