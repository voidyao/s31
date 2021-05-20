



# （1） 位置参数
# def add(x,y):
# 	print(x+y)
# add(1)
# add(1,2,3)
# add(23,45)

# （2） 默认参数

# def print_info(name,age,gender="男"):
# 	print("姓名：%s，年龄：%s，性别：%s"%(name,age,gender))
#
# print_info("张三",23)
# print_info("李四",33)
# print_info("赵四小姐",33,"女")
# print_info("王五",43)

# （3） 关键字参数

# def print_info(name,age,height):
# 	print("姓名：%s，年龄：%s，身高：%scm"%(name,age,height))

# print_info("张三",23,180)
# print_info("张三",180,23)
# print_info(name="张三",height=180,age=23)
# print_info(name="张三",age=23,height=180)
# print_info(names="张三",age=23,height=180)

# (4) 不定长参数:  *args   **kwargs

# def add(x,y,z):
# 	print(x+y+z)
# add(1,2,3)


# def add(name,*args):
# 	print("args:",args)
# 	print("args type",type(args)) # args type <class 'tuple'>
# 	ret = 0
# 	for i in args:
# 		ret += i
# 	print(ret)
#
# add("超级加法器",1,2,3,4)


# **kwargs
# def print_info(**kwargs):
# 	print("kwargs:",kwargs)
#
# print_info(name="张三",height=180,age=23)


# 同时使用*args和**kwargs
def print_stu_info(name, age=18, *args, **kwargs):
	print(name, age)
	print(args)
	print(kwargs)

print_stu_info("yuan", 20, "China", "Beijing", height="188cm", weight="60kg")




