
# x = 1000  # 全局变量
def foo():
	# x = 100  # enclosing 变量
	def inner():
		x = 10  # local变量
		print(x)
		# print(sum)
	inner()

def bar():
	x = 34
	z = 23

foo()



