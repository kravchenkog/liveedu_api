from fixture.app_manager import AppManager
from random import randint



def purchasing():
    app = AppManager()

    my_plan = app.api_helper.get_plan(app, "lprot3")
    range_from = my_plan['topic_qty']
    app.user_data = app.api_helper.get_registered_and_logged_user(app)
    puerchasing = app.api_helper.purchase_package_ledu(
        app, plan=my_plan['id'], no_topics=range_from)
    print(app.user_data.__dict__)
    print(puerchasing)

    resp = app.api_helper.general_get(app=app, route=app.route.me)




if __name__=="__main__":
    purchasing()

