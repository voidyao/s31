
import sys

def check():
	print("查看成绩")

def add():
	print("添加成绩")

def update():
	print("修改成绩")

def order():
	print("成绩排序")

def quit():
	sys.exit(0)

print('''
   1 查看成绩
   2 修改成绩
   3 添加成绩
   4 统计成绩
   5 退出
''')

handler = {"1":check,"2":update,"3":add,"4":order,"5":quit}
while 1:
	choice = input("请输入选择>>>")
	if choice.isdigit():
		func = handler.get(choice)
		if func:
			func()
		else:
			print("没有匹配的数字项")
	else:
		print("非法输入")