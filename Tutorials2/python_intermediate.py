# coding: utf-8
# Python 中级课程
'''
本课程是对初级教程的补充，主要讲解 Python 中的异常处理、模块、文件 I/O、GUI 编程等知识
最后带你用这些知识做一个日记本的桌面应用程序
'''




# Lesson 1
'''
异常就是代码在执行过程中发生的一个特殊的事件. 如果不对异常进行处理，那么当出现异常时，程序就会崩溃无法正确运行
处理异常需要用到 try/except 语句，我们通过一个除法程序举例来看看该如何使用

鲁棒性, 也就是系统和程序的稳定性、健壮性
'''

'''
num1 = raw_input('输入被除数：')
num2 = raw_input('输入除数：')
# 用 int() 将 num1、num2 转为数字
result = int(num1) / int(num2)
print '运算结果为：%d' % result
'''

'''
while 1:
	try:
		num1 = raw_input('输入被除数：')
		num2 = raw_input('输入 除数：')
		result = float(num1) / float(num2)
	#except Exception as e:
	#	raise e
	except ZeroDivisionError:
		print '0 不能做除数' + '\n'
	except ValueError:
		print '请勿输入空值或字母' + '\n'
	else:
		print '运算结果为：%f' % result + '\n'
'''

'''
while True:
	try:
		num1 = raw_input('Please input the dividend: ')
		num2 = raw_input('Please input the divisor : ')
		result = float(num1) / float(num2)
	except BaseException:
		print 'Problem occurred.' + '\n'
	else:
		print "The calculation result is: ", result, '\n'
'''




# Lesson 2    模块的知识
'''
模块（Module）当然也是一个 Python 文件
当我们做一个程序时，可以把与某功能的相关代码写在一个模块里，这样能让我们整体的代码更清晰、更好用

如何编写呢？
非常简单，我们新建一个 Python 文件，斌叔建了一个名为 hello.py 的模块
然后编写一个最简单的模块，进行如下编辑

除此外，我们还可以通过 from ... import ... 的形式导入模块
比如爬虫课程中的 from selenium import webdriver 就表示我们导入了 selenium 模块中的 webdriver 函数
要是写成 from selenium import * 则表示导入 selenium 的全部内容，但是不建议过多的这样来写
'''

def say_hello(par):
	print 'Hello,', par +'.'
	return 

say_hello('Jackie')  #hello.say_hello('Jackie')

import calendar
cal = calendar.month(2017, 8)
print cal




# Lesson 3
'''
Python 中的文件操作
学完这节课，我们就能过通过代码来创建、修改和管理文件

首先我们创建一个文件，我在桌面上创建了一个名为 cxy_python 的文件夹
位置和名字可以随便设置，我为了方便就放在了桌面上

下面开始编写代码，首先我们要拿到要操作的文件对象
这就要涉及到 Python 的一个内置函数 open()

这就是我们通过文件操作而创建的
但是我们的文件是空的，让我们来给它写入点内容，这就用到了 write() 方法

然后我们再看看如何读取
看程序和运行结果，通过 read() 方法可以读取文件的内容，你也试着操作一下

看程序和运行结果，通过 read() 方法可以读取文件的内容，你也试着操作一下
完成了
好，那么如果我要重命名一个文件，或者删除一个文件该怎么办呢
你知道重命名和删除的英文是什么吗？
rename and remove
Very good! 我们要使用的方法也就是 rename() 和 remove()
不过在使用前，我们需要导入 os 模块
remove() 的使用更是简单，只要添加要删除的文件名即可

运行后发现，test2.txt 被删除了
好，我们这节课主要讲了写、读、改、删这几个常用的文件操作方法
'''

# 打开一个文件
# 第一个参数： 表示我要打开的文件名是 test1.txt
# 第二个参数： 为打开文件的模式是 wb
#                      wb 代表通过二进制格式打开一个文件来写入
#                      若该文件已存在，则覆盖；若不存在，则新建

fileObj = open("test1.txt", "wb")
print "文件名称：", fileObj.name
print "文件是否关闭：", fileObj.closed
print "文件访问模式：", fileObj.mode 
print "文件末尾是否强制加空格：", fileObj.softspace
fileObj.close()
print "文件是否关闭：", fileObj.closed
# 0表示没有强制加空格，反之则会输出1

# 打开文件
fileObj = open("test1.txt", "wb")
# 写入文字 \n 表示换行
fileObj.write("I'm learning Python on this website.\n");
# 关闭文件
fileObj.close()

# 打开文件，r+ 表示读写模式
fileObj = open("test1.txt", "r+")
# 读取文件
string = fileObj.read()
print "读取内容为：", string
# 关闭文件
fileObj.close()

import os
# rename("原文件名", "要修改的名")
os.rename("test1.txt", "test2.txt")
os.remove("test2.txt")

'''
Hello, Jackie.
    August 2017
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

文件名称： test1.txt
文件是否关闭： False
文件访问模式： wb
文件末尾是否强制加空格： 0
文件是否关闭： True
读取内容为： I'm learning Python on this website.

[Finished in 0.0s]

References
http://blog.csdn.net/ztf312/article/details/47259805
'''




# Lesson 4
'''
'''




