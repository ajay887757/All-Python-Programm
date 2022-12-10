a=20
def f1():
    a=10
    print("Accessing Global variable",globals().get('a'))
    print("this is local variable",a)
f1()

def f2():
    a=1000
    print(globals())
f2()
