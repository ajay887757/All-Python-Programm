class A:
    def m1(self):
        print("A Class Method")
class B(A):
    def m1(self):
        print("B Class Method")
class C(B):
    def m1(self):
        print("C Class Method")
class D(C):
    def m1(self):
        print("D Class Method")
class E(D):
    def m1(self):
        print("E Class Method")
class F(E):
    def m1(self):
        super(B,self).m1()
        super(E,self).m1()

        C.m1(self)   # using Class name

        # print("F Class Method")

f=F()
f.m1()