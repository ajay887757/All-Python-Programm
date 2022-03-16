n=int(input("Enter Nu"))
t=int(input("Enter Time "))
t1=[]   
b=[]

e=0

for i in range(n):
    k=int(input())
    t1.append(k)

for j in range(n):
    l=int(input())
    b.append(l)


while t>0:
    m=min(t1)
    index=t1.index(m)  #0
    e=e+b[index]
    t=t-m
    t1.pop(index)
    b.pop(index)
    if len(t1)==0:
        break

print("e",e)
    


