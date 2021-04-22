
# (1) 将字符串转换成整型和浮点型方法
# s = "123yuan"
s = "123"
num = int(s)
print(num)
print(type(num))
print(num+100)

s2 = "3.14"
num2 = float(s2)
print(num2)
print(type(num2))  #<class 'float'>

# （2）将数字或布尔值转换成字符串

num3 = 3.14
s3 = str(num3)
print(s3) # "3.14"
print(type(s3)) # <class 'str'>

s4 = str(True)
print(s4) # "True"
print(type(s4)) # str

# bool() 将整形浮点型或者字符串转换成布尔值的方法

print(bool(3.14)) # True
print(bool(0)) # False
print(bool("")) # False
print(bool("100")) # True

