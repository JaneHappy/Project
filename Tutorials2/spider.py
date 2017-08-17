#!/usr/bin/env python
#coding: utf-8
'''
网络爬虫（英语：web crawler），也叫网络蜘蛛（spider），是一种用来自动浏览万维网的网络机器人。其目的一般为编纂网络索引。
'''

# 导入 selenium
from selenium import webdriver

# 打开谷歌浏览器，并访问百度
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
#browser = webdriver.Chrome('http://www.baidu.com/')



