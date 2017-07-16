#!/usr/bin/env python
# coding: utf-8




'''
chapter 1
print "Hello";
'''




'''
chapter 2-3

age = 23			# 赋值整型 
height = 1.85		# 浮点型 
name = "Jackie"		# 字符串
print age
print height
print name
a,b,c = 1,2,3

str = 'Hello World!'
print str			# 输出完整字符串
print str[0]		# 输出字符串中的第一个字符
print str[2:5]		# 输出字符串中第三个至第五个之间的字符串
print str[2:]		# 输出从第三个字符开始的字符串
print str * 2		# 输出字符串两次
print str + "TEST"	# 输出连接的字符串
# %和//,%是取模，也就是得出除法的余数，//相反取的是商的整数部分
print 7%3, 7//3
'''





# chapter 4

import random					# 导入随机数
s = int(random.uniform(1,10))	# 设置1-10的随机数字
m = int(input('输入整数：'))
while m != s:
	if m > s:
		print('大了')
		m = int(input('输入整数：'))
	if m < s:
		print('小了')
		m = int(input('输入整数：'))
	if m == s:
		print('OK')
		break;
'''
输入整数：1
小了
输入整数：5
OK
ubuntu@ubuntu-VirtualBox:~/Program/Project/Tutorials$ python python_1.py
输入整数：9
大了
输入整数：5
OK
'''



