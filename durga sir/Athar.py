n=int(input("Enter Any Number you want to create List"))
j=1
li=[]
for i in range(n):
    y=int(input("Enter List {}: ".format(j)))
    li.append(y)
    j=j+1
print(li)

print("The Sum Of List Is",sum(li))
