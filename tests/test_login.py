
class TestLogin:
    def test_WHEN_user_is_reg_AND_pass_is_incorrect_EXPECTED_status_code_400_TC90051(self, app):
        app.user_data = app.api_helper.get_registered_user(app)
        app.user_data.password1 = app.string_generator.get_random_two_passwords()[0]
        resp_conf = app.api_helper.email_confirmation(app)
        resp_log = app.api_helper.login_perform(app)
        assert resp_log['status_code'] == 400

    def test_WHEN_user_is_reg_AND_pass_is_incorrect_EXPECTED_response_text_is_ok_TC9052(self, app):
        app.user_data = app.api_helper.get_registered_user(app)
        app.user_data.password1 = app.string_generator.get_random_two_passwords()[0]
        resp_conf = app.api_helper.email_confirmation(app)
        resp_log = app.api_helper.login_perform(app)
        assert resp_log['non_field_errors'][0] == 'Unable to log in with provided credentials.'

    def test_WHEN_user_is_reg_AND_username_is_incorrect_EXPECTED_response_code_400_TC9053(self, app):
        app.user_data = app.api_helper.get_registered_user(app)
        app.user_data.username = app.string_generator.get_random_username()
        resp_conf = app.api_helper.email_confirmation(app)
        resp_log = app.api_helper.login_perform(app)
        assert resp_log['status_code'] == 400

    def test_WHEN_user_is_reg_AND_email_is_not_confirmed_EXPECTED_response_code_400_TC9054(self, app):
        app.user_data = app.api_helper.get_registered_user(app)
        app.user_data.email = app.string_generator.get_random_email()
        #resp_conf = app.api_helper.email_confirmation(app)
        resp_log = app.api_helper.login_perform(app)
        assert resp_log['status_code'] == 400


    def test_WHEN_user_is_reg_AND_email_is_not_confirmed_EXPECTED_response_code_400_TC9055(self, app):
        app.user_data = app.api_helper.get_registered_user(app)
        app.user_data.email = app.string_generator.get_random_email()
        #resp_conf = app.api_helper.email_confirmation(app)
        resp_log = app.api_helper.login_perform(app)
        assert resp_log['non_field_errors'][0] == 'E-mail is not verified.'

    def test_WHEN_user_is_reg_AND_login_is_perform_EXPECTED_token_is_received_TC90056(self, app):
        app.user_data = app.api_helper.get_registered_user(app)
        resp_conf = app.api_helper.email_confirmation(app)
        resp_log = app.api_helper.login_perform(app)
        assert len(resp_log['token']) > 10

    def test_WHEN_login_is_performed_EXPECTED_email_is_proper_TC90057(self, app):
        app.user_data = app.api_helper.get_registered_user(app)
        app.api_helper.email_confirmation(app)
        app.api_helper.login_perform_and_parse_fields(app)
        assert app.user_data.email == app.real_user_data.email

    def test_WHEN_login_is_performed_EXPECTED_username_is_proper_TC90058(self, app):
        app.user_data = app.api_helper.get_registered_user(app)
        app.api_helper.email_confirmation(app)
        app.api_helper.login_perform_and_parse_fields(app)
        assert app.user_data.email == app.real_user_data.email

    def test_WHEN_login_is_performed_EXPECTED_userrole_is_proper_TC90059(self, app):
        app.user_data = app.api_helper.get_registered_user(app)
        app.api_helper.email_confirmation(app)
        app.api_helper.login_perform_and_parse_fields(app)
        assert app.user_data.userrole == app.real_user_data.user_role









