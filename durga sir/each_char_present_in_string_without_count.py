#s='ABBACBA'
s=input("Enter String:")
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)

for k,v in sorted(d.items()):
    print('{} occures {} times'.format(k,v))
