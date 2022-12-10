class A:
    a=888
    def __init__(self):
        self.b=999
    
class B(A):
    def __init__(self):
        self.b=20
    def m1(self):
        # print(self.a)
        # print(self.b)
        print(super().a)
        # print(super().b)
        print(self.b)

b=B()
b.m1()