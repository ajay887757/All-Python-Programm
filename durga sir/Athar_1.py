n=int(input())
x=int(input())
y=int(input())
z=int(input())
l=[]
c=0
t= (1*x)+(2*y)+(3*z)
for i in range(n):
    p=int(input())
    l.append(p)

for j in l:
    if j<=t:
        c=c+1
print(c)



