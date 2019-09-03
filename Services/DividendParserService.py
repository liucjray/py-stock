import requests
from bs4 import BeautifulSoup


class DividendParserService:
    url = 'https://tw.stock.yahoo.com/d/s/dividend_{}.html'
    code = None
    html = None
    bs4 = None

    def __init__(self, code):
        self.code = code

    def set_html(self, html):
        self.html = html
        return self

    def set_html_real(self):
        url = self.url.format(self.code)
        self.html = requests.get(url).text
        return self

    def set_bs4(self):
        self.bs4 = BeautifulSoup(self.html, 'lxml')
        return self

    def get_name(self):
        soup = self.bs4
        name = soup.select('table font b')[0]
        return name.string

    def get_title(self):
        titles = []
        soup = self.bs4
        column_table = soup.select('table table')[1]
        tr = column_table.find_all('tr')[0]
        tds = tr.find_all('td')
        for td in tds:
            titles.append(td.string)
        return titles

    def get_data(self):
        data = []
        soup = self.bs4
        data_table = soup.select('table table')[1]
        trs = data_table.find_all('tr')[1:]

        for tr in trs:
            tds = tr.find_all('td')
            tmp = []
            for i in range(len(tds)):
                tmp.append(tds[i].string)
                if i + 1 == len(tds):
                    data.append(tmp)
        return data
