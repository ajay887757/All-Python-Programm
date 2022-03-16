
class Employee:
    def __init__(self,name,salaryperday):
        self.name=name
        self.salaryperday=salaryperday
    def __mul__(self,others):
        return self.salaryperday*others.workingdays

    def __str__(self):
        return self.name

class TimeSheet:
    def __init__(self,name,workingdays):
        self.name =name
        self.workingdays=workingdays

    def __mul__(self,others):
        return self.workingdays*others.salaryperday

    def __str__(self):
        return self.name

e=Employee("Ajay",500)
t=TimeSheet("Ajay",25)

print("This month salary:",e*t)
print("This month salary:",t*e)

print("e Objecrt print:",e)
print("t Objecrt print",t)


