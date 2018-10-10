import random






class TestTopic:
    def test_WHEN_get_topic_EXPECTED_response_code_is_200_TC90080(self, app):
        resp = app.api_helper.general_get(app, route=app.route.topics)
        assert resp['status_code'] == 200

    def test_WHEN_get_topic_AND_limit_is_add_EXPECTED_number_of_el_proper_TC90081(self, app):
        limit = 3
        app.env.params = {'limit': limit}
        resp = app.api_helper.general_get(app, route=app.route.topics)
        assert len(resp['results']) == limit

    def test_WHEN_get_topic_AND_offset_is_added_EXPECTED_number_of_el_proper_TC90082(self, app):
        offset = 3

        resp = app.api_helper.general_get(app, route=app.route.topics)
        list_len = len(resp['results'])
        app.env.params = {'offset': offset}
        resp2 = app.api_helper.general_get(app, route=app.route.topics)
        assert list_len - offset == len(resp2['results'])

    def test_WHEN_get_topic_AND_search_is_added_EXPECTED_result_is_correct_TC90083(self, app):
        search = 'crypto'
        app.env.params = {'search': search}
        resp = app.api_helper.general_get(app, route=app.route.topics)
        for x in resp['results']:
            assert search in x['slug']

    def test_WHEN_get_topic_AND_ordering_is_added_EXPECTED_sorting_is_proper_TC90084(self, app):
        ordering = 'slug'

        resp = app.api_helper.general_get(app, route=app.route.topics)
        list_top = []
        [list_top.append(x['slug']) for x in resp['results']]
        list_top.sort()
        app.env.params = {'ordering': ordering}
        resp2 = app.api_helper.general_get(app, route=app.route.topics)
        list_top_or = []
        [list_top_or.append(x['slug']) for x in resp2['results']]

        for x in range(0, len(list_top_or)-1):
            assert list_top[x] == list_top_or[x]

    def test_WHEN_get_topic_AND_slug_is_added_EXPECTED_response_is_correct_TC90085(self, app):

        random_slug = app.api_helper.get_random_slug_topic(app)
        app.route.topics = app.route.topics + random_slug
        resp_sl = app.api_helper.general_get(app, route=app.route.topics)
        assert resp_sl['slug'] == random_slug

class TestTopicsCategories:
    def test_WHEN_get_categories_by_topic_EXPECTED_status_code_is_200_TC90086(self, app):

        random_slug = app.api_helper.get_random_slug_topic(app)
        app.route.topics = app.route.topics + random_slug + '/categories'
        resp_cat = app.api_helper.general_get(app, route=app.route.topics)
        assert resp_cat['status_code'] == 200

    def test_WHEN_get_categories_by_topic_EXPECTED_all_categories_from_topic_TC90087(self, app):

        random_slug = app.api_helper.get_random_slug_topic(app)
        app.route.topics = app.route.topics + random_slug + '/categories'
        resp_cat = app.api_helper.general_get(app, route=app.route.topics)
        for x in resp_cat['results']:
            assert x['topic']['slug'] == random_slug

    def test_WHEN_get_categories_by_topic_AND_limit_EXPECTED_count_is_correct_TC90088(self, app):
        limit = 5
        random_topic_slug = random.choice(
            app.api_helper.general_get(app, route=app.route.topics)['results'])['slug']
        app.route.topics = app.route.topics + random_topic_slug + '/categories'
        app.env.params = {'limit': limit}
        resp_lim = app.api_helper.general_get(app, route=app.route.topics)
        assert len(resp_lim['results']) == limit

    def test_WHEN_get_categories_by_topic_AND_search_EXPECTED_search_res_is_correct_TC90089(self, app):
        random_topic_slug = random.choice(
            app.api_helper.general_get(app, route=app.route.topics)['results'])['slug']
        app.route.topics = app.route.topics + random_topic_slug + '/categories'
        categories_by_slug = app.api_helper.general_get(app, route=app.route.topics)
        random_cat_name = random.choice(categories_by_slug['results'])['name']
        app.env.params = {'search': random_cat_name}
        response = app.api_helper.general_get(app, route=app.route.topics)
        assert len(response['results']) > 0
        for x in range(0, len(response['results'])-1):
            assert random_cat_name in response['results'][x]['name']

    def test_WHEN_get_categories_by_topic_AND_ordering_EXPECTED_sorting_is_correct_TC90090(self, app):

        random_topic_slug = random.choice(
            app.api_helper.general_get(app, route=app.route.topics)['results'])['slug']
        app.route.topics = app.route.topics + random_topic_slug + '/categories'
        categories_by_slug = app.api_helper.general_get(app, route=app.route.topics)
        list_of_cat_slag = []
        [list_of_cat_slag.append(x['slug']) for x in categories_by_slug['results']]
        list_of_cat_slag.sort()
        app.env.params = {'ordering': 'slug'}
        categories_by_order = app.api_helper.general_get(app, route=app.route.topics)
        list_order = []
        [list_order.append(x['slug']) for x in categories_by_order['results']]
        for x in range(0, len(list_order)-1):
            assert list_order[x] == list_of_cat_slag[x]

class TestTopicsHieracly:
    def test_WHEN_get_topic_hierarchy_EXPECTED_status_code_200_TC90095(self, app):
        response = app.api_helper.general_get(app, route=app.route.topic_hierarchy)
        assert response['status_code'] == 200

    def test_WHEN_get_topic_hierarchy_AND_limit_EXPECTED_status_code_200_TC90096(self, app):
        limit = 3

        app.env.params = {'limit': limit}
        response = app.api_helper.general_get(app, route=app.route.topic_hierarchy)
        assert len(response['results']) == limit

    def test_WHEN_get_topic_hierarchy_AND_random_offser_EXPECTED_results_are_correct_TC90097(self, app):
        resp1 = app.api_helper.general_get(app, route=app.route.topic_hierarchy)
        random_offset_no = random.randint(0, len(resp1['results'])-1)
        app.env.params = {'offset': random_offset_no}
        resp2 = app.api_helper.general_get(app, route=app.route.topic_hierarchy)
        assert len(resp2['results']) + random_offset_no == len(resp1['results'])

    def test_WHEN_get_topic_hierarchy_AND_random_search_EXPECTED_search_res_are_correct_TC90098(self, app):
        resp1 = app.api_helper.general_get(app, route=app.route.topic_hierarchy)
        random_name = random.choice(resp1['results'])['name']
        app.env.params = {'search': random_name}
        resp12 = app.api_helper.general_get(app, route=app.route.topic_hierarchy)
        assert resp12['results']
        received_name = resp12['results'][0]['name']
        assert received_name == random_name

    def test_WHEN_get_topic_hierarchy_AND_ordering_by_name_EXPECTED_sorting_is_correct_TC90099(self, app):
        resp1 = app.api_helper.general_get(app, route=app.route.topic_hierarchy)
        manual_ord = sorted([x['name'] for x in resp1['results']])
        random_name = random.choice(resp1['results'])['name']
        app.env.params = {'ordering': 'name'}
        resp2 = app.api_helper.general_get(app, route=app.route.topic_hierarchy)
        for x in range(0, len(resp2)-1):
            assert manual_ord[x] == resp2['results'][x]['name']

    def test_WHEN_get_topic_hieracly_by_slug_EXPECTED_received_topic_is_correct_TC90100(self, app):
        random_slug = app.api_helper.get_random_slug_topic(app)
        app.route.topic_hierarchy = app.route.topic_hierarchy+random_slug
        resp = app.api_helper.general_get(app, route=app.route.topic_hierarchy)
        assert resp['slug'] == random_slug

    






