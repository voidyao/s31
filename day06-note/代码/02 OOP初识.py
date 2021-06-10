
# 声明类
class Person(object):
    legs_num = 2
    has_emotion = True

    def play_fire(self):
        print("玩火")

    def think(self):
        print("思考")
# 类对象
print(Person)

# 创建实例对象
p1 = Person()
print(p1)
p2 = Person()
print(p2)

print(p1.legs_num)
print(p2.legs_num)

p1.play_fire()

# 实例属性赋值操作
p1.name = "张三"
p1.age = 22

p2.name  = "李四"
# 实例属性取值操作
print(p1.name)
print(p1.age)
print(p2.name)

p2.legs_num = 4
print(p2.legs_num)


