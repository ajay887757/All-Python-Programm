import os
fname=input("Enter Your file Name :")

if os.path.isfile(fname):
    print("File Exists :",fname)
    f=open(fname,"r")
    lcount=wcount=ccount=0
    for lines in f:
        lcount=lcount+1
        words=lines.split()
        wcount=wcount+len(words)
        ccount=ccount+len(lines)
    f.close()
    print(lcount)
    print(wcount)
    print(ccount)
else:
    print("File Not Exist :", fname)