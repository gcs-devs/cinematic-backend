import unittest
from datetime import datetime, timezone
from flask import json
from app import create_app
from unittest import TestCase
from unittest.mock import patch, MagicMock

class HistoryTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()  # Inicializa o app
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()

    @patch('app.views.get_db')
    def test_get_history(self, mock_get_db):
        mock_db = MagicMock()
        mock_get_db.return_value = mock_db
        mock_search_log = MagicMock()
        mock_db.search_log = mock_search_log

        # Simule o retorno do histórico
        mock_search_log.find.return_value = [
        {"_id": MagicMock(), "user": "test_user", "movie_name": "The Two Towers", "result": {"docs": [{"name": "The Two Towers", "runtimeInMinutes": 179}], "total": 1}, "timestamp": datetime.now(timezone.utc)}
        ]
    
        app = create_app()
        client = app.test_client()
    
        response = client.get('/history')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json), 0)

if __name__ == '__main__':
    unittest.main()

