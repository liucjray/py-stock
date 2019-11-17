import urllib3
import json

import unittest
from Services.PandasService import *


class PandasServiceTest(unittest.TestCase):
    http = None

    def setUp(self):
        self.PandasService = PandasService()
        self.http = urllib3.PoolManager()

    def testBalanceSheet(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)',
        }
        data = "encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&inpuType=co_id&TYPEK=all&isnew=true&co_id=6666&year=107&season=01"
        # data = json.dumps(data).encode()  # json.dumps方法可以将python对象转换为json对象
        response = self.http.request('POST', 'https://mops.twse.com.tw/mops/web/ajax_t164sb03', body=data,
                                     headers=headers)
        self.assertEqual(200, response.status)
        html = response.data.decode('utf-8')

        # print(html)
        self.PandasService.read_html(html)
