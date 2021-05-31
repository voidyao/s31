import re


with open("douban.html","r",encoding="utf8") as f:
	data = f.read()

# print(type(data))

ret = re.findall('<li>.*?<div class="item">.*?<span class="title">(.*?)</span>.*?<span class="rating_num".*?>(.*?)</span>.*?<span>(.*?)人评价</span>',data,re.S)
print(ret)

