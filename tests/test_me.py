from random import randint
from random import choice

class TestCheckMePositive:

    def test_WHEN_token_is_added_AND_me_EXPECTED_status_code_is_200_TC90300(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert resp['status_code'] == 200

    def test_WHEN_put_new_topics_EXPECTED_status_code_is_200TC90301(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        topics = app.api_helper.get_random_slug_topic(app)
        data = {
            'topics': [topics]
        }
        resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert resp['topics'][0] == topics

    def test_WHEN_put_newtopic_EXPECTED_status_code_is_200TC90302(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        topics = app.api_helper.get_random_slug_topic(app)
        data = {"email": app.user_data.email,
                "topics": [topics],
                "categories": [],
                "birthday_day": None,
                "birthday_month": None,
                "birthday_year": None,
                "avatar": None,
                "timezone": "UTC"
                }
        resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert resp['status_code'] == 200

    def test_WHEN_put_newSeveraltopics_EXPECTED_list_of_topics_is_properTC90303(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        topics_list = app.api_helper.get_num_slug_topic(app, 3)
        data = {
            "email": app.user_data.email,
            "topics": topics_list,
            "categories": [],
            "birthday_day": None,
            "birthday_month": None,
            "birthday_year": None,
            "avatar": None,
            "timezone": "UTC"
                }
        resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert set(topics_list) == set(resp['topics']) and len(topics_list) == len(resp['topics'])

    def test_WHEN_put_newtopic_AND_category_EXPECTED_list_of_cat_is_properTC90304(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        topics_list = app.api_helper.get_num_slug_topic(app, 1)
        app.route.topics = app.route.topics + topics_list[0] + '/categories'
        cat_resp = app.api_helper.general_get(app, route=app.route.topics)
        cat_list_slug = choice([x['slug'] for x in cat_resp['results']])
        data = {
            "email": app.user_data.email,
            "topics": topics_list,
            "categories": [cat_list_slug],
            "birthday_day": None,
            "birthday_month": None,
            "birthday_year": None,
            "avatar": None,
            "timezone": "UTC"
                }
        resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert cat_list_slug == resp['categories'][0]

    def test_WHEN_put_timezone_EXPECTED_value_is_savedTC90305(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        timezone = "Africa/Freetown"
        data = {
            "email": app.user_data.email,
            "topics": [],
            "categories": [],
            "birthday_day": None,
            "birthday_month": None,
            "birthday_year": None,
            "avatar": None,
            "timezone": timezone
                }
        resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert resp["timezone"] == timezone

    def test_WHEN_put_birthday_day_EXPECTED_value_is_savedTC90306(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        birthday_day = 30
        data = {
            "email": app.user_data.email,
            "topics": [],
            "categories": [],
            "birthday_day": birthday_day,
            "birthday_month": None,
            "birthday_year": None,
            "avatar": None,
            "timezone": "UTC"
                }
        resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert resp["birthday_day"] == birthday_day

    def test_WHEN_put_birthday_month_EXPECTED_value_is_savedTC90307(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        birthday_month = 12
        data = {
            "email": app.user_data.email,
            "topics": [],
            "categories": [],
            "birthday_day": None,
            "birthday_month": birthday_month,
            "birthday_year": None,
            "avatar": None,
            "timezone": "UTC"
            }
        resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert resp["birthday_month"] == birthday_month

    def test_WHEN_put_birthday_year_EXPECTED_value_is_savedTC90308(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        birthday_year = 1984
        data = {
            "email": app.user_data.email,
            "topics": [],
            "categories": [],
            "birthday_day": None,
            "birthday_month": None,
            "birthday_year": birthday_year,
            "avatar": None,
            "timezone": "UTC"
                }
        resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert resp["birthday_year"] == birthday_year

class TestCheckMeDelete:
    def test_WHEN_delete_EXPECTED_login_is_notTC90309(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        app.api_helper.general_delete(app=app, route=app.route.me, data=None)
        resp = app.api_helper.login_perform(app)
        assert resp['status_code'] == 400

    def test_WHEN_delete_EXPECTED_signup_is_notTC90310(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        app.api_helper.general_delete(app=app, route=app.route.me, data=None)
        resp = app.api_helper.get_registered_user(app, app.user_data)
        assert app.user_data.response_reg['status_code'] == 400

class TestCheckMeBalanses:
    def test_WHEN_me_balanses_EXPECTED_response_code_is_200TC90311(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app, app.route.me_balanses)
        assert resp['status_code'] == 200

    def test_WHEN_user_is_registered_AND_me_balances_EXPECTED_balances_is_0TC90312(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app, app.route.me_balanses)
        assert float(resp['data'][0]['amount']) == 0
        assert float(resp['data'][0]['amount_usd']) == 0
        assert float(resp['data'][1]['amount']) == 0
        assert float(resp['data'][1]['amount_usd']) == 0

    def test_WHEN_buy_subscr_AND_me_balances_EXPECTED_balances_is_properTC90313(self, app):
        plan = 'lprot3'
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        app.api_helper.purchase_package(app, plan, 3)
        plan = app.api_helper.get_plan(app, plan)
        resp = app.api_helper.general_get(app, app.route.me_balanses)
        value1 = round(float(plan['balance_ledu']), 0)
        value2 = round(float(resp['data'][0]['amount']), 0)
        assert value1 == value2

class TestCheckMeBillingHistory:
    def test_WHEN_me_billing_EXPECTED_response_code_is_200TC90314(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app, app.route.me_billing_history)
        assert resp['status_code'] == 200

    def test_WHEN_user_is_registered_AND_me_billing_EXPECTED_list_is_emptyTC90315(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app, app.route.me_billing_history)
        assert resp['data'] == []

    def test_WHEN_buy_subcr_AND_me_billing_EXPECTED_amount_is_properTC90316(self, app):
        plan = 'lprot3'
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        app.api_helper.purchase_package(app, plan, 3)
        plan_resp = app.api_helper.get_plan(app, plan)
        resp = app.api_helper.general_get(app, app.route.me_billing_history)
        assert plan_resp['price'] == resp['data'][-1]['amount']

class TestCheckMeChatCred:
    def test_WHEN_chat_cred_EXPECTED_response_code_is_200TC90317(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app, app.route.me_chat_cred)
        assert resp['status_code'] == 200


class TestCheckMeFollowers:
    def test_WHEN_me_followers_EXPECTED_response_code_is_200TC90318(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app, app.route.me_followers)
        assert resp['status_code'] == 200

    def test_WHEN_me_followimg_EXPECTED_response_code_is_200TC90319(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app, app.route.me_following)
        assert resp['status_code'] == 200

class TestMePreferences:
    def test_WHEN_get_pref_EXPECTED_response_code_is_200TC90320(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app=app, route=app.route.me_preferences)
        assert resp['status_code'] == 200

    def test_WHEN_put_pref_activity_not_EXPECTED_value_saved_TC90321(self, app):
        activity_notify = False
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "activity_notify": activity_notify
        }
        resp = app.api_helper.general_put(app=app, route=app.route.me_preferences, data=data)
        assert resp['activity_notify'] == activity_notify

    def test_WHEN_put_pref_email_not_update_EXPECTED_value_saved_TC90322(self, app):
        email_general_updates = False
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "email_general_updates": email_general_updates
        }
        resp = app.api_helper.general_put(app=app, route=app.route.me_preferences, data=data)
        assert resp['email_general_updates'] == email_general_updates

    def test_WHEN_put_pref_topic_notif_EXPECTED_value_saved_TC90323(self, app):
        topic_notify = False
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "topic_notify": topic_notify
        }
        resp = app.api_helper.general_put(app=app, route=app.route.me_preferences, data=data)
        assert resp['topic_notify'] == topic_notify

    def test_WHEN_put_pref_category_notif_EXPECTED_value_saved_TC90324(self, app):
        category_notify = False
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "category_notify": category_notify
        }
        resp = app.api_helper.general_put(app=app, route=app.route.me_preferences, data=data)
        assert resp['category_notify'] == category_notify

    def test_WHEN_put_pref_folow_project_notif_EXPECTED_value_saved_TC90325(self, app):
        followed_projects_notify = False
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "followed_projects_notify": followed_projects_notify
        }
        resp = app.api_helper.general_put(app=app, route=app.route.me_preferences, data=data)
        assert resp['followed_projects_notify'] == followed_projects_notify

    def test_WHEN_put_pref_notify_type_EXPECTED_value_saved_TC90326(self, app):
        notify_type = 2
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "notify_type": notify_type
        }
        resp = app.api_helper.general_put(app=app, route=app.route.me_preferences, data=data)
        assert resp['notify_type'] == notify_type

    def test_WHEN_get_prefsubscr_EXPECTED_response_code_is_200TC90327(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app=app, route=app.route.me_subscr_notif)
        assert resp['status_code'] == 200

    def test_WHEN_post_prefsubscr_broadcaster_EXPECTED_value_saved_TC90328(self, app, app_streamer):
        broadcaster = app_streamer.username
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "broadcaster": broadcaster
        }
        resp = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        assert resp['broadcaster'] == broadcaster

    def test_WHEN_post_notifsubscr_AND_incorrectbroadcaster_EXPECTED_value_not_saved_TC90329(self, app):
        broadcaster = "12"
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "broadcaster": broadcaster
        }
        resp = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        assert resp['status_code'] == 400

    def test_WHEN_post_notifsubscr_AND_project_EXPECTED_value_is_saved_TC90330(self, app):
        project = choice(app.api_helper.general_get(app, app.route.projects)['results'])['slug']
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "project": project
        }
        resp = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        assert resp['project'] == project

    def test_WHEN_post_notifsubscr_AND_incorrect_project_EXPECTED_value_isnot_saved_TC90331(self, app):
        project = "1"
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "project": project
        }
        resp = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        assert resp['status_code'] == 400

    def test_WHEN_post_notifsubscr_AND_topics_EXPECTED_value_is_saved_TC90332(self, app):
        topics = choice(app.api_helper.general_get(app, app.route.topics)['results'])['slug']
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "topic": topics
        }
        resp = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        assert resp['topic'] == topics

    def test_WHEN_post_notifsubscr_AND_incorrect_topics_EXPECTED_value_is_notsaved_TC90333(self, app):
        topics = "wer"
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "topic": topics
        }
        resp = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        assert resp['status_code'] == 400

    def test_WHEN_post_notifsubscr_AND_topics_is_already_EXPECTED_value_isnot_saved_TC90334(self, app):
        topics = choice(app.api_helper.general_get(app, app.route.topics)['results'])['slug']
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "topic": topics
        }
        resp1 = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        resp = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        assert resp['status_code'] == 400

    def test_WHEN_post_notifsubscr_AND_category_EXPECTED_value_is_saved_TC90335(self, app):
        category = choice(app.api_helper.general_get(app, app.route.categories)['results'])['slug']
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "category": category
        }
        resp = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        assert resp['category'] == category

    def test_WHEN_post_notifsubscr_AND_incorrect_category_EXPECTED_value_isnot_saved_TC90336(self, app):
        category = "qwert"
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "category": category
        }
        resp = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        assert resp['status_code'] == 400

    def test_WHEN_post_notifsubscr_AND_category_is_already_EXPECTED_value_isnot_saved_TC90337(self, app):
        category = choice(app.api_helper.general_get(app, app.route.categories)['results'])['slug']
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "category": category
        }
        app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        resp = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        assert resp['status_code'] == 400

    def test_WHEN_post_notifsubscr_AND_difficulty_EXPECTED_value_is_saved_TC90338(self, app):
        category = choice(app.api_helper.general_get(app, app.route.categories)['results'])['slug']
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            "category": category
        }
        resp = app.api_helper.general_post(app=app, route=app.route.me_subscr_notif, data=data)
        assert resp['category'] == category

    #TODO /api/v3/me/notification/subscriptions/{id}/ GET PUT DELETE


