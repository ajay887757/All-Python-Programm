n=input("Enter Characters and digit:") #a3z2b4
j=''
for i in n:
    if i.isalpha():
        x=i
    else:
        j=j+x*int(i)
k=sorted(j)
print("".join(k))
