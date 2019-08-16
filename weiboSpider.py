#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/15 14:40
#@Author: jzy
#@File  : weiboSpider.py

import codecs
import csv
import os
import random
import re
import sys
import traceback
from collections import OrderedDict
from datetime import datetime,timedelta
from time import sleep

import requests
from lxml import etree
from requests.adapters import HTTPAdapter
from tqdm import tqdm

class weibo(object):
    cookie = {'Cookie':'your cookie'}  # 将your cookie替换成自己的cookie

    def __init__(self, user_id, filter=0, pic_download=0, video_download=0):
        """weibo类初始化"""
        if not isinstance(user_id,int):
            sys.exit(u'user_id应为一串数字，请重新输入')
        if filter != 0 and filter != 1:
            sys.exit(u'filter值应为0或1,请重新输入')
        if pic_download != 0 and pic_download != 1:
            sys.exit(u'pic_download值应为0或1,请重新输入')
        if video_download != 0 and video_download != 1:
            sys.exit(u'video_download值应为0或1,请重新输入')

        self.user_id = user_id  # 用户id,即需要我们输入的数字,如昵称为"Dear-迪丽热巴"的id为1669879400
        self.filter = filter # 取值范围为0、1，程序默认值为0，代表要爬取用户的全部微博；1代表只爬取用户的原创微博
        self.pic_download = pic_download # 取值范围仍然是0、1，程序默认值是0表示不现在微博原始图片，1表示下载
        self.video_download = video_download # 取值范围是0、1，程序默认值是0表示不下载微博视频，1代表下载
        self.nickname = '' # 用户昵称，如：“Dear-迪丽热巴”
        self.weibonum = 0 # 用户全部微博数
        self.got_num = 0 # 爬取到的微博数
        self.following = 0 # 用户关注数
        self.followers = 0 # 用户粉丝数
        self.weibo = [] # 用来存储爬取到的全部微博信息

        def deal_html(self, url):
            """处理HTML"""
            try:
                html = requests.get(url, cookies = self.cookie).content
                selector = etree.HTML(html)
                return selector
            except Exception as e:
                print('Error:', e)
                traceback.print_exc()

        def deal_garbled(self, info):
            """处理乱码问题"""
            try:
                info = (info.xpath('string(.)').replace(u'\u200b', '').encode(
                    sys.stdout.encoding, 'ignore').decode(sys.stdout.encoding))
                return info
            except Exception as e:
                print('Error:', e)
                traceback.print_exc()

        def get_nickname(self):
            """获取用户昵称"""
            try:
                url = 'htttps://weibo.cn/%d/info' % (self.user_id)
                selector = self.deal_html(url)
                nickname = selector.xpath('//title/text()')[0]
                self.nickname = nickname[:-3]
                if self.nickname == u'登录 - 新' or self.nickname == u'新浪':
                    sys.exit(u'cookie错误或已过期,请按照README中方法重新获取')
                print(u'用户昵称: ' + self.nickname) # 加 u 就可以正常打印出中文
            except Exception as e:
                print('Error: ', e)
                traceback.print_exc()