class TestMePaymentMethods:
    def test_WHEN_get_me_payment_methods_EXPECTED_response_code_is_200TC90340(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app, app.route.me_payment_methods)
        assert resp['status_code'] == 200

    def test_WHEN_get_me_payment_methods_after_registration_EXPECTED_list_is_emptyTC90341(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app, app.route.me_payment_methods)
        assert resp['data'] == []

    def test_WHEN_post_me_payment_methods_AND_servise_ledu_EXPECTED_is_savedTC90342(self, app):
        service = "ledu"
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            'service': service,
        }
        resp = app.api_helper.general_post(app, app.route.me_payment_methods, data)
        assert resp['service'] == service

    def test_WHEN_post_me_payment_methods_AND_servise_stipe_token_EXPECTED_is_savedTC90343(self, app):
        service = "stripe"
        token = 'tok_visa'
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        data = {
            'service': service,
            "token": token
        }
        resp = app.api_helper.general_post(app, app.route.me_payment_methods, data)
        assert resp['service'] == service


    def test_WHEN_post_me_payment_method_AND_currency_EXPECTED_is_savedTC__(self, app):
        service = "stripe"
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        email = app.user_data.email
        data = {
            'service': service,
            "email": email,
            'token': 'tok_visa',
        }
        resp = app.api_helper.general_post(app, app.route.me_payment_methods, data)
        assert resp['service'] == service

