n=int(input())
t=int(input())  #60
T=[]
B=[]
energy=0
count=0
for i in range(n):
    x=int(input())
    T.append(x)
for i in range(n):
    y=int(input())
    B.append(y)
while(t>0):
    m=min(T)
    t1=T.index(m)
    t=t-T[t1]
    energy=energy+B[t1]
    T.remove(T[t1])
    B.remove(B[t1])
    if len(T)==0:
        break
print(energy)
   


    
