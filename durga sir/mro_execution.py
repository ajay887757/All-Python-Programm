class A:
    def m1(self):
        print("A class Method")
class B(A):
    def m1(self):
        print("B class Method")
class C(B):
    def m1(self):
        print("C class Method")
class D(C):
    def m1(self):
        print("D class Method")
class E(D):
    def m1(self):
        # super().m1()
        super(D,self).m1()
        # print("E class Method")

e=E()
e.m1()
print(E.mro())

