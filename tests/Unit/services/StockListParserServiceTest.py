import unittest
from Services.StockListParserService import *


class StockListParserTest(unittest.TestCase):
    dividend = None
    names = []
    codes = []

    def setUp(self):
        self.stock_list = StockListParserService()

        fake_html = open('html/stock_list_all.html', 'r', encoding="Big5", errors='ignore')
        self.stock_list.set_html(fake_html.read()).set_bs4()
        fake_html.close()

    def test_get_code(self):
        self.codes = self.stock_list.get_code()
        expect = ['1101', '1102', '1103', '1104', '1108', '1109', '1110', '1201']
        self.write_file('stock_list_codes', self.codes)
        self.assertEqual(expect, self.codes)

    def test_get_name(self):
        self.names = self.stock_list.get_name()
        expect = ['台泥', '亞泥', '嘉泥', '環泥', '幸福', '信大', '東泥', '味全']
        self.write_file('stock_list_names', self.names)
        self.assertEqual(expect, self.names)

    def test_name_code_count(self):
        self.assertEqual(len(self.names), len(self.codes))

    def write_file(self, file_name, data_list):
        fo = open("{}.txt".format(file_name), "w")
        fo.write(str(data_list).strip('[]'))
        fo.close()
