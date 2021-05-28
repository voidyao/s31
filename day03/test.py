def inputscore(snumber,sname,sscore):
	"""
	:return:
	"""
	file = open("data", mode="a+", encoding="utf8")
	print("学生学号:%s,学生姓名:%s,学生成绩:%s"%(snumber,sname,sscore))
	file.write(snumber+"\n"+sname+"\n"+sscore+"\n")
	file.close()

def selectscore(snumber):
	"""
	:return:
	"""
	file = open("data", encoding="utf8")
	for line in file.readlines():
		if line.split(" ")[0] == snumber:
			print("学号 姓名 成绩")
			print(line,end="")
		else:
			print("nono")

print("""
**********欢迎进入学生管理系统**********
				菜单
输入成绩----------------------------1
""")
while True:
	res = input("请输入您的选择:")
	if res.isdigit() and 0 < int(res) < 10:
		if int(res) == 1:
			snumber = input("学生学号：")
			sname = input("学生姓名：")
			sscore = input("学生成绩：")
			inputscore(snumber,sname,sscore)
			print(res)
		elif int(res) == 2:
			snumber = input("请输入学生学号：")
			selectscore(snumber)
			# print(res)
		else:
			print("else")
	elif res == 'q':
		break
	else:
		print("请输入1-9的数字")


