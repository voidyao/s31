


dic = {"names":["zhangsan","li"],"detail":{"k1":"v1"},"gender":None}
# data = dic["detail"]
# print(data["k1"])

print(dic["detail"]["k1"])
print(dic["names"][1])

# 循环列表
li = [111,222,333]
for i in li:
	print(i)

# 循环字典




info = {"name":"yuan","age":18}
# x = "name"
# print(info["x"])
# print(info["name"])

# for i in info:
# 	print(i,info[i])

# print("info.items()",info.items()) #[('name', 'yuan'), ('age', 18)]
# for item in info.items():
# 	print(item)

# a,b,*x = [111,222,333,444]
# print(a)
# print(b)
# print(x)

for item in info.items():
	print(item)

for key,val in info.items():
	print(key,val)



def foo():
	x = 10

# def bar():
# 	print(x)

print(x)





