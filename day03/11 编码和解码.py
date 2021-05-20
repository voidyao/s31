


s = "苑昊"

print(type(s))

# 编码方法
b1 = s.encode()
b2 = s.encode("GBK")
print(b1,len(b1))
print(b2,len(b2))
# 解码方法
print(b1.decode("GBK"))
# print(b2.decode())