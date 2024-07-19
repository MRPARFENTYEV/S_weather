# from weather_info import views
import requests
import requests_mock
import unittest
from unittest.mock import patch

def get_external_ip(): # Вычислить ip
    response = requests.get('https://api.ipify.org?format=json')
    external_ip = response.json()['ip']
    return external_ip

class TestGetExternalIp(unittest.TestCase):
    @requests_mock.Mocker()
    def test_get_external_ip(self, mock_request):
        expected_ip = '123.123.123.123'
        mock_request.get('https://api.ipify.org?format=json', json={'ip': expected_ip})

        actual_ip = get_external_ip()
        self.assertEqual(actual_ip, expected_ip)

if __name__ == '__main__':
    unittest.main()