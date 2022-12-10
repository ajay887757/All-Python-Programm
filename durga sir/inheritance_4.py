class Car:
    def __init__(self,cname,model,color):
        self.cname=cname
        self.model=model
        self.color=color

    def carinfo(self):
        print("\tCar Name:{}\n\tModel:{}\n\tColor:{}".format(self.cname,self.model,self.color))

class Person:
    def __init__(self , name,age) :
        self.name=name
        self.age=age
    
    def eatndrink(self):
        print("Eat Biriyani and drink Beer")
    @staticmethod
    def ajay(x,y):
        z1="The Sum"
        z=x+y
        return z1+" "+str(z)
class Employee(Person):
    def __init__(self, name, age, eno, esal,car):
        super().__init__(name, age)
        self.eno=eno
        self.esal=esal
        self.car=car
    
    def work(self):
        print("Coding Python Program")
    
    def EmpInfo(self):
        print("Employee Name: ", self.name)
        print("Employee Age: ", self.age)
        print("Employee Eno: ", self.eno)
        print("Employee Salary: ", self.esal)
        print("Car Informations")
        self.car.carinfo()
        self.eatndrink()
        self.work()
        print(self.ajay(12,67))
c=Car("Innova","2.5V","Gray")
emp=Employee('Ajay',20,84821,10000,c)
emp.eatndrink()
emp.work()
emp.EmpInfo()


        