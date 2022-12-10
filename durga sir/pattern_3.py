n=int(input("Enter Row"))
m=int(input("Enter Colomn"))
for i in range(n):
    for j in range(m):
        print(chr(65+j)+" ",end="")
    print()
        
