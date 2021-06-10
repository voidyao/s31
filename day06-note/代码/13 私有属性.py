

class Person(object):
    def foo(self):
        print(self._gender)  # _Person__score

class Student(Person):
    def __init__(self,name,score,gender):
        self.name = name
        self.__score = score   # _Student__score=99
        self._gender = gender

    def check_score(self):
        return self.__score # self._Student__score

    def set_score(self,new_score):
        if type(new_score) == int:
            self.__score = new_score
        else:
            print("非法输入")

s1 = Student("yuan",99,"male")
# print(s1.name)
# print(s1.__score)
# s1.check_score()
# print(s1._Student__score)
# s1._Student__score = 100

# s1.__score = 66
# print(s1.check_score())

# s1.set_score("hello world")
# print(s1.check_score())
# s1.name = 100


print(s1._gender)
s1.foo()
