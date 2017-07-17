#!/usr/bin/env python
#coding:utf-8




# chapter 13
'''
我们的Python的基础课程到这里告一段落了
这节课，我们要用学过的知识来完成一个小程序
这个程序是一个问答机器人

不难不难，我们只需要让它能够回答简单的问题即可
还可以训练它去记住某个问题和答案，下次你同它对话，它就会回答相应的话语
'''




'''
dictionary = {
	'Hello'							: 'Hello',
	'Nice to meet you'				: 'Nice to meet you, too',
	'Which fruit do you like best'	: 'I like apple very much',
	'How old are you'				: '20 years old',
	'You are handsome'				: 'Thank you'
}
'''
dictionary = {
	
}

# t--train 训练机器人对话；c--chat 同机器人聊天；l--leave 让机器人离开
flag = 'c'			# 让机器人默认是聊天状态
work = True			# 让机器人开默认是工作的

print 'Hi, my name is Python.'
print 'Do you want to chat with me?'  ##wanna

while flag == 'c' or 't':			# 聊天或训练状态时循环执行
	flag = raw_input("你可以选择跟我聊天(c)还是训练我对话(t)，或让我离开(l)？(c/t/l) ")

	# 训练状态时
	if flag == "t":
		question = raw_input("请输入问题 (key)：")		# 获取输入作为 key
		answer = raw_input("请输入回答 (value)：")		# 获取输入作为 value
		dictionary[str(question)] = str(answer)		# 向字典中存入键值对
		print "训练成功！"
		print "现在我已经会 %d 个问题了！" % len(dictionary)
		continue									# 跳出本次循环

	# 聊天状态时
	elif flag == 'c':
		if len(dictionary) == 0:			# 如果字典为空
			print "现在我还不会任何问题，请先训练我！"
			continue
		# 获取输入作为要查找的 key
		chat_word = raw_input("谢谢你跟我聊天，你想对我说点什么？ ")
		# 遍历整个字典
		for key in sorted(dictionary.keys()):
			if str(chat_word) == key:		# 如果有相同的 key
				work = True					# 设置机器人工作开启
				print dictionary[key]		# 打印出对应的 value
				break						# 结束遍历
			else:
				work = False				# 无相同 key，机器人不工作
		# 如果机器人为不工作状态，打印提示信息，并重置工作状态为 True
		if work == False:
			print "抱歉，这句话我还不会回答。"
			work = True

	# 执行离开操作时，打印提示信息
	elif flag == 'l':
		print "好的，下次再见~"
		break						# 跳出整个循环

	# 其他情况，不输入或输入非法信息时
	else:
		print "请输入提示的指令："
		continue




'''
ubuntu@ubuntu-VirtualBox:~/Program/Project/Tutorials$ python python-c.py
Hi, my name is Python.
Do you want to chat with me?
你可以选择跟我聊天(c)还是训练我对话(t)，或让我离开(l)？(c/t/l) c
现在我还不会任何问题，请先训练我！
你可以选择跟我聊天(c)还是训练我对话(t)，或让我离开(l)？(c/t/l) l
好的，下次再见~
ubuntu@ubuntu-VirtualBox:~/Program/Project/Tutorials$ python python-c.py
Hi, my name is Python.
Do you want to chat with me?
你可以选择跟我聊天(c)还是训练我对话(t)，或让我离开(l)？(c/t/l) c
现在我还不会任何问题，请先训练我！
你可以选择跟我聊天(c)还是训练我对话(t)，或让我离开(l)？(c/t/l) t
请输入问题 (key)：Hello
请输入回答 (value)：Hello
训练成功！
现在我已经会 1 个问题了！
你可以选择跟我聊天(c)还是训练我对话(t)，或让我离开(l)？(c/t/l) t
请输入问题 (key)：Nice to meet you
请输入回答 (value)：Nice to meet you, too
训练成功！
现在我已经会 2 个问题了！
你可以选择跟我聊天(c)还是训练我对话(t)，或让我离开(l)？(c/t/l) t
请输入问题 (key)：Which fruit do you like best
请输入回答 (value)：I like apple very much
训练成功！
现在我已经会 3 个问题了！
你可以选择跟我聊天(c)还是训练我对话(t)，或让我离开(l)？(c/t/l) c
谢谢你跟我聊天，你想对我说点什么？ How old are you
抱歉，这句话我还不会回答。
你可以选择跟我聊天(c)还是训练我对话(t)，或让我离开(l)？(c/t/l) c
谢谢你跟我聊天，你想对我说点什么？ Hello
Hello
你可以选择跟我聊天(c)还是训练我对话(t)，或让我离开(l)？(c/t/l) c
谢谢你跟我聊天，你想对我说点什么？ hello
抱歉，这句话我还不会回答。
你可以选择跟我聊天(c)还是训练我对话(t)，或让我离开(l)？(c/t/l) l
好的，下次再见~
ubuntu@ubuntu-VirtualBox:~/Program/Project/Tutorials$ 
'''








'''
dictionary = {
	'Hello'							: 'Hello',
	'Nice to meet you'				: 'Nice to meet you, too.',
	'Which fruit do you like best?'	: 'I like apple very much.',
	'How old are you?'				: '20 years old.',
	'You are handsome!'				: 'Thank you~'
}
'''



