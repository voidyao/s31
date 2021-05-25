
def foo(z):
	x = 10
	y = 100
	def bar(): # bar函数此时为闭包函数
		# x =  100
		print(x)
		print(y)
		print(z)
		print("bar功能函数")

	return bar

func = foo()
func()
