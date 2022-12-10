from black import out
from numpy import inner


def Outer():
    # print("Outer Function Executed")
    def inner():
        print("Inner Function")

    return inner

inner1=Outer()
inner1()
