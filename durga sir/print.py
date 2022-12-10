name=input("Enter Any Name:")
salary=float(input("Enter Salary"))
gf=input("Enter GF name:")

print('Hello {}, your Salary is {}, and your Friend {} waiting '.format(name,salary,gf))
print('Hello {0}, your Salary is {1}, and your Friend {2} waiting '.format(name,salary,gf))
print('Hello {1}, your Salary is {2}, and your Friend {0} waiting '.format(name,salary,gf))


print("===================Using Key value Result=====================")

print('Hello {n}, your Salary is {s}, and your Friend {f} waiting '.format(n=name,s=salary,f=gf))

