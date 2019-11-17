from urllib.parse import urlencode
import requests
import json
import re
from Services.RequestProxyService import *


class TWSEService:
    code, data, info = None, None, None
    url = 'https://www.twse.com.tw'
    req = RequestProxyService()

    def __init__(self):
        pass

    def set_code(self, code):
        self.code = code
        return self

    def get_endpoint(self, node, params):
        url = self.url + node + '?' + urlencode(params)
        return url

    def price_format(self, price):
        return "{:.2f}".format(float(price))

    def get_info(self, p_json=None):
        # print('get_info')
        node = "/exchangeReport/STOCK_DAY_AVG"
        params = {'response': 'json', 'stockNo': self.code}
        if p_json is None:
            resp = self.req.get(self.get_endpoint(node, params))
            if hasattr(resp, 'text'):
                p_json = resp.text
            else:
                raise ValueError('get_info failed.')
        self.info = {
            'name': self.parse_name(p_json),
            'price': self.price_format(self.parse_price(p_json)),
        }
        return self

    def parse_price(self, input_json):
        j = json.loads(input_json)
        price = self.price_format(j['data'][-2][1])
        return price

    def parse_name(self, input_json):
        j = json.loads(input_json)
        title = j['title']
        match = re.findall('\d+\s(\S+)\s+', title)
        return match[0]

    def get_data(self, input_json=None):
        if input_json is None:
            node = '/exchangeReport/FMNPTK'
            params = {'response': 'json', 'stockNo': self.code}
            url = self.get_endpoint(node, params)
            resp = self.req.get(url)
            if hasattr(resp, 'text'):
                input_json = resp.text
            else:
                raise ValueError('get_data failed.')

        r_dict = json.loads(input_json)

        years, max_prices, min_prices, avg_prices = [], [], [], []
        for row in r_dict['data']:
            years.append(row[0] + 1911)
            max_prices.append(float(row[4]))
            min_prices.append(float(row[6]))
            avg_prices.append(float(row[8]))

        self.data = {
            'years': years,
            'max_prices': max_prices,
            'min_prices': min_prices,
            'avg_prices': avg_prices,
        }
        return self

    def index_to_year(self, index=0):
        return self.data['years'][index] + 1911

    def year_to_index(self, input_year=None):
        for year in self.data['years']:
            if year == input_year + 1911:
                return self.data['years'].index(year)
        return -1

    def get_max_price(self, year=None):
        return year is None and self.data['max_prices'] or self.data['max_prices'][self.year_to_index(year)]

    def get_min_price(self, year=None):
        return year is None and self.data['min_prices'] or self.data['min_prices'][self.year_to_index(year)]

    def get_avg_price(self, year):
        return year is None and self.data['avf_prices'] or self.data['avf_prices'][self.year_to_index(year)]
