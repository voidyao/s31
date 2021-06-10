
class Animal(object):
    def sleep(self):
        print("睡觉80行")

    def eat(self):
        print("干饭")

    # def spark(self):
    #     print("spark...")





class Dog(Animal):

    def spark(self):
        print("狂吠")

class Cat(Animal):
    def catch_mouse(self):
        print("抓老鼠")

    def sleep(self):
        # 方式1:
        # Animal.sleep(self)
        # 方式2:super
        # super(Cat,self).sleep()
        super().sleep()
        print("睡觉over")

# zhangsan = Dog()
# zhangsan.spark()
# zhangsan.sleep()

huahua = Cat()
huahua.sleep()


