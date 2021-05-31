import sys


# print(sys.version)
# print(sys.platform)
# print(sys.path)
# sys.exit(0)
print("sys.argv",sys.argv)
if len(sys.argv)>1:
	_,user,pwd = sys.argv
else:
	user = input("用户名>>")
	pwd = input("密码>>")

if user == "yuan" and pwd == "123":
	print("登录成功")
else:
	print("登录失败")