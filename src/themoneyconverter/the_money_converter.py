import requests
from bs4 import BeautifulSoup

from datetime import datetime, timedelta
from enum import Enum


class MoneyConverter:
    URL_TEMPLATE = 'https://themoneyconverter.com/zh-CN/{source}/{target}?amount=1.00'

    def __init__(self, source='CNY', target='CNY'):
        self.rate = {}
        self.source = source
        self.target = target
        self.updateTime = None

    def refresh(self):
        url = MoneyConverter.URL_TEMPLATE.format(source=self.source, target=self.target)
        response = requests.get(url)
        # print("响应：", response.text)
        bs = BeautifulSoup(response.text, 'lxml')
        table = bs.find('table', attrs={'id': 'major-currency-table'})
        for tr in table.find_all('tr'):
            # print('行：', tr)
            em_list = tr.find_all('em')
            td_list = tr.find_all('td')

            self.rate[em_list[0].attrs['class'][0]] = td_list[2].attrs['data-value']
            self.rate[em_list[1].attrs['class'][0]] = td_list[5].attrs['data-value']

            a_list = tr.find_all('a')
            # print('{} = \'{}\''.format(em_list[0].attrs['class'][0], a_list[0].attrs['title'].replace(' 汇率', '')))
            # print('{} = \'{}\''.format(em_list[1].attrs['class'][0], a_list[1].attrs['title'].replace(' 汇率', '')))
        # print('汇率表：', self.rate)

        time_tag_list = bs.find_all('time')
        detester = time_tag_list[1].attrs['datetime']
        # print("时间：", detester)
        utc_time = datetime.strptime(detester, '%Y-%m-%d %H:%M:%SZ')
        self.updateTime = utc_time + timedelta(hours=8)

        # print('更新时间', self.updateTime)

    def get_rate(self, key):
        return self.rate.get(key)


class Currency(Enum):
    AED = '阿联酋迪拉姆'
    JPY = '日元'
    ARS = '阿根廷比索'
    KRW = '韩元'
    AUD = '澳元'
    MAD = '摩洛哥迪拉姆'
    BRL = '巴西雷亚尔'
    MXN = '墨西哥比索'
    CAD = '加元'
    NOK = '挪威克朗'
    CHF = '瑞士法郎'
    NZD = '新西兰元'
    CNY = '人民币'
    PHP = '菲律宾比索'
    CZK = '捷克克朗'
    PLN = '波兰兹罗提'
    DKK = '丹麦克朗'
    RUB = '俄罗斯卢布'
    EUR = '欧元'
    SEK = '瑞典克朗'
    GBP = '英镑'
    SGD = '新加坡元'
    HKD = '港元'
    THB = '泰铢'
    HUF = '匈牙利福林'
    TRY = '土耳其里拉'
    ILS = '以色列谢克尔'
    USD = '美元'
    INR = '印度卢比'
    ZAR = '南非南特'
