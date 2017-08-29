#!/usr/bin/env python
#coding: utf-8
from __future__ import print_function




# PART I





# PART 2




# PART 3




# PART 4
'''
from selenium import webdriver

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

'''








#----------------------------------



#!/usr/bin/env python
#coding: utf-8
#from __future__ import print_function





'''
Class 2:

# 导入 selenium
from selenium import webdriver

# 打开谷歌浏览器，并访问百度
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
'''



'''
Class 2:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获取浏览器中 name 为 wd 的标签
elem = driver.find_element_by_name("wd")
# 搜索 cxy61
elem.send_keys("cxy61")
elem.send_keys(Keys.RETURN)
# 打印页面
print driver.page_source
##driver.quit()
'''



# PART  III,  Class 3
'''

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

dr = webdriver.Chrome()
dr.get('https://www.qiushibaike.com/')

# 获取 id 为 content-left 的元素
main_content = dr.find_element_by_id('content-left')
# 获取 class 为 content 的元素
contents = main_content.find_elements_by_class_name('content')

# for 循环
i = 1
for content in contents:
	#print(content.text)
	print(str(i)+'.' + content.text + '\n')
	i += 1

# 退出
dr.quit()

'''




from selenium import webdriver

class Qiubai:
	def __init__(self):
		self.dr = webdriver.Chrome()
		self.dr.get('https://www.qiushibaike.com/')

	def print_contenx(self):
		main_content = self.dr.find_element_by_id('content-left')
		contents = main_content.find_elements_by_class_name('content')

		i = 1
		for content in contents:
			print(str(i)+"." + content.text + '\n')
			i += 1

		self.quit()

	def quit(self):
		self.dr.quit()


Qiubai().print_contenx()












