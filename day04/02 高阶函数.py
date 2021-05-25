
# 高阶函数：   1 ： 以函数为函数参数    2： 以函数为返回值
'''
def add(x,y):
	print(x+y)

a = 10
b = 20

add(a,b)

def foo():
	print("foo...")

x = foo

print(id(x))
print(id(foo))
x()

# 练习
def foo():
	print("foo")

foo = 10
foo()

'''

# ******************  以函数作为函数参数   ******************
# import time
#
# def timer(func):
# 	# 计算开始时间
# 	s1 = time.time()
# 	# func功能代码
# 	func()
# 	# 计算结束时间
# 	s2 = time.time()
# 	# 计算时间差
# 	print("耗时时间：", s2 - s1)
#
# def foo():
# 	# foo功能代码
# 	print("foo功能开始")
# 	time.sleep(3)
# 	print("foo功能结束")
#
# def bar():
# 	# bar功能代码
# 	print("bar功能开始")
# 	time.sleep(4)
# 	print("bar功能结束")
#
# timer(bar)

# ******************  以函数作为函数返回值   ******************


# def test():
# 	x = 10
# 	return x
# ret = test()
# print(ret)




# def foo():
#
# 	print("foo功能")
# 	def bar():
# 		print("bar功能！")
# 		return 100
# 	return bar
#
# ret = foo()
# print("ret:",ret)

# def test():
# 	print("test")
# print(test())













