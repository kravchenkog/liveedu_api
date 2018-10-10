from random import randint
from time import sleep


class TestPostSubscription:
    def test_WHEN_subscr_isnt_purchased_AND_get_subscr_EXPECTED_response_code_is_400_TC___(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app=app, route=app.route.subscription)
        assert resp['status_code'] == 404

    def test_WHEN_post_subscr_AND_stripe_plus_lpro_EXPECTED_response_code_is_201_TC___(self, app):
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
    def test_WHEN_post_subscr_AND_stripe_plus_lpro_EXPECTED_not_is_failing_TC___(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        topics =  app.api_helper.get_random_slug_topic(app)
        data = {'plan': 'lpro',
                'service': 'stripe',
                'token': 'tok_visa',
                'topics': [topics]}
        resp = app.api_helper.general_post(app=app, route=app.route.subscription, data=data)
        assert not resp['is_failing']

    def test_WHEN_post_subscr1_AND_topics_more_than_possible_EXPECTED_is_not_TC___(self, app):

        my_plan = app.api_helper.get_plan(app, "lpro")
        range_from= my_plan['topic_qty']+1
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        puerchasing = app.api_helper.purchase_package(
            app, plan=my_plan['id'], no_topics=randint(range_from, 10))
        assert puerchasing['status_code'] != 201

    def test_WHEN_post_subscr2_AND_topics_more_than_possible_EXPECTED_is_not_TC___(self, app):
        my_plan = app.api_helper.get_plan(app, "lpro12")
        range_from= my_plan['topic_qty']+1
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        puerchasing = app.api_helper.purchase_package(
            app, plan=my_plan['id'], no_topics=randint(range_from, 10))
        assert puerchasing['status_code'] != 201

    def test_WHEN_post_subscr5_AND_topics_more_than_possible_EXPECTED_is_not_TC___(self, app):
        my_plan = app.api_helper.get_plan(app, "lprot3")
        range_from= my_plan['topic_qty']+1
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        puerchasing = app.api_helper.purchase_package(
            app, plan=my_plan['id'], no_topics=randint(range_from, 10))
        assert puerchasing['status_code'] != 201

    def test_WHEN_post_subscr6_AND_topics_more_than_possible_EXPECTED_is_not_TC___(self, app):
        my_plan = app.api_helper.get_plan(app, "lpro12t3")
        range_from= my_plan['topic_qty']+1
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        puerchasing = app.api_helper.purchase_package(
            app, plan=my_plan['id'], no_topics=randint(range_from, 10))
        assert puerchasing['status_code'] != 201

class TestMeAfterPurchase:
    def test_WHEN_user_is_registered_AND_me_EXPECTED_package_is_free_TC___(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert resp['plan']['id'] == 'free'

    def test_WHEN_package_is_free_AND_me_EXPECTED_is_premium_is_false_TC___(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert not resp['is_premium']

    def test_WHEN_subscription_0_is_purchased_EXPECTED_me_package_id_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lprotall')
        #sleep(1.5)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert purchase['status_code'] == 201
        assert resp['plan']['id'] == my_plan['id']

    def test_WHEN_subscription_1_is_purchased_EXPECTED_me_package_id_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lpro12tall')
        #sleep(1.5)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert purchase['status_code'] == 201
        assert resp['plan']['id'] == my_plan['id']

    def test_WHEN_subscription_2_is_purchased_EXPECTED_me_package_id_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lpro')
        #sleep(1.5)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert purchase['status_code'] == 201
        assert resp['plan']['id'] == my_plan['id']

    def test_WHEN_subscription_3_is_purchased_EXPECTED_me_package_id_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lpro12')
        #sleep(1.5)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert purchase['status_code'] == 201
        assert resp['plan']['id'] == my_plan['id']

    def test_WHEN_subscription_4_is_purchased_EXPECTED_me_package_id_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lprot3')
        #sleep(1.5)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert purchase['status_code'] == 201
        assert resp['plan']['id'] == my_plan['id']

    def test_WHEN_subscription_5_is_purchased_EXPECTED_me_package_id_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lpro12t3')
        #sleep(1.5)
        resp = app.api_helper.general_get(app=app, route=app.route.me)
        assert purchase['status_code'] == 201
        assert resp['plan']['id'] == my_plan['id']



class TestTRansactionAfterPurchase():

    def test_WHEN_subsc_is_purchased_EXPECTED_ledu_balance_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lpro12t3')
        #sleep(1.5)
        last_transaction = app.api_helper.general_get(app=app, route=app.route.transaction_ledu)['data'].pop()
        print(app.user_data.__dict__)
        assert purchase['status_code'] == 201
        assert last_transaction['amount'] == my_plan['price_ledu']


    def test_WHEN_subsc_is_purchased_EXPECTED_usd_balance_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lpro12t3')
        #sleep(1.5)
        last_transaction = app.api_helper.general_get(app=app, route=app.route.transaction_ledu)['data'].pop()
        print(app.user_data.__dict__)
        assert purchase['status_code'] == 201
        assert last_transaction['amount_usd'] + " USD" == my_plan['price']

    def test_WHEN_subsc2_is_purchased_EXPECTED_ledu_balance_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lprotall')

        #sleep(1.5)
        last_transaction = app.api_helper.general_get(app=app, route=app.route.transaction_ledu)['data'].pop()
        print(app.user_data.__dict__)
        assert purchase['status_code'] == 201
        assert last_transaction['amount'] == my_plan['price_ledu']

    def test_WHEN_subsc3_is_purchased_EXPECTED_ledu_balance_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lpro12tall')
        #sleep(1.5)
        last_transaction = app.api_helper.general_get(app=app, route=app.route.transaction_ledu)['data'].pop()
        print(app.user_data.__dict__)
        assert purchase['status_code'] == 201
        assert last_transaction['amount'] == my_plan['price_ledu']

    def test_WHEN_subsc4_is_purchased_EXPECTED_ledu_balance_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lpro')
        #sleep(1.5)
        last_transaction = app.api_helper.general_get(app=app, route=app.route.transaction_ledu)['data'].pop()
        print(app.user_data.__dict__)
        assert purchase['status_code'] == 201
        assert last_transaction['amount'] == my_plan['price_ledu']

    def test_WHEN_subsc5_is_purchased_EXPECTED_ledu_balance_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lpro12')
        #sleep(1.5)
        last_transaction = app.api_helper.general_get(app=app, route=app.route.transaction_ledu)['data'].pop()
        print(app.user_data.__dict__)
        assert purchase['status_code'] == 201
        assert last_transaction['amount'] == my_plan['price_ledu']


    def test_WHEN_subsc6_is_purchased_EXPECTED_ledu_balance_is_proper(self, app):
        my_plan, purchase = app.api_helper.register_user_and_purchaqse_subs(app=app, plan_name='lprot3')
        #sleep(1.5)
        last_transaction = app.api_helper.general_get(app=app, route=app.route.transaction_ledu)['data'].pop()
        print(app.user_data.__dict__)
        assert purchase['status_code'] == 201
        assert last_transaction['amount'] == my_plan['price_ledu']
