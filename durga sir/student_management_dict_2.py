s=input("Enter Student Name").split()
m=input("Enter Marks :").split()
d={}
i=0
while i<len(s):
    d[s[i]]=m[i]
    i=i+1
#print(d)
print("#"*30)
print("Name\t\tMarks")
for k,v in d.items():
    print(k,"\t\t",v)
print("#"*30)

f=input("Enter Student You Want to Find:")
if f in d:
    print(d[f])
else:
    print(f,"Student Not Available")
