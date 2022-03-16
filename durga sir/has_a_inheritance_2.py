class Car:
    def __init__(self,carname,model,color):
        self.carname=carname
        self.model=model
        self.color=color

    def CarInfo(self):
        print("Car Name:{}, Model:{}, color:{}".format(self.carname,self.model,self.color))

class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    def EmpInfo(self):
        print("Employee Name:",self.ename)
        print("Employee Number:",self.eno)
        print("Car Info")
        self.car.CarInfo()
class Campany:
    def __init__(self,cname,emp):
        self.cname=cname
        self.emp=emp
    
    def show(self):
        print("Campany Name:",self.cname)
        print("Emp Information")
        self.emp.EmpInfo()
c=Car("Inova","2.4zx","Grey")
emp=Employee("Ajay",5,c)
cmp=Campany("Ajay Enterprises",emp)
cmp.show()
# emp.EmpInfo()