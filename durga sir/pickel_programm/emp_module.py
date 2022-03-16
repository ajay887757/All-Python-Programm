class Employee:
    def __init__(self,eno,ename,esal,eadd):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eadd=eadd
    def display(self):
        print("Employee No :{} , Emoloyee Name: {},Employee Salary :{},Employee Address :{}"
        .format(self.eno,self.ename,self.esal,self.eadd))

