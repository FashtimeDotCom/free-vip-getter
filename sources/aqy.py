#coding: utf-8
__author__ = 'AS126'
#更新行记：
#update：2015.9.22 于电脑课上
#源站继续改数据结构，以为这就能防止被爬了？

from html.parser import HTMLParser
import re
import req

class spider(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.link=[]
        self.rlink=[]
        self.data_list=[]
        self.pass_list=[]
        self.a_tag=False
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            if attrs:
                self.a_tag=True
                for (name,value) in attrs:
                    if name=='href' and (not re.match('javascript.*',value)):

                        self.link.append(value)

    def handle_data(self, data):
        link_re='【夜间自动】更新爱奇艺.*'

        if self.a_tag:
            if self.link:
                if re.match(link_re,data):
                    self.rlink.append(self.link.pop())
                    pass
                else:

                    self.link.pop()
        data_re='账号 *\d'
        pass_re='\r\n密码.*'
        if re.search(data_re,data):
            self.data_list.append(data)
        if re.search(pass_re,data):
            self.pass_list.append(data)
    def handle_endtag(self, tag):
        if tag == 'a':
            self.a_tag=False
if __name__ == '__main__':
    html=req.reqs('http://www.aiqiyivip.com/forum-2-1.html','gbk')
    spider1=spider()
    spider1.feed(html)
    for link in spider1.rlink:
        vip_page=req.reqs(link,'gbk')
        vip_page.replace('<br>','')
        spider2=spider()
        spider2.feed(vip_page)
        re_list=zip(spider2.data_list,spider2.pass_list)
        for data in re_list:
            for i in data:
                print(i.lstrip(),end='')
            print()
        spider2.close()
    print('数据来源：http://www.aiqiyivip.com/')

    spider1.close()
