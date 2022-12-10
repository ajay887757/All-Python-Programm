import csv
with open("file_Handling/write.csv","w",newline="") as f:
    data=csv.writer(f)
    data.writerow(["Enrollment No","Student Name","Mobile No","Add"])
    while True:
        Enrollment_No=input("Enter Enrollment No :")
        Student_Name=input("Enter Student Name :")
        Mobile_No=input("Enter Mobile No :")
        Add=input("Enter Add :")
        data.writerow([Enrollment_No,Student_Name,Mobile_No,Add])
        option=input("Do want addd more data[yes/no] : ")
        if option.lower()=="no":
            break
print("data added succesfully")

    
    
