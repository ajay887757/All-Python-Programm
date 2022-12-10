class P:
    def m1(self):
        print("Parent Class Method")
class C(P):
    def m2(self):
        print("Chlid Class Method")

c=C()
c.m1()
c.m2()