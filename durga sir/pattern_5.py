n=int(input("Enter number"))
c=0
for i in range(n):#0 to n-1
    for j in range(n):
        print(str(c)+" ",end="")
        c+=1
    print()
