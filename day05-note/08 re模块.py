import re

# ret = re.findall("world","hello worlds hi world")
# print(ret)
# ************  元字符 ************

# . ^ $

# ret = re.findall("^hello python$","hello python")
# print(ret)
# .匹配除了换行符以外所有符号
# ret = re.findall("hello .....","hello world")
# print(ret)

# *:[0,无穷] +:[1,无穷] ?:[0,1]    {m,n}:[m,n]   ():分组

# ret = re.findall("^hello a{2,7}","hello a")
# print(ret)

# ret = re.findall("hello .{5}","hello python,hello world,hello re,hello yuan")
# print(ret)
# ret = re.findall("hello .{2,5}","hello python,hello world,hello re")
# print(ret)
# ret = re.findall("hello .{5},","hello python,hello world,hello re")
# print(ret)

# ret = re.findall("hello .*","hello python,hello world,hello re,hello yuan,")
# print(ret)
# ret = re.findall("hello (.*?),","hello python,hello world,hello re,hello yuan,alvin,")
# print(ret)

# [] | \
# ret = re.findall("a[b,c]e","abeaeadeabce")
# print(ret)
# ret = re.findall("[^1-9]+","ab24ea37ead6ea$bce")
# print(ret)
# ret = re.findall("[a-zA-Z]+","ab24ea37ead6ea$bce")
# print(ret)
# ret = re.findall("www\.([a-zA-Z]+)\.(?:com|cn)","www.baidu.com,www.jd.cn,www.python.org")
# print(ret)

# \ 转义符： 将有特殊功能的元字符转换为普通符号
# \ 转义符： 将有普通符号转换为有特殊功能的符号   \d  \w

# ret = re.findall("\d+","ab24ea37ead6ea$bce")
# print(ret)
# ret = re.findall("\w+","ab24ea37ead6ea$bce")
# print(ret)

# ************  方法   ************

# 只能匹配第一个符合条件的对象
ret = re.search("\d+","abc12cd45e")
print(ret)
print(ret.group())


ret = re.search("www\.(?P<name>[a-zA-Z]+)\.(com|cn)","www.baidu.com,www.jd.cn,www.python.org")
print(ret.group())
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group("name"))

# match等同于search，只是多一个开始匹配
# ret = re.match("\d+","67abc12cd45e")
# print(ret)
# print(ret.group())

# 先编译规则再匹配
comp = re.compile("\d+")
rt = comp.search("67abc12cd45e")
ret = comp.search("abc12cd45e")
print(ret.group())

# split分割
ret = re.split("\d+","alvin34yuan23zhangsan45lisi67")
print(ret)

# sub 替换
ret = re.sub("(hello )(.*?)(,)","\\1yuan\\3","hello python,hello world,hello re, JS,")
print(ret)

