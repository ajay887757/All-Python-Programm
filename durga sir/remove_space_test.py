x=input("Enter Any String")
x=list(x)
for i in x:
    if i==chr(32):
        print(end="")
    else:
        print(i,end="")
