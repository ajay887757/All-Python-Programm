class Employee:
    def __init__(self,ename,esal,age):
        self.ename=ename
        self.esal=esal
        self.age=age

    def display(self):
        print("Employe Name Is ",self.ename)
        print("Employee sal Is ",self.esal)
        print("Employee Age is",self.age)


class UpdateEsal:
    def esal_update(emp,newsal):
        emp.esal=newsal

    
emp=Employee("Ajay",1000,12)
i=input("enter New salary:")
UpdateEsal.esal_update(emp,i)
emp.display()
        
