


# s = {1,2,3,9}
# print(s,type(s))

# (1) 去重功能
# l = [1,2,3,3,5,1]
# s = set(l)
# print(s) # {1,2,3,5}
# new_l =list(s)
# print(new_l)

# (2) 访问元素
# for i in s:
# 	print(i)


# 内置方法

# a = {1,2,3,4}
# （1）添加元素
# a.add(5)
# print(a)

# （2） 更新元素
# a.update({3,4,5})
# print(a) # {1, 2, 3, 4, 5}

# （3）删除元素
# remove：删除元素不存在报Key错误
# a.remove(6)
# print(a)
# discard： 删除元素不存在不报错
# a.discard(6)
# a.pop()
# print(a)
# 清空集合
# a.clear()

# （4） 集合操作
a = {1,2,3,4}
b = {3,4,5,6}
# 交集
# ret = a.intersection(b)
# print(ret)
# ret = b.intersection(a)
# print(ret)

# 并集
# a.update(b)
# print(a)
# ret2 = a.union(b)
# print(ret2)
# ret2 = b.union(a)
# print(ret2)

# 差集
ret3 = a.difference(b)
print(ret3)
ret3 = b.difference(a)
print(ret3)

# 对称差集
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))


















