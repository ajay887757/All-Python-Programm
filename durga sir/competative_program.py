

l=[]
l1=[]

for i in range(int(input("Enter Number "))):  #1 ,2
    y=input("Enter Element ")
    print(y)
    for j in y:
        j=int(j)
        l.append(j)

    if int(y[1])==0:

        l1.append(y[:2])
    l.append(None)

print("l1=",l1)

print("l =",l)

s=int(l1[0])**l[-3]*l[-2]
print(s)

# print(l1)
# p=l[:2]
# print(p)


# l=[1,2,3,4,0,55,34,23,234,53,12]
# print(l[:4])
# print(l[4:])
# l.append(None)
# print(l)