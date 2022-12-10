class A:
    def __init__(self) :
        print("A Class constructor")

    def m1(self):
        print("A class Instance method")
    
    @classmethod

    def m2(cls):
        print("A Class Classmethod")
    
    @staticmethod

    def m3():
        print("A class Static Method")

class B(A):
    def __init__(self):
        print("B class Constructor")
    def m1(self):
        super().m1()
        super().m2()
        super().m3()
        super().__init__()

        print("Using Class name",end=" ")
        A.m3()
        print()
        A.m2()
        print()
        A.m1(self)
        A.__init__(self)

b=B()
b.m1()
