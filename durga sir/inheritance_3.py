class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def eatndrink(self):
        print("Ear Biriyani And Drink Beer")

class Empolyee(Person):
    def __init__(self, name, age , esal,eno):
        self.eno=eno
        self.esal=esal
        super().__init__(name, age)
    
    def work(self):
        print("Coding Python Program")
    
    def empInfo(self):
        print("Empolyee Name :",self.name)
        print("Empolyee Age :",self.age)
        print("Empolyee Number :",self.eno)
        print("Empolyee Salary :",self.esal)

emp=Empolyee("Ajay",20,10000,84821)
emp.eatndrink()
emp.work()
emp.empInfo()