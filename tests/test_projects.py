import random
import pytest
class TestTopic:
    def test_WHEN_get_projects_EXPECTED_response_code_is_200_TC90110(self, app):
        resp = app.api_helper.general_get(app, route=app.route.projects)
        assert resp['status_code'] == 200

    def test_WHEN_get_projects_AND_limit_EXPECTED_number_of_projects_are_correct_TC90111(self, app):
        random_limit = random.randint(0, 100)
        app.env.params = {'limit': random_limit}
        resp = app.api_helper.general_get(app, route=app.route.projects)['results']
        assert len(resp) == random_limit

    def test_WHEN_get_projects_AND_offset_EXPECTED_number_of_projects_are_correct_TC90112(self, app):
        full_resp = app.api_helper.general_get(app, route=app.route.projects)
        app.env.params = {'limit': full_resp['count']}
        random_offset = random.randint(0, full_resp['count'])
        app.env.params['offset'] = random_offset
        resp = app.api_helper.general_get(app, route=app.route.projects)['results']
        assert len(resp) + random_offset == full_resp['count']


class TestCreateProject:
    @pytest.fixture(autouse=True)
    def _streamer(self, app_streamer):
        self.app_streamer = app_streamer


    def test_WHEN_post_projects_AND_all_required_filled_EXPECTED_response_code_is_200(self):
        app = self.app_streamer
        data = {
            'title': app.string_generator.get_random_string(random.randint(30, 100)),
            'category': app.api_helper.get_random_category_url(app=app),
            'difficulty': random.choice([1, 2, 3]),
            'language': app.api_helper.get_random_language_url(app)
        }
        resp = app.api_helper.general_post(app, app.route.projects, data)

        assert resp['status_code'] == 201, "test failed"

    def test_WHEN_post_projects_AND_get_project_by_url_EXPECTED_status_code_200(self):
        app = self.app_streamer
        title = app.string_generator.get_random_string(random.randint(30, 100))
        data = {
            'title': title,
            'category': app.api_helper.get_random_category_url(app=app),
            'difficulty': random.choice([1, 2, 3]),
            'language': app.api_helper.get_random_language_url(app)
        }
        create = app.api_helper.general_post(app, app.route.projects, data)
        my_proj = app.api_helper.general_get(app, url=create['url'])

        assert my_proj['status_code'] == 200

    def test_WHEN_post_projects_AND_get_project_by_url_EXPECTED_title_is_proper(self):
        app = self.app_streamer
        title = app.string_generator.get_random_string(random.randint(30, 100))
        data = {
            'title': title,
            'category': app.api_helper.get_random_category_url(app=app),
            'difficulty': random.choice([1, 2, 3]),
            'language': app.api_helper.get_random_language_url(app)
        }
        create = app.api_helper.general_post(app, app.route.projects, data)
        my_proj = app.api_helper.general_get(app, url=create['url'])

        assert my_proj['title'] == title

    def test_WHEN_post_projects_AND_get_project_by_url_EXPECTED_language_is_proper(self):
        app = self.app_streamer
        language = app.api_helper.get_random_language_url(app)
        title = app.string_generator.get_random_string(random.randint(30, 100))
        data = {
            'title': title,
            'category': app.api_helper.get_random_category_url(app=app),
            'difficulty': random.choice([1, 2, 3]),
            'language': language
        }
        create = app.api_helper.general_post(app, app.route.projects, data)
        my_proj = app.api_helper.general_get(app, url=create['url'])

        assert my_proj['language']['url'] == language

    def test_WHEN_post_projects_AND_get_project_by_url_EXPECTED_category_is_proper(self):
        app = self.app_streamer
        language = app.api_helper.get_random_language_url(app)
        category = app.api_helper.get_random_category_url(app=app)
        title = app.string_generator.get_random_string(random.randint(30, 100))
        data = {
            'title': title,
            'category': category,
            'difficulty': random.choice([1, 2, 3]),
            'language': language
        }
        create = app.api_helper.general_post(app, app.route.projects, data)
        my_proj = app.api_helper.general_get(app, url=create['url'])

        assert my_proj['category']['url'] == category

