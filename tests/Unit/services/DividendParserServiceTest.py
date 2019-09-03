import unittest
from Services.DividendParserService import *


class DividendParserServiceTest(unittest.TestCase):
    dividend = None

    def setUp(self):
        self.dividend = DividendParserService('0056')

        fake_html = open('html/0056.html')
        self.dividend.set_html(fake_html.read()).set_bs4()
        fake_html.close()

    def test_get_name(self):
        expect = "0056元大高股息"
        self.assertEqual(expect, self.dividend.get_name())

    def test_get_title(self):
        expect = ['年\u3000度', '現 金 股 利', '盈 餘 配 股', '公 積 配 股', '股 票 股 利', '合\u3000計']
        self.assertEqual(expect, self.dividend.get_title())

    def test_get_data(self):
        expect = [
            ['106', '1.450', '0.000', '0.000', '0.000', '1.450'],
            ['105', '0.950', '0.000', '0.000', '0.000', '0.950'],
            ['104', '1.300', '0.000', '0.000', '0.000', '1.300'],
            ['103', '1.000', '0.000', '0.000', '0.000', '1.000'],
            ['102', '1.000', '0.000', '0.000', '0.000', '1.000'],
            ['101', '0.850', '0.000', '0.000', '0.000', '0.850'],
            ['100', '1.300', '0.000', '0.000', '0.000', '1.300'],
            ['99', '2.200', '0.000', '0.000', '0.000', '2.200'],
            ['97', '2.000', '0.000', '0.000', '0.000', '2.000'],
        ]
        self.assertEqual(expect, self.dividend.get_data())
