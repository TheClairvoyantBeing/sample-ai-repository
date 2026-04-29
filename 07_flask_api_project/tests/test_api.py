import unittest
import json
from app import create_app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_health_check(self):
        response = self.client.get('/api/health')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'healthy')

    def test_echo(self):
        payload = {'message': 'Hello AI'}
        response = self.client.post(
            '/api/echo',
            data=json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['received'], 'Hello AI')

if __name__ == '__main__':
    unittest.main()
