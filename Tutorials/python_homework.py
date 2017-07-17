# coding: utf-8




'''
chapter 10
留个小作业，你能用这节课的知识，通过日历模块显示今天是星期几么？
给你个提示，Python时间日期格式化符号表中可能有你需要的信息哦
'''

import time
import calendar

print time.strftime("Today is %A", time.localtime())
print time.strftime("Output the calender of %m in %Y", time.localtime())
year = time.strftime("%Y", time.localtime())
month = time.strftime("%m", time.localtime())
print '\n',calendar.month(int(year), int(month))






