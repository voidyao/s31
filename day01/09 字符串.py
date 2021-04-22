
# （1） 转义符

# s1 = "yuan"
# print(type(s1)) # <class 'str'>
#
# s2 = "hi,yuan \nhello world"
# print(s2)
#
# s3 = "D:\\nythonProject\\nenv\\Scripts\\python.exe"
# print(s3)
#
# # （2） 长字符串
#
# s4 = '''
# yuan
#    alvin
#       eric
# '''
# print(s4)

# （3）格式化输出

name = input("姓名>>")
age = input("年龄>>")
print(name) #  "yuan"
print(age) #   "23"  input函数返回的一定是字符串类型
print(type(name))
print(type(age))
# name = "yuan"
# age = 29

s5 = "我的姓名：%s，我的年龄：%s"%(name,age)
print(s5)

