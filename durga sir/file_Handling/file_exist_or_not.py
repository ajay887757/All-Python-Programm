import os
f_name=input("Enter File Name :")

if os.path.isfile(f_name):
    print("file is Available",f_name)
    f=open(f_name,"r")
    print("*"*40)
    print(f.read())
    f.close()
else:
    print("File Is not exist",f_name)