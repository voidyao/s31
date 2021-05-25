

import json


# 序列化：  将本语言支持的数据对象转换成json格式的字符串
# 反序列化： 将json格式的字符串转换成本语言支持的数据对象

'''
json格式：
‘12’
'""'
‘true false’
‘[]’
'{}'
"null"
注意：支持双引号
'''
# *************** 序列化 *****************
# num = 100
# b = True
# ret = json.dumps(b)
# print(type(ret))
# print(repr(ret))

# data = {'name':"yuan",'age':18}
#
# json_str = json.dumps(data)
# print(repr(json_str))
#
# with open("a.txt","w",encoding="utf8") as f:
# 	f.write(json_str)

# *************** 反序列化 *****************

# with open("a.txt","r",encoding="utf8") as f:
# 	f_read= f.read()
# 	print("f_read",repr(f_read))
#
# 	data = json.loads(f_read)
# 	print(data,type(data))


# data = json.loads('{"name":"yuan","age":18,"is_married":true}')
# print(data,type(data))

# data = {"name":'yuan',"age":18,"is_married":True,"gender":None}
# print(json.dumps(data))


res = "{\"k1\":\"v1\",\"k2\":\"v2\"}"
data = json.loads(res)
print(data,type(data))





