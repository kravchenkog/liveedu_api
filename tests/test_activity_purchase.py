import pytest
import random
from time import sleep

class TestActivityPurchase:



    def test_WHEN_activity_EXPECTED_balance_is_increased_properly(self,app, plan):

        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        purchase = app.api_helper.purchase_package(
            app=app,
            plan=plan['id'],
            no_topics=random.randint(1, plan['topic_qty']))
        #sleep(1)
        amount = float(app.api_helper.general_get(app=app, route=app.route.me_balanses_s)['amount'])
        price = amount/100*app.act_price.project_request
        data= {
            'category': app.api_helper.get_random_category_url(app),
            'title': app.string_generator.get_random_string(num=random.randint(20, 100)),
            'difficulty': random.choice([1,2,3]),
            'language': app.api_helper.get_random_language_url(app)
        }
        request = app.api_helper.general_post(app, app.route.projects_suggestions, data)
        newamount = float(app.api_helper.general_get(app=app, route=app.route.me_balanses_s)['amount'])
        print(app.user_data.__dict__)
        assert newamount == amount - price

