import unittest
from app import app

class TestDemo(unittest.TestCase):
    def test_web_ok(self):
        client = app.test_client()
        res = client.get("/")
        self.assertEqual(res.status_code,200)

if __name__ == '__main__':
    unittest.main()