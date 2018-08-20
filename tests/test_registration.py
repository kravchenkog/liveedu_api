

class TestRegistration:

    # def test_test_WHEN_registration_request_AND_all_values_ok_EXPECTED_response_text_is_correct(self, app):
    #
    #     passwords = app.string_generator.get_random_two_passwords()
    #     app.user_data.password1 = '9696666g'
    #     app.user_data.password2 = '9696666g'
    #     app.user_data.email = 'liveedutv.grigory@gmail.com'
    #     app.user_data.username = 'Tester969'
    #     app.user_data.userrole = 'streamer'
    #     data = {'email': app.user_data.email, 'password1': app.user_data.password1, 'password2': app.user_data.password2,
    #             'username': app.user_data.username, 'user_role': app.user_data.userrole}
    #     response = app.api_helper.general_post(app=app, route=app.route.register, data=data)
    #     assert response['detail'] == 'Verification e-mail sent.'
    def test_WHEN_registration_request_AND_all_values_ok_EXPECTED_response_text_is_correct(self, app):

        passwords = app.string_generator.get_random_two_passwords()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        app.user_data.email = app.string_generator.get_random_email()
        app.user_data.username = app.string_generator.get_random_username()
        app.user_data.userrole = 'streamer'
        data = {'email': app.user_data.email, 'password1': app.user_data.password1, 'password2': app.user_data.password2,
                'username': app.user_data.username, 'user_role': app.user_data.userrole}
        response = app.api_helper.general_post(app=app, route=app.route.register, data=data)
        assert response['detail'] == 'Verification e-mail sent.' #90040

    def test_WHEN_registration_request_AND_all_values_ok_EXPECTED_response_code_201(self, app):

        passwords = app.string_generator.get_random_two_passwords()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        app.user_data.email = app.string_generator.get_random_email()
        app.user_data.username = app.string_generator.get_random_username()
        app.user_data.userrole = 'streamer'
        data = {'email': app.user_data.email, 'password1': app.user_data.password1, 'password2': app.user_data.password2,
                'username': app.user_data.username, 'user_role': app.user_data.userrole}
        response = app.api_helper.general_post(app=app, route=app.route.register, data=data)
        assert response['status_code'] == 201

    def test_WHEN_registration_request_AND_passwords_notthesame_EXPECTED_response_code_400(self, app):

        passwords = app.string_generator.get_random_two_passwords_not_the_same()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        app.user_data.email = app.string_generator.get_random_email()
        app.user_data.username = app.string_generator.get_random_username()
        app.user_data.userrole = 'streamer'
        data = {'email': app.user_data.email, 'password1': app.user_data.password1, 'password2': app.user_data.password2,
                'username': app.user_data.username, 'user_role': app.user_data.userrole}
        response = app.api_helper.general_post(app=app, route=app.route.register, data=data)
        assert response['status_code'] == 400 #90041

    def test_WHEN_registration_request_AND_email_incorrect_EXPECTED_response_code_400(self, app):

        passwords = app.string_generator.get_random_two_passwords()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        app.user_data.email = app.string_generator.get_random_incorrect_email_type1()
        app.user_data.username = app.string_generator.get_random_username()
        app.user_data.userrole = 'streamer'
        data = {'email': app.user_data.email, 'password1': app.user_data.password1, 'password2': app.user_data.password2,
                'username': app.user_data.username, 'user_role': app.user_data.userrole}
        response = app.api_helper.general_post(app=app, route=app.route.register, data=data)
        assert response['status_code'] == 400 #90042

    def test_WHEN_registration_request_AND_username_incorrect_EXPECTED_response_code_400(self, app):

        passwords = app.string_generator.get_random_two_passwords()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        app.user_data.email = app.string_generator.get_random_email()
        app.user_data.username = app.string_generator.get_random_username_long()
        app.user_data.userrole = 'streamer'
        data = {'email': app.user_data.email, 'password1': app.user_data.password1, 'password2': app.user_data.password2,
                'username': app.user_data.username, 'user_role': app.user_data.userrole}
        response = app.api_helper.general_post(app=app, route=app.route.register, data=data)
        assert response['status_code'] == 400 #90043

    def test_WHEN_registration_request_AND_userrole_incorrect_EXPECTED_response_code_400(self, app):

        passwords = app.string_generator.get_random_two_passwords()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        app.user_data.email = app.string_generator.get_random_email()
        app.user_data.username = app.string_generator.get_random_username_long()
        app.user_data.userrole = 'streamerr'
        data = {'email': app.user_data.email, 'password1': app.user_data.password1, 'password2': app.user_data.password2,
                'username': app.user_data.username, 'user_role': app.user_data.userrole}
        response = app.api_helper.general_post(app=app, route=app.route.register, data=data)
        assert response['status_code'] == 400 #90044

    def test_WHEN_registration_request_AND_plus_slug_EXPECTED_response_code_201(self, app):

        passwords = app.string_generator.get_random_two_passwords()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        app.user_data.email = app.string_generator.get_random_email()
        app.user_data.username = app.string_generator.get_random_username()
        app.user_data.userrole = 'streamer'
        app.user_data.slug = app.api_helper.get_random_list_of_slugs(app)

        data = {'email': app.user_data.email,
                'password1': app.user_data.password1,
                'password2': app.user_data.password2,
                'username': app.user_data.username,
                'user_role': app.user_data.userrole,
                'want_learn': app.user_data.slug}

        response = app.api_helper.general_post(app=app, route=app.route.register, data=data)
        assert response['status_code'] == 201 #90045

    def test_WHEN_registration_request_AND_plus_incorrect_slug_EXPECTED_response_code_400(self, app):

        passwords = app.string_generator.get_random_two_passwords()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
        app.user_data.email = app.string_generator.get_random_email()
        app.user_data.username = app.string_generator.get_random_username()
        app.user_data.userrole = 'streamer'
        app.user_data.slug = [app.string_generator.get_random_username()]

        data = {'email': app.user_data.email,
                'password1': app.user_data.password1,
                'password2': app.user_data.password2,
                'username': app.user_data.username,
                'user_role': app.user_data.userrole,
                'want_learn': app.user_data.slug}

        response = app.api_helper.general_post(app=app, route=app.route.register, data=data)
        assert response['status_code'] == 400 #90046

    def test_WHEN_registration_request_AND_plus_skype_hangouts_EXPECTED_response_code_201(self, app):
        passwords = app.string_generator.get_random_two_passwords()
        app.user_data.password1 = passwords[0]
        app.user_data.password2 = passwords[1]
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

        response = app.api_helper.general_post(app=app, route=app.route.register, data=data)
        assert response['status_code'] == 201 #90047

    def test_WHEN_registration_completed_AND_email_is_confirmed_EXPECTED_login_is_preformaed(self, app):
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
        data_confirm ={'email': app.user_data.email, 'key': '992927E5B1C8A237875C70A302A34E22'}
        response_confirm = app.api_helper.general_post(app=app, route=app.route.email_confirmation, data=data_confirm)
        response_login = app.api_helper.general_post(
            app=app, route=app.route.login, data={'username': app.user_data.username, 'password': app.user_data.password1})
        assert response_login['status_code'] == 200 #90050



