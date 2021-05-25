import time
def decorator(func):

	def timer():
		# 计算开始时间
		s1 = time.time()
		# func功能代码
		ret = func()
		# 计算结束时间
		s2 = time.time()
		# 计算时间差
		print("耗时时间：", s2 - s1)

		return ret

	return timer

@decorator  # foo =  decorator(foo)
def foo():
	# foo功能代码
	print("foo功能开始")
	time.sleep(3)
	print("foo功能结束")
	return "foo函数"


@decorator
def bar():
	# bar功能代码
	print("bar功能开始")
	time.sleep(4)
	print("bar功能结束")
	return "bar函数"

ret = bar()
print("ret:",ret)











