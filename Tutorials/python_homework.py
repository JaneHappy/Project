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





'''
chapter 13
看看我和机器人的对话过程，然后自己试着写写吧
'''


dictionary = {
	'Hello~'						: 'Hello~',
	'Nice to meet you~'				: 'Nice to meet you, too.',
	'Which fruit do you like best?'	: 'I like apple very much.',
	'How old are you?'				: '20 years old.',
	'You are handsome!'				: 'Thank you~'
	'''
	'Haha'							: 'Why do you laugh?',  #'Heihei',
	'I'm sleepy...'					: 'Good night~',
	'''
}


flag = 'chat'
work = True

print "Hi~ My name is Python. Do you wanna chat with me?"

while flag == 'chat' or flag == 'train':
	flag = raw_input("You can choose to chat with me, train me to talk, or let me leave. Which one do you choose? (chat/train/leave)")

	if flag == 'train':  ## with punctuations 标点符号
		question = raw_input("Please input your question as key: ")
		answer   = raw_input("Please input your answer as value: ")
		dictionary[str(question)] = str(answer)  ## save key-value
		print "Training success!", "Now I can answer %d questions." %len(dictionary)

	elif flag == 'chat':
		if len(dictionary) == 0:
			print "I cannot answer any question yet. Please train me first!"
			continue
		chat_word = raw_input("Thanks for chatting with me, what do you want to say? ")

		for key in sorted(dictionary.keys()):
			if str(chat_word) == key[:len(str(chat_word))]:
				work = True
				print dictionary[key]
				break
			else:
				work = False
		if work == False:
			print "Sorry, I cannot answer this question yet."
			work = True

	elif flag == 'leave':
		print "Okay, see you next time~"
		break

	else:
		print "Please input following these descriptions."  ##tips  #prompt instructions."
		continue




