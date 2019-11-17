from statistics import mean
from Services.TWSEService import *


class TrafficLightStrategyService(TWSEService):
    qs, code, price, name = None, None, None, None

    def __init__(self):
        pass

    def set_code(self, input_code=None):
        # print('set_code')
        self.code = input_code
        return self

    def set_price(self):
        # print('set_price')
        self.price = self.info['price']
        return self

    def set_name(self):
        # print('set_name')
        self.name = self.info['name']
        return self

    def get_twse_data(self, input_json=None):
        # print('get_twse_data')
        self.get_data(input_json)
        return self

    def compute(self):
        # print('compute')
        avg_min_prices = mean(self.data['min_prices'][-10:])
        avg_avg_prices = mean(self.data['avg_prices'][-10:])
        avg_max_prices = mean(self.data['max_prices'][-10:])

        price = float(self.price)

        avg_cheap_and_ok_price = (avg_min_prices + avg_avg_prices) / 2
        avg_ok_and_pricey_price = (avg_avg_prices + avg_max_prices) / 2
        # print(avg_cheap_and_ok_price, avg_ok_and_pricey_price)
        # print(1, price <= avg_cheap_and_ok_price)
        # print(2, price >= avg_ok_and_pricey_price)
        # print(3, avg_cheap_and_ok_price > price and price < avg_ok_and_pricey_price)
        # print(price, avg_cheap_and_ok_price, avg_ok_and_pricey_price)

        compute_result = ''
        if price <= avg_cheap_and_ok_price:
            compute_result = '便宜價'
        elif avg_cheap_and_ok_price < price < avg_ok_and_pricey_price:
            compute_result = '合理價'
        elif price >= avg_ok_and_pricey_price:
            compute_result = '昂貴價'

        msg = "ID:{}-{} 現為 {} - 現價:{} / 便宜價:{} / 合理價:{} / 昂貴價:{}".format(
            self.code,
            self.name,
            compute_result,
            price,
            self.price_format(avg_min_prices),
            self.price_format(avg_avg_prices),
            self.price_format(avg_max_prices),
        )
        print(msg)
