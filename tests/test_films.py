import datetime
import http
from dataclasses import dataclass
from unittest.mock import patch
import json

from src import app


@dataclass
class FakeFilm:
    title = 'Fake Film'
    distributed_by = 'Fake'
    release_date = datetime.datetime.now()
    description = 'Fake description'
    length = 100
    rating = 8.0


class TestFilms(object):
    uuid = []

    def test_get_films_with_db(self):
        client = app.test_client()
        resp = client.get('/films')
        assert resp.status_code == http.HTTPStatus.OK

    @patch('src.services.film.FilmService.fetch_all', autospec=True)
    def test_get_films_mock_db(self, mock_db_call):
        client = app.test_client()
        resp = client.get('/films')
        mock_db_call.assert_called_once()
        assert resp.status_code == http.HTTPStatus.OK
        assert not len(resp.json)

    def test_create_film_with_db(self):
        client = app.test_client()
        data = {
            'title': 'Test Title',
            'distributed_by': 'Test Company',
            'release_date': '2010-04-01',
            'description': '',
            'length': 100,
            'rating': 8.0
        }
        resp = client.post('/films', data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.CREATED
        assert resp.json['title'] == 'Test Title'
        self.uuid.append(resp.json['uuid'])

    def test_create_film_with_mock_db(self):
        with patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            client = app.test_client()
            data = {
                'title': 'Test Title',
                'distributed_by': 'Test Company',
                'release_date': '2010-04-01',
                'description': '',
                'length': 100,
                'rating': 8.0
            }
            resp = client.post('/films', data=json.dumps(data), content_type='application/json')
            assert resp.status_code == http.HTTPStatus.CREATED
            assert resp.json['title'] == 'Test Title'
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()

    def test_get_film_with_db(self):
        client = app.test_client()
        url = f'/films/{self.uuid[0]}'
        resp = client.get(url)
        assert resp.status_code == http.HTTPStatus.OK
        assert resp.json['title'] == 'Test Title'

    @patch('src.services.film.FilmService.find_by_uuid', autospec=True, return_value=FakeFilm())
    def test_get_film_with_mock(self, mock_db_call):
        client = app.test_client()
        resp = client.get('/films/1')
        assert resp.status_code == http.HTTPStatus.OK
        assert resp.json['title'] == 'Fake Film'
        mock_db_call.assert_called_once()

    def test_update_film_with_db(self):
        client = app.test_client()
        url = f'/films/{self.uuid[0]}'
        data = {
            'title': 'Update Title',
            'distributed_by': 'update',
            'release_date': '2010-04-01'
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.OK
        assert resp.json['title'] == 'Update Title'

    def test_update_film_with_mock_db(self):
        with patch('src.services.film.FilmService.find_by_uuid') as mocked_query, \
                patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            mocked_query.return_value = FakeFilm()
            client = app.test_client()
            url = f'/films/1'
            data = {
                'title': 'Update Title',
                'distributed_by': 'update',
                'release_date': '2010-04-01'
            }
            resp = client.put(url, data=json.dumps(data), content_type='application/json')
            assert resp.status_code == http.HTTPStatus.OK
            assert resp.json['title'] == 'Update Title'
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()

    def test_delete_film_with_db(self):
        client = app.test_client()
        url = f'/films/{self.uuid[0]}'
        resp = client.delete(url)
        assert resp.status_code == http.HTTPStatus.NO_CONTENT
