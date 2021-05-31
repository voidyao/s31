import os

print(os.getcwd())

# os.chdir("C:")
# print(os.getcwd())

# os.makedirs('dirname1/dirname2')

# print(os.listdir("D:\Codes\s31\day05"))

# 修改文件名
# os.rename("test.py","demo.py")

# 获取文件信息
# info = os.stat("D:\Codes\s31\day05\demo.py")
# print(info)

# ret = os.path.split("D:\Codes\s31\day05\demo.py")[1]
# print(ret)
#
# ret = os.path.basename("D:\Codes\s31\day05\demo.py")
# print(ret)
#
# ret = os.path.getsize("D:\Codes\s31\day05\demo.py")
# print(ret)

ret = os.path.join("/books/","2012/12/12")
print(ret)
