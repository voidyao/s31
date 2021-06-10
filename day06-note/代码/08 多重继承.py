
class Animal(object):
    def sleep(self):
        print("睡觉")

    def eat(self):
        print("干饭")
    def spark(self):
        print("spark...")

class Dog(Animal):

    def spark(self):
        print("狂吠")

class Cat(Animal):
    def catch_mouse(self):
        print("抓老鼠")

zhangsan = Dog()
zhangsan.spark()
zhangsan.sleep()


