# coding: utf-8
__author__ = 'AS126'

from html.parser import HTMLParser

import req


class spider(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.link = []
        self.user_list = []
        self.pass_list = []
        self.user = False
        self.password = False

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            if len(attrs):
                for (name, value) in attrs:

                    if value == 'articleSection':
                        self.user = True
                    if value == 'articleBody':
                        self.password = True
            else:
                pass

    def handle_data(self, data):
        if self.user:
            self.user_list.append(data)
            self.user = False
        if self.password:
            self.pass_list.append(data)
            self.password = False


if __name__ == '__main__':
    html = req.reqs('http://www.9sep.org/free-xunlei-vip')
    spiders = spider()
    spiders.feed(html)
    result = zip(spiders.user_list, spiders.pass_list)
    for (username, password) in result:
        print('账号{0};密码{1}'.format(username, password))
    spiders.close()
    print('数据来源：VIP分享吧 http://www.vipfx8.com')
