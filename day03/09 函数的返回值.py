def add(x,y):

	# print(x+y)
	z = x + y
	return z # 如果没有retrun语句，默认返回None

ret = add(2,3)
print(ret)


def login(user,pwd):
	state = False
	if user=="yuan" and pwd==123:
		state = True
		return state,user
	else:
		return state

ret = login("yuan",123)
print("ret:",ret)
a,b = login("yuan",123)
print(a,b)