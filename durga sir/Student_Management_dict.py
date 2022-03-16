s=input("Enter Student Name:").split()
m=input("Enter Marks Of Students:").split()
d={}
i=0
while i<len(s):
    d[s[i]]=m[i]
    i=i+1
print(d)
f=input("Enter Student Name you want to find")
if f in d:
    print(d[f])
else:
    print(f,"Student not available")
