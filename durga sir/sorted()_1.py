n=input("Enter String:") #aaaabbbccz
i=0
print(len(n))
while i<len(n):
    count=n.count(n[i])
    print(str(count)+n[i],end="")
    n=n[count:]
    i=i+1
        
