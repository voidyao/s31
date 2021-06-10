
class Base:
    def __foo(self): # _Base__foo
        print("foo from Base")

    def test(self):
        self.__foo() # self._Base__foo

class Son(Base):
    def __foo(self): # _Son__foo
        print("foo from Son")

s=Son()
s.test()