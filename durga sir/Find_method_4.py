s1='abcdefghijklmnopqrstuvwxyz'
s2='zyxwvutsrqponmlkjihgfedcba'
x=input("Enter Any String")
try:
    for i in x:
        f=s1.index(i)
        u=s2[f]
        print(u,end='')
except:
    print("please don't enter space")
print()

#printing z to a
c=-1
for i in s1:
    print(s1[c],end="")
    c=c+(-1)
