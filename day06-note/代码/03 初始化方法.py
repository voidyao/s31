# 声明类
class Person(object):
    legs_num = 2
    has_emotion = True

    def __init__(self, name, age, gender):
        print("self", self)
        self.name = name
        self.age = age
        self.gender = gender

    def play_fire(self):
        print("玩火")

    def think(self):
        print("思考")

# 创建实例对象
p1 = Person("yuan", 34, "male")
print("p1", p1)
p1.height = 180
p2 = Person("alvin",22,"male")
print(p2.name)
