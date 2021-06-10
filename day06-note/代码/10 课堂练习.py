class A(object):

    def foo(self):
        print("A foo...")

    def bar(self):
        print("bar...")
        print(self.foo)


class B(A):
    def __init__(self, val):
        self.foo = val

    def foo(self):
        print("B foo...")


b = B("abc")
b.bar()
