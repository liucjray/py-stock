import requests
from bs4 import BeautifulSoup
import re


class StockListParserService:
    url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
    code = None
    html = None
    bs4 = None

    def __init__(self):
        pass

    def set_html(self, html):
        self.html = html
        return self

    def set_html_real(self):
        url = self.url
        self.html = requests.get(url).text
        return self

    def set_bs4(self):
        self.bs4 = BeautifulSoup(self.html, 'lxml')
        return self

    def get_code(self):
        trs = self.bs4.select('table.h4 > tbody > tr')
        codes = []
        for tr in trs[2:]:
            tds = tr.find_all('td')
            for i in range(len(tds)):
                if i == 0:
                    code = str(tds[i].string).split('　')[0]
                    codes.append(code)
                else:
                    continue
        return codes

    def get_name(self):
        trs = self.bs4.select('table.h4 > tbody > tr')
        names = []
        for tr in trs[2:]:
            tds = tr.find_all('td')
            for i in range(len(tds)):
                if len(tds) < 7:
                    continue
                elif i == 0:
                    name = str(tds[i].string).split('　')[1]
                    names.append(name)
                else:
                    continue
        return names

    def get_isin_code(self):
        pass

    def get_publish_date(self):
        pass

    def get_type(self):
        pass

    def get_cfi_code(self):
        pass

    def get_category(self):
        pass