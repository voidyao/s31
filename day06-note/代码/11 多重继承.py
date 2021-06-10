class Animal(object):
    def sleep(self):
        print("睡觉80行")

    def eat(self):
        print("干饭")

    def fly(self):
        print("Animal 飞")


class Fly(object):
    def fly(self):
        print("Fly 飞")

class Bat(Animal, Fly):
    pass


class Tuoniao(Fly,Animal ):

    def jump(self):
        print("跳")


t1 = Tuoniao()
t1.fly()
t1.sleep()
