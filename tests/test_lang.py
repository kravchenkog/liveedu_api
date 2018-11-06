import random


class TestLanguage:
    def test_WHEN_language_request_EXPECTED_status_code_200_TC90070(self, app):
        resp = app.api_helper.general_get(app, app.route.languages)
        assert resp['status_code'] == 200

    def test_WHEN_language_request_AND_limit_is_added_EXPECTED_counter_of_el_proper_TC90071(self, app):
        number = 10
        app.env.params = {'limit': number}
        resp = app.api_helper.general_get(app, app.route.languages)
        assert len(resp['results']) == number

    def test_WHEN_language_request_AND_offset_is_added_EXPECTED_counter_of_el_proper_TC90072(self, app):
        offset = 174
        app.env.params = {'offset': offset}
        resp = app.api_helper.general_get(app, app.route.languages)
        assert resp['count'] - offset == len(resp['results'])

    def test_WHEN_language_request_AND_search_is_added_EXPECTED_received_el_proper_TC90073(self, app):
        search = 'Vietnamese'
        app.env.params = {'search': search}
        resp = app.api_helper.general_get(app, app.route.languages)
        for x in resp['results']:
            assert search in x.values()

    def test_WHEN_language_request_AND_order_is_added_EXPECTED_received_sorting_proper_TC90074(self, app):
        order = 'name_en'
        resp = app.api_helper.general_get(app, app.route.languages)
        list_lang = []
        [list_lang.append(x['name_en']) for x in resp['results']]
        list_lang.sort()

        app.env.params = {'ordering': order}
        resp = app.api_helper.general_get(app, app.route.languages)
        ln = []
        [ln.append(x['name_en']) for x in resp['results']]
        for x in range(100):
            assert list_lang[x] == ln[x]

    def test_WHEN_request_iso639_1_is_correct_EXPECTED_response_is_proper_TC90079(self, app):
        random_lang = random.choice(app.api_helper.general_get(app, app.route.languages)['results'])
        app.route.languages_iso = app.route.languages_iso + random_lang['iso_639_1']
        lang_iso = app.api_helper.general_get(app, app.route.languages_iso)
        assert random_lang['name_en'] == lang_iso['name_en']