import unittest
from Services.RequestProxyService import *


class RequestProxyServiceTest(unittest.TestCase):
    html = None

    def setUp(self):
        self.proxy = RequestProxyService()
        with open('html/free-proxy-list.net.html', encoding="utf-8") as fake_html:
            self.html = fake_html.read()
            fake_html.close()

    def test_parse_proxies(self):
        all_proxies = self.proxy.parse_proxies(self.html)
        all_https_proxies = self.proxy.parse_proxies(self.html, 'yes')
        all_http_proxies = self.proxy.parse_proxies(self.html, 'no')
        self.assertIsInstance(all_proxies, list)
        self.assertIsInstance(all_https_proxies, list)
        self.assertIsInstance(all_http_proxies, list)
