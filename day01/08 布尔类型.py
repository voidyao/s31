


b1 = True
b2 = False
print(type(b1)) # <class 'bool'>
print(type(b2))


x = 2 < 1
print(x) # True

print(1 == "1") # False


s = "yuan"
print(type(s)) # <class 'str'>

# 零值
a = bool(2>1)
print(a)

# b = bool(0)
b = bool(-1)
print(b)

# c = bool("")
# c = bool("-1")
c = bool("0")
print(c)


# 所谓零值，布尔为False的值：
# 在整形里0是零值，字符串里""是零值，列表中 [] 和字典中｛｝都是对应的零值。