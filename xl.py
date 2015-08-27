#coding: utf-8
__author__ = 'AS126'

from html.parser import HTMLParser
from urllib.request import urlopen
import re

class spider(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.link=[]
    def handle_starttag(self, tag, attrs):
        title=False
        link_re='.*迅雷会员.*'
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

if __name__ == '__main__':
    html=urlopen('http://www.vipfx8.com').read().decode('utf-8')
    spiders=spider()
    spiders.feed(html)
    result=spiders.link[1].lstrip('http://www.vipfx8.com/')
    result=result.rstrip('.html')
    spiders.close()
    xlvip_file=urlopen('http://www.vipfx8.com/down?down=' + result).read().decode('gbk')
    print(xlvip_file)
    print('数据来源：VIP分享吧 http://www.vipfx8.com')