#coding: utf-8
__author__ = 'AS126'

from urllib.request import *
import random

def reqs(url,encode='utf-8'):
    request=Request(url)
    ua_list=['User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2467.2 Safari/537.36',
             'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36']
    request.add_header('User-Agent',random.choice(ua_list))
    return urlopen(request).read().decode(encode)