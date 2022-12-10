n=list(input("Enter Your Name"))
for i in n:
    if ord(i)==32:
        r=n.index(i)
        del n[r]
print("".join(n))
        
        
