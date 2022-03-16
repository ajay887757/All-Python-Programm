n=input("Enter Any String")
l=n.split()
r=reversed(l)
#print(" ".join(r))
for i in r:
    print(str(i)+" ",end="")
