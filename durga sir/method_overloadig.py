class Test:
    def m1(self,a):
        print("{} type argument ".format(a.__class__.__name__))
    

t=Test()
t.m1("Ajay")
t.m1(10)
t.m1(12.25)
t.m1(20+30j)