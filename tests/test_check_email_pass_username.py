
class TestCheckEmail:
    def test_WHEN_check_email_request_AND_email_is_correct_EXPECTED_response_text_is_correct(self, app):
        app.user_data.email = app.string_generator.get_random_email()
        data = {'email': app.user_data.email}
        response = app.api_helper.general_post(app=app, route=app.route.check_email, data=data)
        assert response['detail'] == 'The data is valid' #90010

    def test_WHEN_check_email_request_AND_email_is_correct_EXPECTED_status_code_is_200(self, app):
        app.user_data.email = app.string_generator.get_random_email()
        data = {'email': app.user_data.email}
        response = app.api_helper.general_post(app=app, route=app.route.check_email, data=data)
        assert response['status_code'] == 200 #90011

    def test_WHEN_check_email_request_AND_email_is_incorrect1_EXPECTED_status_code_is_400(self, app):
        app.user_data.email = app.string_generator.get_random_incorrect_email_type1()
        data = {'email': app.user_data.email}
        response = app.api_helper.general_post(app=app, route=app.route.check_email, data=data)
        assert response['status_code'] == 400 #90012

    def test_WHEN_check_email_request_AND_email_is_incorrect1_EXPECTED_response_text_is_correct(self, app):
        app.user_data.email = app.string_generator.get_random_incorrect_email_type1()
        data = {'email': app.user_data.email}
        response = app.api_helper.general_post(app=app, route=app.route.check_email, data=data)
        assert response['email'][0] == 'Enter a valid email address.' #90013

    def test_WHEN_check_email_request_AND_email_is_incorrect2_EXPECTED_status_code_is_400(self, app):
        app.user_data.email = app.string_generator.get_random_incorrect_email_type2()
        data = {'email': app.user_data.email}
        response = app.api_helper.general_post(app=app, route=app.route.check_email, data=data)
        assert response['status_code'] == 400 #90014

    def test_WHEN_check_email_request_AND_email_is_incorrect3_EXPECTED_status_code_is_400(self, app):
        app.user_data.email = app.string_generator.get_random_incorrect_email_type3()
        data = {'email': app.user_data.email}
        response = app.api_helper.general_post(app=app, route=app.route.check_email, data=data)
        assert response['status_code'] == 400 #90015

    def test_WHEN_check_email_request_AND_email_is_incorrect4_EXPECTED_status_code_is_400(self, app):
        app.user_data.email = app.string_generator.get_random_incorrect_email_type4()
        data = {'email': app.user_data.email}
        response = app.api_helper.general_post(app=app, route=app.route.check_email, data=data)
        assert response['status_code'] == 400 #90016

    def test_WHEN_check_email_request_AND_email_is_empty_EXPECTED_status_code_is_400(self, app):
        app.user_data.email = app.string_generator.get_random_incorrect_email_type5()
        data = {'email': app.user_data.email}
        response = app.api_helper.general_post(app=app, route=app.route.check_email, data=data)
        assert response['status_code'] == 400 #90017

    def test_WHEN_check_email_request_AND_email_is_empty_EXPECTED_response_text_is_correct(self, app):
        app.user_data.email = app.string_generator.get_random_incorrect_email_type5()
        data = {'email': app.user_data.email}
        response = app.api_helper.general_post(app=app, route=app.route.check_email, data=data)
        assert response['email'][0] == 'This field may not be blank.' #90018

