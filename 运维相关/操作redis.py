import redis

r = redis.Redis(host= "172.16.1.25",port= "6379",password= "redis123")
ret = r.get("ettest:sortinginfo")
print(ret)