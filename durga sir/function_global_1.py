a=10
def f1():
    global a
    print(a)
def f2():
    global b    #creating global variable inside the function
    b=20
    print(b)
def f3():
    print("This is a global variable",b)
def f4():
    a=45
    print("This is local variable",a)
f1()
f2()
f3()
f4()
