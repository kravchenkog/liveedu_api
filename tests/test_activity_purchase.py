import random
from time import sleep
import datetime

class TestActivityPurchase:



    # def test_WHEN_activity_EXPECTED_balance_is_increased_properly(self,app, plan):
    #
    #     app.user_data = app.api_helper.get_registered_and_logged_user(app)
    #     purchase = app.api_helper.purchase_package(
    #         app=app,
    #         plan=plan['id'],
    #         no_topics=random.randint(1, plan['topic_qty']))
    #     current_time = datetime.datetime.now()
    #     amount = float(app.api_helper.general_get(app=app, route=app.route.me_balanses_s)['amount'])
    #     retry_count = 0
    #     while not amount and retry_count < 5:
    #         amount = float(app.api_helper.general_get(app=app, route=app.route.me_balanses_s)['amount'])
    #         sleep(1)
    #         retry_count += 1
    #     duration = datetime.datetime.now() - current_time
    #     price = amount/100*app.act_price.project_request
    #     data= {
    #         'category': app.api_helper.get_random_category_url(app),
    #         'title': app.string_generator.get_random_string(num=random.randint(20, 100)),
    #         'difficulty': random.choice([1,2,3]),
    #         'language': app.api_helper.get_random_language_url(app)
    #     }
    #     request = app.api_helper.general_post(app, app.route.projects_suggestions, data)
    #     newamount = float(app.api_helper.general_get(app=app, route=app.route.me_balanses_s)['amount'])
    #     print(app.user_data.__dict__)
    #     print("data updete during: " + str(duration.total_seconds()))
    #     assert newamount == amount - price


    def test_WHEN_ledu_ended_EXPECTED_10persent_is_added_tobalance(self,app, plan):

        app.user_data = app.api_helper.get_registered_and_logged_user(app)
        purchase = app.api_helper.purchase_package(
            app=app,
            plan=plan['id'],
            no_topics=random.randint(1, plan['topic_qty']))
        current_time = datetime.datetime.now()
        amount = float(app.api_helper.general_get(app=app, route=app.route.me_balanses_s)['amount'])
        retry_count = 0
        while not amount and retry_count < 20:

            amount = float(app.api_helper.general_get(app=app, route=app.route.me_balanses_s)['amount'])
            sleep(1)
            retry_count += 1
        duration = datetime.datetime.now() - current_time
        price = amount/100*app.act_price.project_request
        data= {
            'category': app.api_helper.get_random_category_url(app),
            'title': app.string_generator.get_random_string(num=random.randint(20, 100)),
            'difficulty': random.choice([1,2,3]),
            'language': app.api_helper.get_random_language_url(app)
        }

        if amount:
            request = app.api_helper.general_post(app, app.route.projects_suggestions, data)
            newamount = float(app.api_helper.general_get(app=app, route=app.route.me_balanses_s)['amount'])
            count = 0
            while newamount < amount/100*3:
                count+=1
                print("newamount = " + str(newamount))
                request = app.api_helper.general_post(app, app.route.projects_suggestions, data)
                newamount = float(app.api_helper.general_get(app=app, route=app.route.me_balanses_s)['amount'])
            lastamount = float(app.api_helper.general_get(app=app, route=app.route.me_balanses_s)['amount'])
            print(app.user_data.__dict__)
            print("data updete during: " + str(duration.total_seconds()))
            assert newamount == amount - price and newamount != 0
        else:
            raise AssertionError('Reason: amount=%s' % amount)


