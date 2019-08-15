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
