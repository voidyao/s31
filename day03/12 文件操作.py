


# 打开文件  open

#*********************** 读字符 ***********************

# f = open("满江红","r",encoding="utf8")
# print(f,type(f))

# 读文件    read()   aredline  readlines

# 读取全部数据
# data = f.read()
# print(data)
# 读取指定个数的数据
# data = f.read(3)
# print(data)
# print(f.readline())
# print(f.readlines())

# 循环一个文件
# for line in f:
# 	print(line,end="")
#*********************** 读字节 ***********************

# f = open("满江红","rb")
# data = f.read()
# print(data)
# print(data.decode())

# data = f.read(4)
# print(data.decode())


#*********************** 写文件 ***********************

# f = open("满江红new","a",encoding="utf8")
# f.write("满江红新作\n")
# f.writelines(["怒发冲冠，凭栏处、潇潇雨歇。\n","抬望眼、仰天长啸，壮怀激烈。\n"])
# f.close()


#*********************** seek tell ***********************

f = open("满江红","r",encoding="utf8")
f.read(3)
print(f.tell()) # 9个字节

f.seek(27)
data = f.read(2)
print(data)

