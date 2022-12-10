n=input("Enter String")
l=n.split()
l1=[]
for word in l:
    l1.append(word[::-1])
print(l1)
output=""
print(" ".join(l1))
