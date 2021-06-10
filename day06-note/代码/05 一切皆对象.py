# s = "hello wolrd"
# s2 = str("hi,yuan")
# print(type(s2))
# print(s2.upper())
# l = [1, 2, 3]
# l2 = list((1, 2, 3))
# print(type(l2))

# def foo(a):
#     a = 100
#     print(a)
# a = 10
# foo(a)
# print(a)

# def bar(l):
#     l = [2,3]
#     l.append(4)
#     print("foo l",l)
# l = [1,2,3]
# bar(l)
# print("global l",l)


class Weapon:

    def __init__(self, name, av, color):
        self.name = name
        self.av = av
        self.color = color

jiguangqiang = Weapon("激光枪", 100, "red")


class Hero:

    def __init__(self, name, sex, hp, ce, weapon,level=2,exp=2000, money=10000):  # 类必不可少的方法,用于实例化
        self.name = name  # 英雄的名字
        self.sex = sex  # 英雄的性别
        self.hp = hp  # 英雄生命值
        self.level = level  # 英雄的等级
        self.exp = exp  # 英雄的经验值
        self.money = money  # 英雄的金币
        self.weapon = weapon

yuan = Hero("yuan", "male", 100, 80,jiguangqiang)
print(yuan.name.upper())
print(yuan.weapon.color)
