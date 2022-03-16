x=6
oprator=input()
s=0
if oprator.startswith("++"):
    s=int(oprator[2:])+1
    print(s)
else:
    s=int(oprator[:-2])
    print(s)



# x=5
# y=++x
# print(y)