import pickle
import requests
from bs4 import BeautifulSoup as bs
import os
from datetime import datetime
import pandas as pd
from collections import OrderedDict
import sys

os.chdir(sys.path[0])

class Omx30_Avanza:
    def __init__(self):
        self.dataFolder = 'data'
        self.urlsFile = 'ticker_to_stock.pickle'
        self.stock_urls_d = self.get_stock_urls()
        self.watch_list = self.get_watch_list()
        self.stock_urls = self.get_stock_urls()

    def get_omx30_companies_today(self):
        company_l = []
        html_doc = requests.get('https://en.wikipedia.org/wiki/OMX_Stockholm_30').text
        soup = bs(html_doc, 'lxml')
        table = soup.find('table', {'class': 'wikitable sortable'})
        for row in table.findAll('tr')[1:]:
            company_l.append(row.findAll('td')[2].text)
        return company_l

    def get_watch_list(self):
        watch_list_l = []
        for file in os.listdir('data'):
            watch_list_l.append(os.path.splitext(file)[0])
        return list(set(watch_list_l)|set(self.get_omx30_companies_today()))

    def get_stock_urls(self):
        with open(self.urlsFile, 'rb') as f:
            return pickle.load(f)

    def make_soup(self, url):
        response = requests.get(url)
        return bs(response.content, 'lxml')

    def to_float(self, string):
        if type(string) == str:
            s = list(string)
            if '+' in s:
                s.remove('+')
            if '%' in s:
                s.remove('%')
            if '\xa0' in s:
                s.remove('\xa0')
            if '\xa0' in s:
                s.remove('\xa0')
            if ' ' in s:
                s.remove(' ')
            if ' ' in s:
                s.remove(' ')
            if ',' in s:
                index = s.index(',')
                s.remove(',')
                s.insert(index, '.')
            return float(r''.join(s))
        else:
            return string

    def crawl(self):
        missing_company_l = []
        date = datetime.now()
        for company in self.watch_list:
            try:
                url = self.stock_urls[company]
            except:
                missing_company_l.append(company)
                with open('MISSING_COMPANY.pickel', 'w+') as f:
                    pickle.dump(missing_company_l,f)
            file_name = '{}.csv'.format(company)
            file_path = os.path.join('data', file_name)
            if file_name in os.listdir('data'):
                df = pd.read_csv(file_path)
            else:
                df = pd.DataFrame()

            soup = self.make_soup(url)
            info_bar = soup.find('div', {'id': 'surface'})
            info_bar_row = info_bar.find_all('div', 'row')[1]
            info_bar_list = info_bar_row.find('ul')

            _close = self.to_float(info_bar_list.find('span', 'lastPrice').text)
            _high = self.to_float(info_bar_list.find('span', 'highestPrice SText bold').text)
            _low = self.to_float(info_bar_list.find('span', 'lowestPrice SText bold').text)
            _change_percent = self.to_float(info_bar_list.find('span', 'changePercent').text)
            _open = self.to_float('{0:.2f}'.format(_close - (_close * (_change_percent / (100.0)))))
            _volume = int(self.to_float(info_bar_list.find('span', 'totalVolumeTraded SText bold').text))

            new_row = pd.DataFrame([[date, _open, _high, _low, _close, _volume]],
                                   columns=['date', 'open', 'high', 'low', 'close', 'volume'])
            frames = [df, new_row]
            df = df.append(new_row, ignore_index=True)
            df.to_csv(file_path, index=False)


if __name__== '__main__':
    a=Omx30_Avanza()
    a.crawl()
