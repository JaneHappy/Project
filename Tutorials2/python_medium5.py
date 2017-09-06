# coding: utf-8

'''
接下来就是见证奇迹的时刻
开始学习啦，这节课我们来完善一下日记本的功能
不多废话，直接上代码

你可以在这个地址下载本小节课所需的代码 
https://static1.bcjiaoyu.com/cxy.zip

第一步，我们把要用到的控件写好，其中 entry、text 和 listBox 先不要放到主窗口上

下一步定义一个方法，用于创建文件夹，并切换工作目录到该文件夹中
注释已经写的很清楚了，不过要注意，这用到了 os 模块的方法，不要忘记导入 os 模块，import os

下面看一下如何给按钮添加点击事件，先看写日记的时候
command=write 表示点击这个按钮时候，会执行 write 方法，然后我们来写一下 wirte 方法

好，下一步，同样使用 command，我们来给保存按钮也设置一个点击事件，并完善这个方法
斌叔把每句的意思都写着了注释中，是不是有一部分很眼熟，文件操作中的知识对不对

要注意这步判断，当没有输入标题就保存时，我们给个提示，不执行保存方法
看看效果，自己写一下

好，胜利就在眼前了
下面来给看日记按钮添加一个方法，command=read，并完善 read 方法
同上节课有些不同，上节课 ListBox 的演示中，是直接写了一个列表做为数据源

现在我们要获取当前文件夹内的文件，做为列表，如果没有文件设置提示，有就把它们插入到列表中
然后列表的点击方法可不是 command 了，要使用 bind
listBox.bind('<Double-Button-1>',showDiary) 这就表示过给列表绑定了一个双击方法 showDiary，那么下一步自然是完善 showDiary 方法

除了第一句获取点击的列表项名称我们没接触过，其他的都很简单吧，也是文件操作的知识
看下效果，动手写一写

最后是退出按钮，直接 command = quit 就可以了
但是在 Mac 上有一点问题，不能通过输入法来输入中文，也没关系这不是重点，只要学会如何编写就 OK 了
如果你遇到问题，可以参考如下代码

'''




from Tkinter import *
import os

# 创建日记文件夹
def initDiary():
	my_dir = os.getcwd()                           		# 获取当前.py 文件目录
	my_list =  os.listdir(my_dir)                     	# 获取当前目录中所有文件
	haveDiary = False                           		# 设置一个变量，是否存在 diary 文件夹，默认为 False
	for item in my_list:                           		# 遍历
		if item == "diary":                     		# 判断是否存在 diary 文件夹
			haveDiary = True                    		# 如果有，设置 diary 为 True
	if haveDiary == False:                      		# 如果 haveDiary 为 False
		os.mkdir("diary")                       		# 创建 diary 文件夹
	os.chdir("./diary")                         		# 改变.py 工作目录到 diary 内

# 写日记
def write():
	textVar.set("")                             # 清空 entry
	text.delete("0.0", "end")                   # 清空 text
	label.config(text = "写日记模式") 
	listBox.pack_forget()                       # 隐藏 listBox
	entry.pack()                                # 显示 entry
	text.pack()                                 # 显示 pack

# 保存
def save():
	title = textVar.get() + ".txt"              # 获取标题
	content = text.get("0.0", "end")            # 获取内容

	if title != ".txt":
		fileObj = open(title, "wb")             # 打开一个文件
		fileObj.write(content);                 # 写入内容
		fileObj.close()                         # 关闭打开的文件
		label.config(text = "已保存") 
	else:
		label.config(text = "请输入标题") 

# 看日记
def read():
	listBox.delete(0, END)                       		# 清空 listBox
	my_dir = os.getcwd()                           		# 获取当前目录
	my_list =  os.listdir(my_dir)                     	# 获取目录内所有文件

	showText = "看日记模式"                      
	if len(my_list) == 0:                          		# 如果当前没有日记
		showText += "（日记本是空的）"            			# 设置提示  
	label.config(text = showText)

	for item in my_list:                           		# 遍历
		listBox.insert(0,item)                  		# 向listBox 插入数据
	
	listBox.bind('<Double-Button-1>',showDiary) 		# 绑定双击事件

	entry.pack_forget()                         		# 隐藏 entry
	text.pack_forget()                          		# 隐藏 text
	listBox.pack()                              		# 显示 listBox

# 显示日记内容
def showDiary(event): 
	print listBox.curselection()
	title = listBox.get(listBox.curselection()) # 获取点击的日记名
	showTitle = title[:-4]                      # 截取至倒数第4个字符(即不显示.txt)
	textVar.set(showTitle)                      # 设置日记标题

	fileObj = open(title, "r+")                 # 打开对呀标题的文件
	content = fileObj.read();                   # 获取文件内容
	text.delete("0.0", "end")                   # 清空 text
	text.insert("end", content)                 # 把内容显示在 text 上
	fileObj.close()                             # 关闭打开的文件

	listBox.pack_forget()                       # 隐藏 listBox
	entry.pack()                                # 显示 entry
	text.pack()                                 # 显示 text
	


initDiary()

root = Tk()
root.geometry("500x400")
root.title("程序媛日记本")

saveBtn = Button(root, text="保存", command=save)
saveBtn.pack(side=LEFT, anchor='sw')

quitBtn = Button(root, text="退出", command=quit)
quitBtn.pack(side=RIGHT, anchor='se')

writeBtn = Button(root, text="写日记", command=write)
writeBtn.pack(side=BOTTOM, anchor='s')

readBtn = Button(root, text="看日记", command=read)
readBtn.pack(side=BOTTOM, anchor='s')

textVar = StringVar()
entry = Entry(root, textvariable=textVar)
text = Text(root)
listBox = Listbox(root, height=300)

label = Label(root)
label.pack()
label.config(text="这是一个演示程序")

root.mainloop()



