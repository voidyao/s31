
class Students(object):
    role = "学生"
    class_name = "s31"
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

    @staticmethod   # 静态方法
    def add(x, y):
        print(x + y)

    # @staticmethod
    # def print_info():
    #     print("这是一个%s班级的%s类"%(Student.cls,Student.role))

    # 类方法
    @classmethod
    def print_info(cls):
        print("这是一个%s班级的%s类" % (cls.class_name, cls.role))


s1 = Students(1001, "张三")
# 静态方法
# s1.add(2,4)
# Student.add(4,5)
# 类方法
s1.print_info()
Students.print_info()
