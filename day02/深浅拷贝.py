# 案例1：变量赋值
l1 = [1,2,3]
l2 = l1 # 不是拷贝，完全指向一块内存空间
print(id(l1))
print(id(l2))
l2[1] = 200
print(l1)

l1 = [1,2,3,[4,5]]
l2 = l1 # 不是拷贝，完全指向一块内存空间
print(id(l1))
print(id(l2))
l2[3][0] = 200
print(l1)

# 案例2：浅拷贝：两种方式：切片和copy方法

l1 = [1,2,3,["yuan","alvin"]]
l2 = l1.copy()  # 等同于l2 = l1[:]
print(id(l1))
print(id(l2))
l2[1] = 200
print(l1)
l2[3][0] = "张三"
print(l1)

# 深拷贝
import copy
l1 = [1,2,3,["yuan","alvin"]]
l2 = copy.deepcopy(l1)
l2[3][0] = "张三"
print(l1)