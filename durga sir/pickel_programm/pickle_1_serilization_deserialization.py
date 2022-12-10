import pickle

class Student:
    def __init__(self,eno,name,Add):
        self.eno=eno
        self.name=name
        self.Add=Add
    def show(self):
        print("Employee Eno :",self.eno)
        print("Employee Name :",self.name)
        print("Empolyee Add :",self.Add)

s=Student(101 ,"Ajay Kumar ","Bhopal")
# s.show()

f= open("pickel_programm/stu.ser", "wb") 
pickle.dump(s,f)
print("Serialixation Completed")

f=open("stu.ser", "rb")
new_ob=pickle.load(f)
print("Deserlaization Successfully")
new_ob.show()
