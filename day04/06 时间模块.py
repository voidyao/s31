# 一个模块即一个py文件

import time

# 三种时间表达方式

# （1）时间戳
timestamp = time.time()
print(timestamp)

# （2）格式化的时间字符串
time_str = time.strftime("%Y/%m/%d  %H:%M")
# time_str = time.strftime("%Y/%m/%d  %X")
print(time_str)

# （3）时间元组
time_tuple = time.localtime()
print(time_tuple)
print(time_tuple[0])

# *********************** 三种时间表达方式相互转换 ***********************


# (1) 时间戳 －－－－>时间元组
t1 = time.localtime(5000)
print(t1)
# (2) 时间元组 ---> 时间戳
t2 = time.mktime(t1)
print(t2)

# (3) 结构化时间 －－－－> 字符串时间

t3 = time.localtime(5000)
print(t3)
t4 = time.strftime("%Y-%m-%d %X %a")
print(t4)

# （4） 字符串时间 ------>结构化时间
t5 = time.strptime("2017-03-16","%Y-%m-%d")
print(t5)

# time.sleep(0.2)







