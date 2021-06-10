




import sys

print(sys.argv)

l= sys.argv

print(l.index("-u"))
print(l.index("-p"))

user_index = l.index("-u") + 1
pwd_index = l.index("-p") + 1

user = l[user_index]
pwd = l[pwd_index]

if user == "yuan" and pwd == "123":
    print("登录成功")
else:
    print("登录失败")




