class Engine:
    def m1(self):
        print("Engine Class Functionality")
    
class Car:
    def __init__(self):
        print("Car Class Constructor Execution")
        self.engine=Engine()
    
    def m2(self):
        print("Required Engine Class Functionality")
        self.engine.m1()
c=Car()
c.m2()