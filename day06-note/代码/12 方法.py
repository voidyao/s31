class Animal(object):
    def sleep(self):
        print("睡觉80行")

    def eat(self):
        print("干饭")



class Tuoniao(Animal):

    def jump(self):
        print("跳")
    def fly(self):
        print("Animal 飞")

t1 = Tuoniao()
print(type("hiyuan"))
print(type(t1)) # <class '__main__.Tuoniao'>

print(isinstance(t1,Tuoniao)) # True
print(isinstance(t1,Animal)) # True

print(type(t1) == Tuoniao)
print(type(t1) == Animal)

#  dir内置函数 和 __dict__的区别


class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def test(self):
        pass


yuan = Student("yuan", 100)
print("获取所有的属性列表")
print(dir(yuan))

print("获取自定义属性字段")
print(yuan.__dict__)

print(yuan.__class__ == Student)