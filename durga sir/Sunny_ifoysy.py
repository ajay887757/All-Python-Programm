# n=int(input())
# l=[]
# l1=[]
# for i in range(n):
#     x=int(input())
#     l.append(x)

# for j in l:
#     if n%j==0:
#         l1.append(j)

# m=max(l1)

# print("l",l)
# print("l1",l1)
# print("max",m)


n=int(input())
l=[]
l1=[]
l3=[]
for i in range(n):
    x=int(input())
    l.append(x)
k=2
i=0
for q in l:
    if n%q==0:
        l3.append(q)
m=max(l3)
print("m",m)

if m==2:
    for j in range(m):
        l1.append(l[i:k])
        k=k+2
        i=i+2
elif m==4:
    k=4
    for j in range(m):
        l1.append(l[i:k])
        k=k+4
        i=i+4
else:
    k=3
    for j in range(m):
        l1.append(l[i:k])
        k=k+3
        i=i+3


for i in l1: 
    if [] in l1:
        l1.remove([])

s=set(l)
j=1
isTrue=False
for i in s:
    if i in 
        print("true",i)

print("l",l)
print("l1",l1)
print("set",s)

