x=list(input("Enter Any String"))
y=input("You want to delete")
for i in x:
    if i==y:
        s=x.index(y)
        del x[s]
        f="".join(x)
print(f)
