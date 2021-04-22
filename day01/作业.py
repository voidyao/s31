"""

1. 分析下面代码的运行结果?

x = 10
y = x
y = 20
print(x)
print(y)

2. 用print打印出下面内容：

文能提笔安天下,
武能上马定乾坤。
心存谋略何人胜,
古今英雄唯是君。

3.  利用 input函数,连续输入两个数字求和？

4.  分别使用%占位符以及format方法两种方式制作趣味模板程序需求：
    等待用户输名字、地址、爱好，
    根据用户的名字和爱好进任意格式化输出
    如：敬爱可亲的xxx，最喜欢在xxx地方法xxx

5. 有 names = "  张三 李四 王五 赵六 "
   将names字符串中所有的名字放在一个列表中

6. 查找字符串"  张三 李四 王五 赵六 "王五的索引位置

7. 将十进制1025分别转换为二进制,八进制以及十六进制

8. 将"goods"与"food"以及"meat"拼接为完整路径,即"/goods/food/meat/"

9. s = "hello world"切片操作
   (1) s[1:4]
   (2) s[-1:-4]
   (3) 打印"world"如何切片

10. "1" == 1的结果是什么？结果是什么数据类型

"""
#1
x = 10
y = x
y = 20
print(x)
print(y)

#2
s1 = '''
文能提笔安天下,
武能上马定乾坤。
心存谋略何人胜,
古今英雄唯是君。
'''
print(s1)

#3
num1 = input("num1: ")
num2 = input("num2: ")
sum = int(num1) + int(num2)
print(sum)

#4
name = input("name: ")
address = input("address: ")
hobby = input("hobby: ")
print("敬爱可亲的%s，最喜欢在%s地方法%s"%(name,address,hobby))

#5
names = "  张三 李四 王五 赵六 "
ret = names.strip().split()
for i in ret:
    print(i)
#6
str0 = "  张三 李四 王五 赵六 "
print(str0.find("王五"))

#7
num = 1025
print(bin(num))
print(oct(num))
print(hex(num))

#8
str1 = "goods"
str2 = "food"
str3 = "meat"
str4 = "/" + "/".join([str1,str2,str3]) + "/"
print(str4)

#9
s = "hello world"
print(s[1:4])
print(s[-1:-4:-1])
print(s[6:])

#10
print("1" == 1)
print(type("1" == 1))