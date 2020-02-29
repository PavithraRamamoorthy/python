import unittest
import requests

class Test(unittest.TestCase):
    def setup(self):
        self.base_url="http://www.google.com"

    def test_response_status(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)

unittest.main()
