import unittest
from Services.TWSEService import *


class TWSEServiceTest(unittest.TestCase):
    twse, json = None, None

    def setUp(self):
        self.twse = TWSEService()
        with open('json/stock_day_avg.json', encoding="utf-8") as fake_json:
            self.json = fake_json.read()
            fake_json.close()

    def test_parse_stock_name(self):
        actual = self.twse.parse_name(self.json)
        self.assertEqual('新光金', actual)

    def test_parse_price(self):
        actual = self.twse.parse_price(self.json)
        self.assertEqual('10.10', actual)
