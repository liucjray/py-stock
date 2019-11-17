import unittest
from Services.emily.TrafficLightStrategyService import *


class TrafficLightStrategyServiceTest(unittest.TestCase):
    dividend = None

    def setUp(self):
        self.service = TrafficLightStrategyService()
        self.twse_price_json = open('html/twse_price.json', 'r', encoding="utf-8", errors='ignore')
        self.price_yearly_html = open('html/FMNPTK.json', 'r', encoding="utf-8", errors='ignore')
        self.price_yearly_html3380 = open('html/FMNPTK3380.json', 'r', encoding="utf-8", errors='ignore')
        self.twse_price_json3380 = open('html/STOCK_DAY_AVG3380.json', 'r', encoding="utf-8", errors='ignore')

    def test_compute(self):
        self.service \
            .set_code(9933) \
            .get_info(self.twse_price_json.read()) \
            .set_price() \
            .set_name() \
            .get_twse_data(self.price_yearly_html.read()) \
            .compute()

    def test_compute3380(self):
        self.service \
            .set_code(3380) \
            .get_info(self.twse_price_json3380.read()) \
            .set_price() \
            .set_name() \
            .get_twse_data(self.price_yearly_html3380.read()) \
            .compute()

    def test_get_price(self):
        print(self.twse_price_json.read())
        exit()
        self.service \
            .set_code(2330) \
            .get_info(self.twse_price_json.read()) \
            .set_price() \
            .set_code(self.twse_price_json.read())
        self.assertEqual("303.50", self.service.price)

    def tearDown(self) -> None:
        self.twse_price_json.close()
        self.price_yearly_html.close()
        self.price_yearly_html3380.close()
        self.twse_price_json3380.close()
