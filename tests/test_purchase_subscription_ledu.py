import math


class TestCheckPlan_vs_Subscription:
    def test_WHEN_subscriptionLEDU_AND_get_plan_lprot3_EXPECTED_price_is_the_same_TC90250(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        plan = app.api_helper.get_plan(app, "lprot3")
        subscr = app.api_helper.purchase_package_ledu(app, "lprot3", 3)
        price = float(plan['price_ledu'])*float(plan['minimal_period_crypto'])\
               /100*(100-float(plan['ledu_payment_discount_percent']))
        print(price)
        assert subscr['amount'] == round(price)

    def test_WHEN_subscriptionLEDU_AND_get_plan_lprotall_EXPECTED_price_is_the_same_TC90251(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        plan = app.api_helper.get_plan(app, "lprotall")
        subscr = app.api_helper.purchase_package_ledu(app, "lprotall", 3)
        price = float(plan['price_ledu'])*float(plan['minimal_period_crypto'])\
               /100*(100-float(plan['ledu_payment_discount_percent']))
        print(price)
        assert subscr['amount'] == round(price)

    def test_WHEN_subscriptionLEDU_AND_get_plan_lpro12talll_EXPECTED_price_is_the_same_TC90252(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        plan = app.api_helper.get_plan(app, "lpro12tall")
        subscr = app.api_helper.purchase_package_ledu(app, "lpro12tall", 3)
        price = float(plan['price_ledu']) * float(plan['minimal_period_crypto']) \
                / 100 * (100 - float(plan['ledu_payment_discount_percent']))
        print(price)
        assert subscr['amount'] == round(price)

    def test_WHEN_subscriptionLEDU_AND_get_plan_lpro_EXPECTED_price_is_the_same_TC90253(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        plan = app.api_helper.get_plan(app, "lpro")
        subscr = app.api_helper.purchase_package_ledu(app, "lpro", 1)
        price = float(plan['price_ledu']) * float(plan['minimal_period_crypto']) \
                / 100 * (100 - float(plan['ledu_payment_discount_percent']))
        print(price)
        assert subscr['amount'] == round(price)

    def test_WHEN_subscriptionLEDU_AND_get_plan_lpro12_EXPECTED_price_is_the_same_TC90254(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        plan = app.api_helper.get_plan(app, "lpro12")
        subscr = app.api_helper.purchase_package_ledu(app, "lpro12", 1)
        price = float(plan['price_ledu']) * float(plan['minimal_period_crypto']) \
                / 100 * (100 - float(plan['ledu_payment_discount_percent']))
        print(price)
        assert subscr['amount'] == round(price)

    def test_WHEN_subscriptionLEDU_AND_get_plan_lpro12t3_EXPECTED_price_is_the_same_TC902550(self, app):
        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        plan = app.api_helper.get_plan(app, "lpro12t3")
        subscr = app.api_helper.purchase_package_ledu(app, "lpro12t3", 3)
        price = float(plan['price_ledu']) * float(plan['minimal_period_crypto']) \
                / 100 * (100 - float(plan['ledu_payment_discount_percent']))
        print(price)
        assert subscr['amount'] == round(price)