class TestCheckPassword:

    def test_WHEN_check_password_request_AND_passwords_are_correct_EXPECTED_response_text_is_correct(self, app):
        passwords = app.string_generator.get_random_two_passwords()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        data = {'password1': app.user_data.password1, 'password2': app.user_data.password2}
        response = app.api_helper.general_post(app=app, route=app.route.check_password, data=data)
        assert response['detail'] == 'The data is valid' #90020

    def test_WHEN_check_password_request_AND_passwords_are_correct_EXPECTED_response_code_is_200(self, app):
        passwords = app.string_generator.get_random_two_passwords()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        data = {'password1': app.user_data.password1, 'password2': app.user_data.password2}
        response = app.api_helper.general_post(app=app, route=app.route.check_password, data=data)
        assert response['status_code'] == 200 #90021

    def test_WHEN_check_password_request_AND_passwords_are_not_the_same_EXPECTED_response_code_is_400(self, app):
        passwords = app.string_generator.get_random_two_passwords_not_the_same()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        data = {'password1': app.user_data.password1, 'password2': app.user_data.password2}
        response = app.api_helper.general_post(app=app, route=app.route.check_password, data=data)
        assert response['status_code'] == 400 #90022

    def test_WHEN_check_password_request_AND_passwords_are_not_the_same_EXPECTED_response_text_is_correct(self,app):
        passwords = app.string_generator.get_random_two_passwords_not_the_same()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        data = {'password1': app.user_data.password1, 'password2': app.user_data.password2}
        response = app.api_helper.general_post(app=app, route=app.route.check_password, data=data)
        assert response['non_field_errors'][0] == "The two password fields didn't match." #90023

    def test_WHEN_check_password_request_AND_passwords_are_numeric_EXPECTED_response_code_is_400(self, app):
        passwords = app.string_generator.get_random_two_passwords_numeric()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        data = {'password1': app.user_data.password1, 'password2': app.user_data.password2}
        response = app.api_helper.general_post(app=app, route=app.route.check_password, data=data)
        assert response['status_code'] == 400 #90024

    def test_WHEN_check_password_request_AND_passwords_are_short_EXPECTED_response_code_is_400(self, app):
        passwords = app.string_generator.get_random_two_passwords_short()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        data = {'password1': app.user_data.password1, 'password2': app.user_data.password2}
        response = app.api_helper.general_post(app=app, route=app.route.check_password, data=data)
        assert response['status_code'] == 400 #90025

    def test_WHEN_check_password_AND_passwords_are_thesame_but_lowandupcase_EXPECTED_response_code_is_400(self, app):
        passwords = app.string_generator.get_random_two_passwords_uppercase_lowercase_the_same()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        data = {'password1': app.user_data.password1, 'password2': app.user_data.password2}
        response = app.api_helper.general_post(app=app, route=app.route.check_password, data=data)
        assert response['status_code'] == 400 #90026

class TestCheckUsername:

    def test_WHEN_check_username_AND_value_correct_EXPECTED_response_text_is_correct(self, app):
        app.user_data.username = app.string_generator.get_random_username()
        data = {'username': app.user_data.username}
        response = app.api_helper.general_post(app=app, route=app.route.check_username, data=data)
        assert response['detail'] == 'The data is valid' #90030

    def test_WHEN_check_username_AND_value_correct_EXPECTED_response_code_200(self, app):
        app.user_data.username = app.string_generator.get_random_username()
        data = {'username': app.user_data.username}
        response = app.api_helper.general_post(app=app, route=app.route.check_username, data=data)
        assert response['status_code'] == 200 #90031

    def test_WHEN_check_username_AND_value_short_EXPECTED_response_code_400(self, app):
        app.user_data.username = app.string_generator.get_random_username_short()
        data = {'username': app.user_data.username}
        response = app.api_helper.general_post(app=app, route=app.route.check_username, data=data)
        assert response['status_code'] == 400 #90032

    def test_WHEN_check_username_AND_value_long_EXPECTED_response_code_400(self, app):
        app.user_data.username = app.string_generator.get_random_username_long()
        data = {'username': app.user_data.username}
        response = app.api_helper.general_post(app=app, route=app.route.check_username, data=data)
        assert response['status_code'] == 400 #90033

    def test_WHEN_check_username_AND_value_empty_EXPECTED_response_code_400(self, app):
        data = {'username': []}
        response = app.api_helper.general_post(app=app, route=app.route.check_username, data=data)
        assert response['status_code'] == 400 #90034



