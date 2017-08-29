#!/usr/bin/env python
#coding: utf-8
'''
网络爬虫（英语：web crawler），也叫网络蜘蛛（spider），是一种用来自动浏览万维网的网络机器人。其目的一般为编纂网络索引。
'''

import os
# 导入 selenium
from selenium import webdriver

chromedriver = "C:\User\Lenovo\Downloads\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
# 打开谷歌浏览器，并访问百度
browser = webdriver.Chrome(chromedriver)
browser.get('http://www.baidu.com/')
browser.quit()  #driver
#browser = webdriver.Chrome('http://www.baidu.com/')



'''
References:

2017.8.18 2:25
http://selenium-python-zh.readthedocs.io/en/latest/installation.html
https://stackoverflow.com/questions/8255929/running-selenium-webdriver-python-bindings-in-chrome

'''



