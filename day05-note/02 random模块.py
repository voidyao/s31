import random

# 获取0-1的随机浮点型数字
print(random.random()*10)
print(random.randint(1,3))
print(random.randrange(1,3))
print(random.choice([111,"hello",333]))
print(random.sample([111,"hello",333],2))
print(random.uniform(1,3))
l = [1,2,3,4,5,6]
random.shuffle(l)
print(l)

# 随机验证码案例

def random_code():
	s = ""
	for i in range(5):
		random_int = str(random.randint(1, 9))
		upper_alpha = chr(random.randint(65, 90))
		lower_alpha = chr(random.randint(97, 122))
		ramdom_char = random.choice([random_int, upper_alpha, lower_alpha])
		# print(ramdom_char)
		s += ramdom_char
	return s

ret = random_code()
print(ret)