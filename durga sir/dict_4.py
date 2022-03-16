word=input("Enter Any String")
d={}
for ch in word:
    d[ch]=d.get(ch,0)+1
print(d)

for k,v in sorted(d.items()):
    print(k,'occurs',v,'times')
