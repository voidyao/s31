# 声明一个类

class Teacher(object):
    role = "老师"
    def __init__(self,name):
        self.name = name

class Student(object):
    role = "学生"
    cls = "s31"
    # 初始化方法
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
    # 实例方法
    def study(self):
        print("%s在学习" % self.name)

    # 实例方法
    def ask(self, obj):
        print("%s正在向%s %s提问题" % (self.name,obj.role,obj.name))

# 创建实例对象:  类名()
s1 = Student(1001, "张三")
s2 = Student(1002, "李四")
yuan = Teacher("yuan")

# 张三向李四提问题
s1.ask(s2)
# 张三向yuan提问题
s1.ask(yuan)


####


# 类对象
# 类属性
# 实例对象: 类名()
# 实例属性
# 实例方法

s1.role = "xxx"
# print(Student.role)
# print(Student.cls)
Student.role = "xxxx"
print(s1.role)
print(Student.role)

# 实例对象调用实例方法
s1.study()
# 类对象可不可以调用实例方法
Student.study(s1)

