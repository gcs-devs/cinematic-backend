import unittest
from app import create_app, get_db
from datetime import datetime, timezone

class IntegrationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_config = {
            "MONGO_URI": "mongodb://mongo:27017/test_database"
        }
        cls.app = create_app(test_config)
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            cls.db = get_db()
            cls.db.search_log.drop()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            cls.db.search_log.drop()

    def test_successful_movie_search(self):
        response = self.client.post('/movies', json={
            'user': 'test_user',
            'movie': 'The Matrix'
        })
        self.assertEqual(response.status_code, 200)

    def test_get_history(self):
        with self.app.app_context():
            self.db.search_log.insert_one({
                'user': 'test_user',
                'movie': 'The Matrix',
                'timestamp': datetime.now(timezone.utc)
            })
        response = self.client.get('/history')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['movie'], 'The Matrix')

if __name__ == '__main__':
    unittest.main()

