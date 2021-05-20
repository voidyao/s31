

# info = {"name": "张三", "age": 23, "height": 180, "score": [67,78,88]}
info = {"name": "张三", "age": 23, "gender":1,"is_yihun": True, "score": {"yuwen":78,"shuxue":88,"yingyu":99},"gf_names":["铁锤","二蛋"]}


# （1）查询相关操作

# 查询键的值
# print(info.get("names","yuan"))

# 查询所有的键
# print(info.keys()) # ['name', 'age', 'gneder', 'is_yihun', 'score', 'gf_names']
# 查询所有的值
# print(info.values()) # ['张三', 23, 1, True, {'yuwen': 78, 'shuxue': 88, 'yingyu': 99}, ['铁锤', '二蛋']]

# 查询所有的键和值
# print(info.items()) # [('name', '张三'), ('age', 23), ('gneder', 1), ('is_yihun', True), ('score', {'yuwen': 78, 'shuxue': 88, 'yingyu': 99}), ('gf_names', ['铁锤', '二蛋'])]

# 循环字典所有的键值
# for key in info:
# 	print(key,info.get(key))

# for i in [(1,2),(3,4),(5,6)]:
# 	print(i)

# for k,v in info.items():  # [('name', '张三'), ('age', 23), ('gneder', 1), ('is_yihun', True), ('score', {'yuwen': 78, 'shuxue': 88, 'yingyu': 99}), ('gf_names', ['铁锤', '二蛋'])]
# 	print(k,v)


# 删除键值对方法
# info.pop("gender")
# info.popitem() # 删除最后一个键值对
# print(info)
# 清空字典
# info.clear()
# print(info) # {}


# 更新键值对
# info.update({"is_yihun":False,"height":180})
# print(info)


# 添加键值对

print(info.get("height",180)) # 180
print(info)
print(info.setdefault("height",180))
print(info)









