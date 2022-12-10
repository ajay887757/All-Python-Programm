class P:
    a=10
    def __init__(self):
        print("Parent Class constructor")
        self.b=20
    
    def m1(self):
        print("Parent Class Instance Method")
    @classmethod
    def m2(cls):
        print("Parent Class Class Method")
    @staticmethod
    def m3():
        print("Parent Class Static Method")

class C(P):
    # def m1(self):
    #     print("Inside Child Class")
    #     super().m1()
    #     print(self.a)
    pass

c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
