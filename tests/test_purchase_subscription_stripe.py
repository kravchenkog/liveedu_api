from random import randint
from time import sleep


class TestPostSubscription:
    def test_WHEN_subscr_isnt_purchased_AND_get_subscr_EXPECTED_response_code_is_404_TC90200(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app=app, route=app.route.subscription)
        assert resp['status_code'] == 404

    def test_WHEN_post_subscr_AND_stripe_plus_lpro_EXPECTED_response_code_is_201_TC90201(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        topics =  app.api_helper.get_random_slug_topic(app)
        data = {'plan': 'lpro',
                'service': 'stripe',
                'token': 'tok_visa',
                'topics': [topics]}
        resp = app.api_helper.general_post(app=app, route=app.route.subscription, data=data)
        print(app.user_data.__dict__)
        assert resp['status_code'] == 201
    #
    def test_WHEN_post_subscr_AND_stripe_plus_lpro_EXPECTED_not_is_failing_TC90202(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        topics =  app.api_helper.get_random_slug_topic(app)
        data = {'plan': 'lpro',
                'service': 'stripe',
                'token': 'tok_visa',
                'topics': [topics]}
        resp = app.api_helper.general_post(app=app, route=app.route.subscription, data=data)
        assert not resp['is_failing']

    def test_WHEN_post_subscr_AND_topics_more_than_possible_EXPECTED_is_not(self, app, plan):
        #TC[90203, 90204, 90205, 90206]

        if plan['id'] == 'lprotall' or plan['id'] == 'lpro12tall':
            return
        range_from= plan['topic_qty']+1
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        puerchasing = app.api_helper.purchase_package(
            app, plan=plan['id'], no_topics=randint(range_from, 10))
        assert puerchasing['status_code'] == 400


class TestMeAfterPurchase:
    def test_WHEN_user_is_registered_AND_me_EXPECTED_package_is_free_TC90220(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert resp['plan']['id'] == 'free'

    def test_WHEN_package_is_free_AND_me_EXPECTED_is_premium_is_false_TC90221(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert not resp['is_premium']

    def test_WHEN_subscr_is_purchased_EXPECTED_me_package_id_is_proper(self, app, plan):
        # TC[90222, 90223, 90224, 90225, 90226, 90227]
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name=plan['id'])

        resp = app.api_helper.general_get(app=app, route=app.route.me)
        print(app.user_data.__dict__)
        assert purchase['status_code'] == 201
        assert resp['plan']['id'] == my_plan['id']


class TestTRansactionAfterPurchase():

    def test_WHEN_subsc_is_purchased_EXPECTED_ledu_balance_is_proper(self, app, plan):
        #TC[90240, 90242, 90243, 90244, 90245, 90246]
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name=plan['id'])
        sleep(1.5)
        last_transaction = app.api_helper.general_get(app=app, route=app.route.transaction_ledu)['data'].pop()
        my_plan_after = app.api_helper.get_plan(app=app, plan=plan['id'])
        print(app.user_data.__dict__)
        assert purchase['status_code'] == 201
        assert last_transaction['amount'] == my_plan['price_ledu'] or\
               last_transaction['amount'] == my_plan_after['price_ledu']



    def test_WHEN_subsc_is_purchased_EXPECTED_usd_balance_is_properTC90241(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lpro12t3')
        sleep(1.5)

        last_transaction = app.api_helper.general_get(app=app, route=app.route.transaction_ledu)['data'].pop()
        print(app.user_data.__dict__)
        assert purchase['status_code'] == 201
        assert last_transaction['amount_usd'] + " USD" == my_plan['price']
        AssertionError(print(my_plan))


