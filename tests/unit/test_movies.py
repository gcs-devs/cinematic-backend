from unittest import TestCase
from unittest.mock import patch, MagicMock, ANY
import json
from app import create_app

class MoviesTestCase(TestCase):
    @patch('app.views.get_db')
    def test_invalid_data(self, mock_get_db):
        # Cria um mock para o banco de dados e o `search_log`
        mock_db = MagicMock()
        mock_get_db.return_value = mock_db
        mock_search_log = MagicMock()
        mock_db.search_log = mock_search_log

        # Configura o mock para simular uma falha de busca
        mock_search_log.insert_one.side_effect = Exception("Simulated insertion error")

        app = create_app()
        client = app.test_client()

        response = client.post('/movies', json={'user': 'test_user', 'movie': 'The Two Towers'})
        self.assertEqual(response.status_code, 500)
        self.assertIn('error', response.json)

    @patch('app.views.get_db')
    def test_missing_movie(self, mock_get_db):
        # Cria um mock para o banco de dados e o `search_log`
        mock_db = MagicMock()
        mock_get_db.return_value = mock_db
        mock_search_log = MagicMock()
        mock_db.search_log = mock_search_log

        # Configura o mock para simular uma falha de busca
        mock_search_log.insert_one.return_value = None

        app = create_app()
        client = app.test_client()

        response = client.post('/movies', json={'user': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    @patch('app.views.get_db')
    def test_missing_user(self, mock_get_db):
        # Cria um mock para o banco de dados e o `search_log`
        mock_db = MagicMock()
        mock_get_db.return_value = mock_db
        mock_search_log = MagicMock()
        mock_db.search_log = mock_search_log

        # Configura o mock para simular uma falha de busca
        mock_search_log.insert_one.return_value = None

        app = create_app()
        client = app.test_client()

        response = client.post('/movies', json={'movie': 'The Two Towers'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()

