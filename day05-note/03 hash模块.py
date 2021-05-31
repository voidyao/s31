import hashlib

md5 = hashlib.sha3_256()
print(md5)

md5.update(b"hi,yuan")
print(md5.hexdigest())
print(len(md5.hexdigest()))

# 多次更新
md5.update(b"hi,world")
print(md5.hexdigest()) # de4fec393ddd7261ee927adead8de05e