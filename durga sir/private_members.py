class Test:
    def __init__(self):
        self.__x=10
    
    def __m1(self):
        print("Private Method")

    def m2(self):
        print(self.__x)

t=Test()
t.m2()
# t.__m1()
# print(t.__x)
print(t._Test__x)
t._Test__m1()