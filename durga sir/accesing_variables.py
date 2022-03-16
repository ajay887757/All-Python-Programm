class Test:
    a=10

    def __init__(self):
        self.b=20
        
    def m1(self):
        self.c=30
        self.a=888

t1=Test()
t2=Test()
Test.a=3444
print("t1", t1.a , t1.b )
print("t2", t2.a , t1.b )
t1.m1()
t1.a=9000
print("t1", t1.a , t1.b ,t1.c)
print("t2", t2.a , t1.b )
print("Test",Test.a ,t1.b)

print(t1.__dict__)
print(t1.a)