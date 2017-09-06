# coding: utf-8
# Python 中级课程




# Lesson 4
'''
我们以往的课程都是在终端里运行显示结果，是不是太过枯燥了
这节课斌叔教你如何编写一个桌面小程序
也就是开始时提到的 GUI 编程，它是图形用户界面的简称（Graphical User Interface）
Python 中有 Tkinter、wxPython 等图形界面开发的库，本课程以 Tkinter 为例讲解

运行看一下
我们发现了一个小火箭图标和一个空白的窗口，这个就是我们刚刚生成的小程序
现在我们来给它丰富一下界面

这个窗口实在是太小了，我们给它变大一点
下面看看如何自定义它的标题
下面我们来试着添加一个按钮(Button)和一个标签(Label)

很简单吧，
btn = Button(root, text='这是一个按钮')，代表创建了一个按钮，btn.pack() 表示把 btn 放在主窗口上，pack 是一种布局方式
Label 可以通过 config 的方法来设置文字，自己试试吧！

还记得第一节中讲过我们要做一个日记本小程序么，我们来看下最终实现的效果，然后看看需要怎么来设置
程序运行后，会在当前目录下生成一个 diary 文件夹，用于存储日记
点击写日记，会出现两个文本框，一个用来写标题，一个写内容，点击看日记，会出现一个列表来显示当前的日记

我们先把按钮按照位置写好
saveBtn.pack(side=LEFT, anchor='sw') 表示把按钮设置在左下
其中 side 有4个值，TOP、BOTTOM、LEFT、RIGHT，默认为 TOP
anchor 是对齐方式，sw 即 southwest(西南)的，也就是左下，以此类推，一共有9个值 n、s、w、e、nw、sw、se、ne、center，默认是 center

先看写日记时，需要用到 Entry 和 Text，Entry 是一个简单的输入控件，Text 用来显示多行文本
StringVar 是一个字符串变量类型，textvariable 表示文本框中的值，写 textvariable=textVar 是为了方便我们后期对标题的一些操作

再来看看日记时，需要显示一个列表，这就要用到 ListBox
比起其他的控件多了一步，不过也是很简单的，默认的列表高度太小了，所以用 height=300 设置了一下高度
但这时列表是空的，我们需要有个数据源，变量，向列表中插入数据，看一下效果，自己写着试试

关于 Tkinter 的使用，还有很多组件这里没有用到，感兴趣的童鞋可以搜索学习下，我们下节课来把这个日记本的功能完善好

'''


'''
from Tkinter import *   # 导入 Tkinter 库

root = Tk() 			# 创建窗口
root.geometry('500x400')
root.title("Custom headers. User-defined.")  #Define its title.

btn = Button(root, text="This is a buttom.") #这是一个按钮
btn.pack()

label = Label(root)
label.pack()
label.config(text="This is a demo.")  #这是一个演示程序

root.mainloop() 		# 开始事件循环
'''


from Tkinter import *

root = Tk()
root.geometry("500x400")
root.title("程序媛日记本")

saveBtn = Button(root, text="保存")
saveBtn.pack(side=LEFT, anchor='sw')

quitBtn = Button(root, text="退出")
quitBtn.pack(side=RIGHT, anchor='se')

writeBtn = Button(root, text="写日记")
writeBtn.pack(side=BOTTOM)

readBtn = Button(root, text="看日记")
readBtn.pack(side=BOTTOM)

label = Label(root)
label.pack()
label.config(text="这是一个演示程序")

textVar = StringVar()
entry = Entry(root, textvariable=textVar)
entry.pack()

text = Text(root)
text.pack()

listBox = Listbox(root, height=300)
listBox.pack()
# 设置一个数据源
mylist = ["apple", "orange", "milk", "water"]  #list
for item in mylist:
	listBox.insert(0, item)
#listBox.pack()

root.mainloop()



# ??????????




