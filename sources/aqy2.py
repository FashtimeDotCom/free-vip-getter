#coding: utf-8
__author__ = 'AS126'

from html.parser import HTMLParser
from urllib.request import urlopen
import re
import req

class spider(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.link=[]
        self.data_list=[]
    def handle_starttag(self, tag, attrs):
        title=False
        link_re='.*爱奇艺vip.*'
        if tag == 'a':
            if len(attrs) == 0:
                pass
            else:
                for (name,value) in attrs:
                    if name=='title':
                        if re.search(link_re,value):
                            title=True
                for (name,value) in attrs:
                    if name=='href' and title:
                        self.link.append(value)
    def handle_data(self, data):
        data_re='账号\d*'
        if re.match(data_re,data):
            self.data_list.append(data)

if __name__ == '__main__':
    html=req.reqs('http://www.vipfenxiang.com/aiqiyi/')
    spider1=spider()
    spider1.feed(html)
    result=spider1.link
    for link in result:
        vip_page=req.reqs(link)
        spider2=spider()
        spider2.feed(vip_page)
        for data in spider2.data_list:
            print(data)
    print('数据来源：VIP分享网 http://www.vipfenxiang.com/')
    spider1.close()
    spider2.close()

