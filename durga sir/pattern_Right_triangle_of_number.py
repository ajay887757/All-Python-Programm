n=int(input("Enter number"))
for i in range(n):#0 to n-1
    for j in range(i+1):
        print(str(j)+" ",end="")
    print()
