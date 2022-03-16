class Test:
    def m1(self,a=None,b=None,c=None):
        if a is not None and b is not None and c is not None:
            print("3- arguments ")
        
        elif a is not None and b is not None:
            print("2-aguments ")
        
        elif a is not None:
            print("1- argument")
        
        else:
            print("No arguments")

t=Test()
t.m1()
t.m1(10)
t.m1(10,2)
t.m1(10,20,30)
# t.m1(10,20,30,40)  TypeError: m1() takes from 1 to 4 positional arguments but 5 were given