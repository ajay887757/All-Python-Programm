from zipfile import *
f=ZipFile("file_Handling/zip_file.zip","r",ZIP_STORED)
names=f.namelist()
# print(names)

for name in names:
    f=open(name,"r")
    data=f.read()
    print(data)
    
