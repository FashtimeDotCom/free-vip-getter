#coding: utf-8
__author__ = 'AS126'

from html.parser import HTMLParser
from urllib.request import *
import re

class spider(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.link=[]
        self.rlink=[]
        self.data_list=[]
        self.a_tag=False
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            if attrs:
                self.a_tag=True
                for (name,value) in attrs:
                    if name=='href' and (not re.match('javascript.*',value)):

                        self.link.append(value)

    def handle_data(self, data):
        link_re='夜间自动更新.*爱奇艺VIP账号.*'

        if self.a_tag:
            if self.link:
                if re.match(link_re,data):
                    self.rlink.append(self.link.pop())
                    pass
                else:

                    self.link.pop()
        data_re='账号 *\d'
        if re.search(data_re,data):
            self.data_list.append(data)
    def handle_endtag(self, tag):
        if tag == 'a':
            self.a_tag=False
if __name__ == '__main__':
    request=Request('http://www.aiqiyivip.com/forum-2-1.html')
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2467.2 Safari/537.36')
    html=urlopen(request).read().decode('gbk')
    spider1=spider()
    spider1.feed(html)
    for link in spider1.rlink:
        page_request=Request(link)
        page_request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2467.2 Safari/537.36')
        vip_page=urlopen(page_request).read().decode('gbk')
        vip_page.replace('<br>','')
        spider2=spider()
        spider2.feed(vip_page)
        for data in spider2.data_list:
            print(data)
        spider2.close()
    print('数据来源：http://www.aiqiyivip.com/')

    spider1.close()
