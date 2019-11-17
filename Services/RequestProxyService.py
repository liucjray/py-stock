from urllib.parse import urlencode
import requests
import random
from config.config import *
from bs4 import BeautifulSoup


class RequestProxyService:
    config = get_config()
    available_proxy_path = None

    def __init__(self):
        self.available_proxy_path = os.path.join(self.config['PATH']['PROXY'], 'available_proxy.txt')

    def get(self, url):
        resp = None
        try:
            connection_timeout, read_timeout = 3, 5
            proxy = self.get_random_proxy()
            resp = requests.get(url, verify=False, proxies=proxy,
                                timeout=(connection_timeout, read_timeout))
            resp.encoding = 'utf-8'
            self.store_proxy(proxy)
        except Exception as e:
            raise e
        finally:
            return resp

    def store_proxy(self, proxy):
        print('store_proxy')

        self.available_proxy_path = os.path.join(self.config['PATH']['PROXY'], 'available_proxy.txt')

        # 先寫入檔案
        with open(self.available_proxy_path, 'a') as f:
            f.write("%s\n" % proxy)

        # 讀取檔案
        with open(self.available_proxy_path, 'r') as f:
            available_proxies = f.read().splitlines()

        # 去重複後寫回檔案
        with open(self.available_proxy_path, 'w') as f:
            for proxy in list(set(available_proxies)):
                f.write("%s\n" % proxy)

    def get_proxies(self):
        # 讀取 free-proxy-list 版本
        # html = requests.get('https://free-proxy-list.net').text
        # proxies = self.parse_proxies(html)

        # 本地版
        proxies = self.get_local_proxies()
        # print(proxies)
        # exit()
        return proxies

    def get_local_proxies(self):
        # 本地版
        with open(self.available_proxy_path, 'r') as f:
            available_proxies = f.read().splitlines()
        return list(map(lambda x: eval(x), available_proxies))

    def get_random_proxy(self, proxies=None):
        if proxies is None:
            proxies = self.get_proxies()
        proxy = random.choice(proxies)
        print(proxy)
        return proxy

    def get_proxy_by_domain(self, domain):
        pass

    def parse_proxies(self, html, https=None):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find(id='proxylisttable')

        proxies = []

        for tr in table.find_all('tr')[1:-1]:
            try:
                if len(table.find_all('tr')) <= 0:
                    raise ValueError('沒有資料')
                tds = tr.find_all('td')
                # if https is not None and https == tds[6].text.lower():
                #     continue
                domain = "{}:{}".format(tds[0].text, tds[1].text)
                protocal = tds[6].text.lower() == 'yes' and 'https' or 'http'
                proxy = {protocal: domain}
                proxies.append(proxy)
            except Exception as e:
                continue
        return proxies
