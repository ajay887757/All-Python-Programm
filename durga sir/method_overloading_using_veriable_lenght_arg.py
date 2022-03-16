class Test:
    def m1(self,*args):
        print("{} - arguments".format(len(args)))

t=Test()
t.m1()
t.m1(10,20,30)
t.m1(10,20,30,10,20,30)


