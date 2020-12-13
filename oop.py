from oop_classes import C


class A(C):
    class B:
        def method1():
            print("")
    
    def method1(self):
        pass

    arg2 = "123"

    def __init__(self, a=None):
        self.arg1 = a
    
    def _method2(self):
        print(self.arg2)
    
    def __method3(self):
        print("private", self.arg1)


C = A

a = C('3')

# a._method2()


def dec1(func):
    def wrapper(a):
        print('123')
        func(a * 2)
    
    return wrapper


@dec1
def tempo(a=0):
    print(a)


# tempo(1)


class D:
    @staticmethod
    def static():
        pass

    @classmethod
    def classmeth(cls):
        cls.static()


class E:
    def m(self):
        pass

    class Meta:
        pass


# D.classmeth()
