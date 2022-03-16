d={}
n=int(input("Enter How Many Student you add:"))
i=0
#for i in range(n):
while i<n:
    s=input("Enter Student Name:")
    m=input("Enter Student Marks:")
    d.setdefault(s,m)
    i=i+1
print(d)
f=input("Enter Student Name you Want to find:")
if f in d:
    print(d[f])
else:
    print(f,"is not avialable")
