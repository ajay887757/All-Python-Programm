n=input("Enter string:")
l=[]
for ch in n:
    if ch not in l:
        l.append(ch)
for i in sorted(l):
    x=n.count(i)
    print("Charcter {} present in {} times".format(i,x))
