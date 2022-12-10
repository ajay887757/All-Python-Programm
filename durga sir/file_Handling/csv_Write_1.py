import csv
f=open("file_Handling/1st_csv.csv","w",newline="")
w=csv.writer(f)
w.writerow(["ENO","ENAME","ESAL","EADD"])
while True:
    eno=int(input("Enter Eno :"))
    ename=input("Enter Ename :")
    esal=float(input("Enter Esal :"))
    eadd=input("Enter Eadd :")
    w.writerow([eno,ename,esal,eadd])
    option=input("Do you Want to add more records[yes/no] :")
    if option.lower()=="no":
        break
f.close()
print("Writing file successfully")