class TestMeChangePassword:
    def test_WHEN_post_me_AND_password_positive_EXPECTED_response_200TC90350(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        newpass = app.string_generator.get_random_two_passwords()
        data = {"email": app.user_data.email,
                'old_password': app.user_data.password1,
                'new_password': newpass[0],
                'confirmed_password': newpass[1]
                }
        resp = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert resp['status_code'] == 200

    def test_WHEN_post_me_AND_password_change_EXPECTED_login_using_newTC90351(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        newpass = app.string_generator.get_random_two_passwords()
        data = {"email": app.user_data.email,
                'old_password': app.user_data.password1,
                'new_password': newpass[0],
                'confirmed_password': newpass[1]
                }
        app.api_helper.general_put(app=app, route=app.route.me, data=data)
        app.user_data.password1 = choice(newpass)
        login = app.api_helper.login_perform(app)
        assert login['status_code'] == 200

    def test_WHEN_post_me_AND_password_change_EXPECTED_login_using_oldTC90352(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        newpass = app.string_generator.get_random_two_passwords()
        data = {"email": app.user_data.email,
                'old_password': app.user_data.password1,
                'new_password': newpass[0],
                'confirmed_password': newpass[1]
                }
        app.api_helper.general_put(app=app, route=app.route.me, data=data)
        login = app.api_helper.login_perform(app)
        assert login['status_code'] == 400

    def test_WHEN_post_me_AND_not_the_same_passwordschange_EXPECTED_400TC90353(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        newpass = app.string_generator.get_random_two_passwords()
        data = {"email": app.user_data.email,
                'old_password': app.user_data.password1,
                'new_password': newpass[0],
                'confirmed_password': "123"
                }
        me = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert me['status_code'] == 400

    def test_WHEN_post_me_AND_numeric_passwordschange_EXPECTED_400TC90354(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        newpass = app.string_generator.get_random_two_passwords_numeric()
        data = {"email": app.user_data.email,
                'old_password': app.user_data.password1,
                'new_password': newpass[0],
                'confirmed_password': "123"
                }
        me = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert me['status_code'] == 400

    def test_WHEN_post_me_AND_short_passwordschange_EXPECTED_400TC90355(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        newpass = app.string_generator.get_random_two_passwords_short()
        data = {"email": app.user_data.email,
                'old_password': app.user_data.password1,
                'new_password': newpass[0],
                'confirmed_password': "123"
                }
        me = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert me['status_code'] == 400

    def test_WHEN_post_me_AND_upperlowercase_passwordschange_EXPECTED_400TC90356(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        newpass = app.string_generator.get_random_two_passwords_uppercase_lowercase_the_same()
        data = {"email": app.user_data.email,
                'old_password': app.user_data.password1,
                'new_password': newpass[0],
                'confirmed_password': newpass[1]
                }
        me = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert me['status_code'] == 400

    def test_WHEN_post_me_AND_incorrectold_password_EXPECTED_400TC90357(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        newpass = app.string_generator.get_random_two_passwords_uppercase_lowercase_the_same()
        data = {"email": app.user_data.email,
                'old_password': "123",
                'new_password': newpass[0],
                'confirmed_password': newpass[1]
                }
        me = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert me['status_code'] == 400

    def test_WHEN_post_me_AND_emptyold_password_EXPECTED_400TC90358(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        newpass = app.string_generator.get_random_two_passwords_uppercase_lowercase_the_same()
        data = {"email": app.user_data.email,
                'new_password': newpass[0],
                'confirmed_password': newpass[1]
                }
        me = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert me['status_code'] == 400

    def test_WHEN_post_me_AND_emptynew_password_EXPECTED_400TC90359(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        newpass = app.string_generator.get_random_two_passwords_uppercase_lowercase_the_same()
        data = {"email": app.user_data.email,
                'old_password': app.user_data.password1,
                'confirmed_password': newpass[1]
                }
        me = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert me['status_code'] == 400

    def test_WHEN_post_me_AND_emptyconf_password_EXPECTED_400TC90360(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        newpass = app.string_generator.get_random_two_passwords_uppercase_lowercase_the_same()
        data = {"email": app.user_data.email,
                'old_password': app.user_data.password1,
                'new_password': newpass[1]
                }
        me = app.api_helper.general_put(app=app, route=app.route.me, data=data)
        assert me['status_code'] == 400

class TestMeProjectsSocialStreaming:
    def test_WHEN_get_me_projects_EXPECTED_response_code_is_200TC__(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        me_project = app.api_helper.general_get(app, route=app.route.me_projects)
        assert me_project['status_code'] == 200

    def test_WHEN_get_me_social_acc_EXPECTED_response_code_is_200TC__(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        social = app.api_helper.general_get(app, route=app.route.me_social_accounts)
        assert social['status_code'] == 200

    def test_WHEN_get_streaming_creadantials_EXPECTED_response_code_is_200TC__(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        me_stream_cred = app.api_helper.general_get(app, route=app.route.me_streaming_credentials)
        assert me_stream_cred['status_code'] == 200

    def test_WHEN_get_streaming_creadantials_EXPECTED_key_and_link_is_not_emptyTC__(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        me_stream_cred = app.api_helper.general_get(app, route=app.route.me_streaming_credentials)
        assert me_stream_cred['url'] != '' and me_stream_cred['token'] != ''

    def test_WHEN_put_streaming_creadantials_EXPECTED_token_is_changedTC__(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        me_stream_cred = app.api_helper.general_get(app, route=app.route.me_streaming_credentials)
        token = me_stream_cred['token']
        me_stream_cred = app.api_helper.general_put(app, route=app.route.me_streaming_credentials, data={})
        assert me_stream_cred['token'] != token





