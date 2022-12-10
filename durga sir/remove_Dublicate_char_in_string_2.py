s=input("Enter Any String:")
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
print("".join(l))
