n=input("Enter Any String:")
s=set(n)
print(s)
for ch in sorted(s):
    x=n.count(ch)
    print("Charcter {} present in {} times".format(ch,x))
