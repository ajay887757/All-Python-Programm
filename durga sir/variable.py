class Test:
    school="Durgasoft"
    """Doc string"""
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def m1(self):
        print(self.name)
        print(self.rollno)
        print(self.school) #accesing static variable

    @classmethod
    def m2(cls):
        cls.a=10
        Test.b=20
        print(cls.a)
        print(Test.a)
    @staticmethod

    def m3():
        Test.c=30
        print("a is :",Test.a)
        print(Test.c)

t=Test("Ajay",101)
t.m1()
Test.m2()
print(t.a)

Test.m3()
print(t.__dict__)
print(Test.__dict__)
print(Test.c)

