# 声明类
class Person(object):
    legs_num = 2
    has_emotion = True

    def __init__(self, name, age, gender="male"):
        print("self", self)
        self.name = name
        self.age = age
        self.gender = gender


    def play_fire(self):
        print(self.name+"在玩火")

    def think(self):
        print("思考")

# 创建实例对象
p1 = Person("yuan", 34,"male")
p1.play_fire()

p2 = Person("alvin",23)
p2.play_fire()

