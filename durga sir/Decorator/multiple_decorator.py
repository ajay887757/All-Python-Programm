def deco1(func):
    def inner1():
        print("Decorator_1 execution")
        func()
    return inner1
def deco2(func):
    def inner2():
        print("Decorator_2 execution")
        func()
    return inner2

@deco2
@deco1
def f():
    print("Original Function")
f()