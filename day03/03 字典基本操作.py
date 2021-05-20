

# info = {"name": "张三", "age": 23, "height": 180, "score": [67,78,88]}
info = {"name": "张三", "age": 23, "gneder":1,"is_yihun": True, "score": {"yuwen":78,"shuxue":88,"yingyu":99},"gf_names":["铁锤","二蛋"]}
print(info)


# 查询键的值
print(info["name"])
print(info["score"])
print(":::",info["score"]["yuwen"])
print("gf_names",info["gf_names"][1])


# 添加键值对: 如果键存在，修改键值，如果不存在，添加键值
info["gender"] = "male"
print(info)

# 删除键值
# print("is_yihun" in info)

if "is_yihun" in info:
    del info["is_yihun"]
# del info
print(info)











