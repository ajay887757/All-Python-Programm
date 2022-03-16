class Test:
    def m1(self,*args):
        total=0
        for i in args:
            total=total+i
        print("The Sum:",total)

t=Test()
t.m1()
t.m1(10,20,30)
t.m1(30,40,50,60,70)