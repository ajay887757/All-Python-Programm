import pickle
from emp_module import Employee

f=open("pickel_programm/emp.ser","wb")
while True:
    eno=int(input("Enter Employee No :"))
    ename=input("Enter Employee Name :")
    esal=float(input("Enter Employee Salary :"))
    eadd=input("Enter Employee Address :")
    e=Employee(eno,ename,esal,eadd)
    pickle.dump(e,f)
    option=input("Do you Want To Add More Record[yes/No]")
    if option.upper()=="NO":
        break
print("Serialization Completed")
