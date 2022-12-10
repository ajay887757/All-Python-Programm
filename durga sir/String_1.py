#n='ABAABBCA'
#output=4A3B1C
n=input("Enter Digitawith chracters:")
s=set(n)
print(s)

for ch in sorted(s):
    x=n.count(ch)
    print(str(x)+ch,end="")



