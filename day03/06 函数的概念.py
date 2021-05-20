'''
# 1 打印菱形
rows = 6
i = j = k = 1
# 菱形的上半部分
for i in range(rows):
	for j in range(rows - i):
		print(" ", end=" ")
		j += 1
	for k in range(2 * i - 1):
		print("*", end=" ")
		k += 1
	print("\n")

# 菱形的下半部分
for i in range(rows):
	for j in range(i):
		print(" ", end=" ")
		j += 1
	for k in range(2 * (rows - i) - 1):
		print("*", end=" ")
		k += 1
	print("\n")

# 2 计算1-100的和
ret = 0
for i in range(1,101):
	ret+=i
print(ret)

# 3 再次打印菱形
rows = 6
i = j = k = 1
# 菱形的上半部分
for i in range(rows):
	for j in range(rows - i):
		print(" ", end=" ")
		j += 1
	for k in range(2 * i - 1):
		print("*", end=" ")
		k += 1
	print("\n")

# 菱形的下半部分
for i in range(rows):
	for j in range(i):
		print(" ", end=" ")
		j += 1
	for k in range(2 * (rows - i) - 1):
		print("*", end=" ")
		k += 1
	print("\n")
'''



def print_ling():
	rows = 6
	i = j = k = 1
	# 菱形的上半部分
	for i in range(rows):
		for j in range(rows - i):
			print(" ", end=" ")
			j += 1
		for k in range(2 * i - 1):
			print("*", end=" ")
			k += 1
		print("\n")

	# 菱形的下半部分
	for i in range(rows):
		for j in range(i):
			print(" ", end=" ")
			j += 1
		for k in range(2 * (rows - i) - 1):
			print("*", end=" ")
			k += 1
		print("\n")

def cal_sum(n):
	# 计算1-100的和
	ret = 0
	for i in range(1, n+1):
		ret += i
	print(ret)




print_ling()
cal_sum(100)
print_ling()
cal_sum(101)








