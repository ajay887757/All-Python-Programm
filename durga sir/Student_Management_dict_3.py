n=int(input("Enter Number of Student:"))
d={}
for i in range(n):
    s=input("Enter Student Name:")
    m=int(input("Marks of Student:"))
    d[s]=m
print("Student Data Inserted")
print('*'*40)
print('Name\t\tMarks')
for k,v in d.items():
    print(k,'\t\t',v)

print("Searching is Started")
while True:
    f=input("Enter Student Name To Find Marks")
    marks=d.get(f,-1)
    if marks==-1:
        print(f,"Student Is Not Available")
    else:
        print('Marks of ',f, 'are',marks)
        option=input("Do you want to Search another Student Marks(yes/no):").lower()
    if option=="no":
        break
    else:
        continue
print()
print("*"*40)

print()
print("Thank you ")

print()
print("*"*40)
        

    
