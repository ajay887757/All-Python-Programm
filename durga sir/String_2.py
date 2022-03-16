#n='ABAABBCA'
#output=4A3B1C
n=input("Enter Digit Along with chracters:")
d={}
for ch in n:
    d[ch]=d.get(ch,0)+1
print(d)

for k,v in sorted(d.items()):
    print(str(v)+k,end="")
