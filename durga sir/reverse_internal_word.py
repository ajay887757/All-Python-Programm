n=input("Enter Any String")
k=n.split()
for i in k:
    r=reversed(i)
    j="".join(r)
    print(j+" ",end="")

