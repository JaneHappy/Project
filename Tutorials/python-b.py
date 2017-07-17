#!/usr/bin/env python
# coding: utf-8




# chapter 5

for letter in 'Python':		# Example 1
	print 'Current letter: ', letter
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:		# e.g. 2
	print 'Current fruit : ', fruit
print "Good bye!"
# eg 3
for index in range(len(fruits)):
	print 'Current fruit : ', fruits[index]
print "Good bye!"




# chapter 6




# chapter 8

tuple1 = ('physics', 'chemistry', 1997, 2000)
tuple2 = (1, 2, 3, 4, 5)
tuple3 = 'a', 'b', 'c', 'd'
# 当我们想要创建一个空元组时，可以这样写 tup1 = ();
# 还有一点要注意, 元组中只包含一个元素时，需要在元素后面添加逗号，例如：tup1 = (50,);

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print tup3   # del tup3
print (100,) * 4




# chapter 9
'''
假如我们不想要key是Age的这个键值对了，我们可以 del dict['Age']; 这样这个字典里Age就不存在了
我们还可以用dict.clear();来清除整个字典
同样的，可以通过del dict;删除这个字典，不过删除后再使用这个字典就会报错，以为这个dict已经从内存中删除了
而dict.clear();后再使用dict则不会报错，因为这个字典依旧存在，只不过里面是空的

关于字典的使用，有两点必须要记住
1、不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};
这时我们如果通过dict['Name']获取值的话，将会获取'Manni',而'Zara'因为后面出现了相同的key被覆盖了
2、键必须不可变，所以可以用数字，字符串或元组充当，而列表就不行

字典还有很多用法，比如我们可以通过 dict.keys()以列表返回一个字典所有的键
对应的可以通过 dict.values()以列表返回一个字典所有的值
'''




# chapter 10
'''
这次我们来看一下Python中日期和时间
Python提供了一个time和calendar模块可以用于格式化日期和时间。
我们先来通过time.time()用于获取当前时间戳

首先 import time 导入时间模块  然后 print time.time();
试一试看看出现了什么	类似1499938242.87这样一串数字
对，这个叫时间戳，它是从1970年1月1日午夜到现在时刻的秒数

至于为什么是1970年1月1日，斌叔这里不多讲
如果你感兴趣的话，可以通过百度、谷歌等，搜索相关知识
记住要善于通过网络获取新知识

那么我们怎么获取能看懂的时间呢？输入下面的代码看看
print time.localtime(time.time());
怎么样出现了年月日、时分秒等信息，对吧
如果我想让它更简明些怎么办呢？比如2008-08-08 13:00:00这样的格式
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime());
运行这段代码看看
因为我们把时间信息格式化为我们想要的格式了
Python中时间日期常用的格式化符号有


Python可以用来获取日历吗？答案是肯定的
'''

import time

print time.time()
print time.localtime(time.time())
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print time.strftime('%y year   %l hour   %A %B   %a %b    |    %c', time.localtime())

import calendar

print calendar.month(2017, 7)




# chapter 11
# chapter 12

str1 = raw_input("raw_input   请输入：");
print "raw_input 的内容是：", str1




# chapter 13

